####################################################################################################
### read and process

f = open("2.txt", "r")
lines = f.read()
f.close()

# keep an example at hand
# lines = """forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2"""

lines = lines.split("\n")
lines = [ l.split(" ") for l in lines ]
lines = [ ( l[0], int(l[1]) ) for l in lines ]
# lines

####################################################################################################
### PART 1

# set initial horizontal and vertical pos
x = 0
y = 0

# process commands, one-by-one
for l in lines:
    if l[0] == "forward":
        x += l[1]
    if l[0] == "down":
        y += l[1]
    if l[0] == "up":
        y -= l[1]

# answer
ans = x * y
print(f"Answer: { ans }")

####################################################################################################
### PART 2

# same as previous, set aim too
x = 0
y = 0
a = 0

# modified process
for l in lines:
    if l[0] == "forward":
        x += l[1]
        y += l[1] * a
    if l[0] == "down":
        a += l[1]
    if l[0] == "up":
        a -= l[1]

# answer
ans = x * y
print(f"Answer: { ans }")
