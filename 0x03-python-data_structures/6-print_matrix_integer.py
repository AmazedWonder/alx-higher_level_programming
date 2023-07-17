def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            # Print each number followed by a space
            print("{:d}".format(row[i]), end=" ")
        # Print a newline character at the end of each row
        print()
