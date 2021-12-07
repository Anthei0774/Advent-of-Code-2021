####################################################################################################
### read and process

f = open(path_to_drive + "1.txt", "r")
lines = f.read()
f.close()

# keep an example at hand
# lines = """199
# 200
# 208
# 210
# 200
# 207
# 240
# 269
# 260
# 263"""

lines = lines.split("\n")
lines = list(map(int, lines))
# lines

####################################################################################################
### PART 1

n = len(lines)

# all directions initialiased as no change
directions = [0] * n

for i in range(1, n):

    # rules for change upwards and downwards
    directions[i] = 1 if lines[i - 1] < lines[i] else -1

# directions
ans = directions.count(1)
print(f"Answer: { ans }")

####################################################################################################
### PART 2

# init 3-window sums : calculate first, set the rest to 0, mind the limit
sums = [ sum(lines[:3]) ] + [0] * (n - 2)

# same approach here
directions = [0] * (n - 2)

for i in range(1, n - 2):

    # calculate window
    sums[i] = sum(lines[i : i + 3])

    # check change
    directions[i] = 1 if sums[i - 1] < sums[i] else -1

# directions
ans = directions.count(1)
print(f"Answer: { ans }")
