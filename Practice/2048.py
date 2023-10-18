import random

grade = 0
number = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
while True:
    while True:
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        z = random.choice([2, 4])
        if number[x][y] == 0:
            number[x][y] = z
            break
    print(grade)
    for i in range(4):
        for j in range(4):
            print(number[i][j], end = ' ')
        print()
    z = int(input())
    if z == 1:
        for i in range(4):
            for k in range(3):
                for j in range(3):
                    if number[i][j] == number[i][j + 1]:
                        number[i][j] += number[i][j + 1]
                        number[i][j + 1] = 0
                        grade += number[i][j]
                    elif number[i][j] == 0:
                        number[i][j] = number[i][j + 1]
                        number[i][j + 1] = 0
    elif z == 2:
        for i in range(4):
            for k in range(3):
                for j in range(1, 4):
                    if number[i][j] == number[i][j - 1]:
                        number[i][j] += number[i][j - 1]
                        number[i][j - 1] = 0
                        grade += number[i][j]
                    elif number[i][j] == 0:
                        number[i][j] = number[i][j - 1]
                        number[i][j - 1] = 0
    elif z == 3:
        for i in range(4):
            for k in range(3):
                for j in range(3):
                    if number[j][i] == number[j + 1][i]:
                        number[j][i] += number[j][i]
                        number[j + 1][i] = 0
                        grade += number[j][i]
                    elif number[j][i] == 0:
                        number[j][i] = number[j + 1][i]
                        number[j + 1][i] = 0
    elif z == 4:
        for i in range(4):
            for k in range(3):
                for j in range(1, 4):
                    if number[j][i] == number[j - 1][i]:
                        number[j][i] += number[j - 1][i]
                        number[j - 1][i] = 0
                        grade += number[j][i]
                    elif number[j][i] == 0:
                        number[j][i] = number[j - 1][i]
                        number[j - 1][i] = 0
