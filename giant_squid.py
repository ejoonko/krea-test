n = 100

ball_array = [int(n) for n in input().split(",")]
bingo_array = [[[False for i in range(5)] for j in range(5)] for k in range(n)]
number_array = [[[0 for x in range(5)] for y in range(5)] for z in range(n)]
coordinate_array = dict()
winning_array = []


def check_winners():
    count = 0
    for board in bingo_array:
        # check row wins
        for i in range(5):
            if all(board[i]) and count not in winning_array:
                winning_array.append(count)

        # check column wins
        for i in range(5):
            check = True
            for j in range(5):
                check = check and board[j][i]
            if check and count not in winning_array:
                winning_array.append(count)
        count += 1
    return


for i in range(n):
    input()
    for j in range(5):
        bingo_row = input().split()
        for k in range(len(bingo_row)):
            if bingo_row[k].isdigit():
                if int(bingo_row[k]) in coordinate_array:
                    coordinate_array[int(bingo_row[k])].append((i, j, k))
                else:
                    coordinate_array[int(bingo_row[k])] = [(i, j, k)]
            number_array[i][j][k] = int(bingo_row[k])

for number in ball_array:
    if number in coordinate_array:
        for coordinate in coordinate_array[number]:
            bingo_array[coordinate[0]][coordinate[1]][coordinate[2]] = True
    check_winners()
    if len(winning_array) == n:
        unmarked_sum = 0
        for i in range(5):
            for j in range(5):
                if not bingo_array[winning_array[-1]][i][j]:
                    unmarked_sum += number_array[winning_array[-1]][i][j]
        print(unmarked_sum * number)
        exit()
