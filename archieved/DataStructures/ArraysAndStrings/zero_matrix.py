
def zero_matrix(matrix):
    zero_rows = []
    zero_columns = []

    row_length = len(matrix)
    column_length = len(matrix[0])

    for i in range(row_length):
        for j in range(column_length):
            if matrix[i][j] == 0:
                zero_rows.append(i)
                zero_columns.append(j)

    i = 0
    while i < len(zero_rows):
        zero_out_row(matrix, zero_rows[i])
        zero_out_column(matrix, zero_columns[i])
        i += 1

    return matrix

def zero_out_row(matrix, i):
    for j in range(len(matrix[i])):
        matrix[i][j] = 0

def zero_out_column(matrix, j):
    for i in range(len(matrix)):
        matrix[i][j] = 0


if __name__ == "__main__":
    print(zero_matrix([
        [1, 2, 3, 4, 0],
        [6, 0, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 0, 18, 19, 20],
        [21, 22, 23, 24, 25]]))
