
def rotate(matrix):
    result = []

    for j in range(4):
        new_row = []
        for i in reversed(range(4)):
            new_row.append(matrix[i][j])
        result.append(new_row)

    return result

def rotate_inplace(matrix):
    length = len(matrix)
    for i in range(length / 2):
        lower = 0
        higher = length - 1
        for j in range(length):
            matrix[j][higher] = matrix[lower][j]
            matrix[lower][j] = matrix[higher][j]

        lower += 1
        higher -= 1

    return matrix

if __name__ == "__main__":
    print(rotate([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]))

    print(rotate_inplace([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]))
