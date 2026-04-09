def multiplyMatrix(matrixOne, matrixTwo):
    matrixOne = [[a+1, b+2] for a in range(rows) for b in range(cols)]
    matrixTwo = [[a+3, b+4] for a in range(rows) for b in range(cols)]

    totalSumListingsTwo = sum(a*b for rowOne, rowTwo in zip(matrixOne, matrixTwo) for a,b in zip(rowOne, rowTwo))
    return totalSumListingsTwo

def sumMatrix(matrixOne, matrixTwo):
    matrixOne = [[a+1, b+2] for a in range(rows) for b in range(cols)]
    matrixTwo = [[a+3, b+4] for a in range(rows) for b in range(cols)]

    totalSumListings = sum(a+b for rowOne, rowTwo in zip(matrixOne, matrixTwo) for a,b in zip(rowOne, rowTwo))
    return totalSumListings

def transposeMatrix(matrixOne):
    matrixOne = [[a+1, b+2] for a in range(rows) for b in range(cols)]
    return matrixOne

def scalarMatrix(matrixOne, matrixTwo):
    matrixOne = [[a+1, b+2] for a in range(rows) for b in range(cols)]
    matrixTwo = [[a+3, b+4] for a in range(rows) for b in range(cols)]

    scalarMatrixX = [[a*b, c*d] for (a, c), (b, d) in zip(matrixOne, matrixTwo)]
    return scalarMatrixX

rows = int(input("Number of rows: "))
cols = int(input("Number of columns: "))

matrixO = [[i+1, j+2] for i in range(rows) for j in range(cols)]
matrixT = [[i+3, j+4] for i in range(rows) for j in range(cols)]

print(matrixO)
print(matrixT)

print(f"Total sum = {multiplyMatrix(matrixO, matrixT)}")
print(f"Total product = {sumMatrix(matrixO, matrixT)}")
print(f"Transpose MatrixOne: {transposeMatrix(matrixO)}")
print(f"Transpose MatrixTwo: {transposeMatrix(matrixT)}")
print(F"Scalar Matrix: {scalarMatrix(matrixO, matrixT)}")
