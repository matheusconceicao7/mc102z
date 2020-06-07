# Returns:
# 0 - Alive
# 1 - Death


def verify_arround_and_define_state(x, y, max_x, max_y, matrix):
    if(x < 2 or x >= max_x or y < 2 or y >= max_y):
        return 1
    else:
        alive_cells_arround_count = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if((i != x or j != y) and matrix[i][j] == "@"):
                    alive_cells_arround_count = alive_cells_arround_count + 1
                # print("x: {} y: {} i: {} j: {}. count = {}".format(
                #     x, y, i, j, alive_cells_arround_count))
        if(matrix[x][y] == "@"):
            if alive_cells_arround_count >= 2 and alive_cells_arround_count < 4:
                return 0
            else:
                return 1
        else:
            if alive_cells_arround_count == 3:
                return 0
            return 1


def is_inside_matrix(caractere):
    if caractere == "-" or caractere == "+" or caractere == "|":
        return False
    else:
        return True


def god_decision(state):
    if state == 0:
        return "@"
    return " "


line = input()
matrix = []
while not line.isnumeric():
    matrix.append(line)
    line = input()

for i in matrix:
    print(i)
for _ in range(int(line)):
    newMatrix = []
    for line_index, line in enumerate(matrix):
        newLine = ""
        for column_index, value in enumerate(line):
            if is_inside_matrix(value):
                state = verify_arround_and_define_state(
                    line_index, column_index, len(line) - 1, len(matrix) - 1, matrix)
                newLine = newLine + god_decision(state)
            else:
                newLine = newLine + value
        newMatrix.append(newLine)

    for i in newMatrix:
        print(i)
    matrix = newMatrix.copy()
