if __name__ == "__main__":
    matrix = [
        [i*j for j in range(1, 10)]
        for i in range(1, 10)
    ]

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            ceil = matrix[row][col]
            print(f'{ceil:2}', end=" ")
        print()
