def pascals_triangle(n):
    """
    Prints the Pascal Triangle to the console
    :param n: a number of lines in pascal triangle
    """

    for line in range(1, n + 1):
        C = 1
        for i in range(1, line + 1):
            print(C, end=' ')
            C = C * (line - i) // i
        print()
