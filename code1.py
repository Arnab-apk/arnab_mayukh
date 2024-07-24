def grid():
    n = 0
    while (n <= 10):
        if (n == 0 or n == 5 or n == 10):
            print("+ - - - - + - - - - +")
        else:
            print("|         |         |")
        n += 1
grid()
