import random

# Define rows and columns
def matrix(x, y):
    row, col = (x, y)

# Create a matrix using list comprehension
    matrix = [[random.randint(0, 100) for _ in range(col)] for _ in range(row)]

# Print the matrix
    for r in matrix:
        print(r)

x = int(input("Enter the number of Rows in a Matrix: "))
y = int(input("Enter the number of Columns in a Matrix: "))

matrix(x,y)
