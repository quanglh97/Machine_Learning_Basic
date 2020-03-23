#cong 2 vector
def add_vector(vector1, vector2):
    return [v1 + v2 for v1, v2 in zip(vector1, vector2)]

#minus 2 vector
def minus_vector(vector1, vector2):
    return[v1 - v2 for v1, v2 in zip(vector1, vector2)]

#matrix_multiplication
def matrix_multiplication(matrix1, matrix2):
    matrix1_nrows = len(matrix1)
    matrix1_ncols = len(matrix1[0])

    matrix2_nrows = len(matrix2)
    matrix2_ncols = len(matrix2[0])

    if matrix1_ncols != matrix2_nrows:
        print("2 ma tran ko hop le\n")
        return

    #add matrix result
    result =[[0]*matrix2_ncols for i in range(matrix1_nrows)]

    for i in range(matrix1_nrows):
        for j in range(matrix2_ncols):
            for k in range(matrix2_nrows):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


#check function add vector
vector1 = [1,3]
vector2 = [4,6]
added_vector = add_vector(vector1, vector2)
minused_vector = minus_vector(vector1, vector2)


matrix1 =  [[1,2,3],
            [4,5,6],
            [7,8,9]]

matrix2 =  [[1,2,3,1],
            [4,5,6,1],
            [7,8,9,1],[7,8,9,1]]

matrix3 = matrix_multiplication(matrix1, matrix2)
print(matrix3)
