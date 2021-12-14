####################################################################################################
### PROCESS

# small example
lines = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

# overwrite input here
f = open("4.txt", "r")
lines = f.read()
f.close()

lines = lines.split("\n")

# process numbers in the first line
numbers = lines[0]
numbers = numbers.split(",")
numbers = list(map(int, numbers))
# print(numbers)

lines = lines[2:]
boards = []

ll = len(lines)
for i in range(0, ll, 6):

    # extract one board
    b = lines[i : i + 6]

    # remove one empty line space in the end
    if len(b) == 6:
        b = b[ : -1 ]
    # print(b)
    
    # process from raw to array
    b = [ row.strip().replace("  ", " ") for row in b ]
    b = [ row.split(" ") for row in b ]
    b = [ list(map(int, row)) for row in b ]
    # print(b)

    boards.append(b)

# check
# for i, b in enumerate(boards):
#     print(i)
#     for row in b:
#         print(row)


####################################################################################################
### PART 1

lb = len(boards)

# cannot create the mask like this, the * operator creates same references, rookie mistake
# masks = [ [ [0] * 5 ] * 5 ] * lb
# answers here: https://stackoverflow.com/questions/3854870/python-replacing-an-element-in-a-list-of-lists-2
masks = [ [ [ False for k in range(5) ] for j in range(5) ] for i in range(lb) ]

winner = False
w = None

# start listing th numbers
for i, nbr in enumerate(numbers):

    if winner:
        break

    # print(f"i: {i}, number: {nbr}")

    # given a number, check each board
    for j, brd in enumerate(boards):
        # print(f"j: {j}")
        # print(brd)

        # look for the called number
        fnd = False
        loc = None
        for k, row in enumerate(brd):
            # break out as soon as found
            if fnd:
                break
            else:
                for l, itm in enumerate(row):
                    fnd = (fnd or (itm == nbr))
                    if fnd:
                        loc = (k, l)
                        break

        # if number found on board, mark it on the mask
        if fnd:
            masks[j][loc[0]][loc[1]] = True

        # calculate horizontal sums in mask
        row_sms = [0 for k in range(5)]
        for k in range(5):
            for l in range(5):
                row_sms[k] += masks[j][k][l]
        # print(row_sms)

        # vertical sums of mask
        col_sms = [0 for k in range(5)]
        for k in range(5):
            for l in range(5):
                col_sms[k] += masks[j][l][k]
        # print(col_sms)

        # if either a row or a column is filled
        if (5 in row_sms) or (5 in col_sms):

            # declare winner
            winner = True
            w = j

            # print(f"Board with index {w} won")
            # print(boards[w])
            # print(masks[w])

            # calculate unmarked items
            s = 0
            for k in range(5):
                for l in range(5):
                    if not masks[w][k][l]:
                        s += boards[w][k][l]
            # print(s)

            # solution and break out
            ans = s * nbr
            print(f"Ans: {ans}")
            break
