####################################################################################################
### read and process

f = open("3.txt", "r")
lines = f.read()
f.close()

# keep an example at hand
# lines = """00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010"""

# import numpy for ease of array indexing
import numpy as np

# transform raw text into np
lines = lines.split("\n")
for i, l in enumerate(lines):
    new_l = list(l)
    new_l = list(map(int, new_l))
    lines[i] = new_l

lines = np.array(lines)
lines

# save shape, used later
n, m = lines.shape
# print(f"n: {n} ; m: {m}")

# utility function to help binary to decimal conversion
def binary_to_decimal(binary_str):
    n_digits = len(binary_str)
    decimal = 0
    for i, digit in enumerate(binary_str):
        decimal += int(digit) * 2 ** (n_digits - i - 1)
    return decimal

####################################################################################################
### PART 1

gamma = ""
epsilon = ""

# iterate through the column
for i in range(m):

    # calculate column sum
    s = np.sum(lines[:, i])

    # compare it with half length
    if n / 2 < s: # 1 is majority
        gamma += "1"
        epsilon += "0"

    else: # 0 is majority
        gamma += "0"
        epsilon += "1"

# print(f"Gamma: {gamma}")
# print(f"Epsilon: {epsilon}")

gamma = binary_to_decimal(gamma)
epsilon = binary_to_decimal(epsilon)

# print(f"Gamma: {gamma}")
# print(f"Epsilon: {epsilon}")

ans = gamma * epsilon
print(f"Answer: {ans}")

####################################################################################################
### PART 2

# function to find rates for o2 and co2
def bit_crit(input):

    # recall shape of array
    global n, m

    # init local array : will be filtered until 1 value
    local = lines.copy()

    # boolean mask for filtering
    mask = np.array([True] * n)

    for i in range(m):

        # select column, calculate length and sum
        column = local[:, i]
        l = len(column)
        s = sum(column)
    
        # update mask
        if l / 2 <= s: # if 1 is majority, set 1 for o2, or 0 for co2
            mask = (column == 1) if input == "o2" else (column == 0)
        else: # vice versa
            mask = (column == 0) if input == "o2" else (column == 1)

        # filter local, break out if only one line
        local = local[mask]
        if len(local) == 1:
            break
    
    # format back into str
    local = list(local[0])
    local = list(map(str, local))
    local = "".join(local)

    return local

o2_gen = bit_crit("o2")
co2_scrub = bit_crit("co2")
# print(o2_gen, co2_scrub)

o2_gen = binary_to_decimal(o2_gen)
co2_scrub = binary_to_decimal(co2_scrub)
# print(o2_gen, co2_scrub)

ans = o2_gen * co2_scrub
print(f"Answer: {ans}")
