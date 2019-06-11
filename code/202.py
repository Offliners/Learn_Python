# transpose a matrix

matrix = [[10,20,30],
          [40,50,60]]

# using nested list comprehensions
transposed_matrix = [
    [
        matrix[j][i] for j in range(len(matrix))
    ]
    for i in range(len(matrix[0]))
]

print(transposed_matrix)

# Output:
# [[10, 40], [20, 50], [30, 60]]
