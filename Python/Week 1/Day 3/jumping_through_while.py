def printIncreasingPower(x):
    i = 1
    # Loop to jump in powers of 2
    while (i * i <= x):
        print(i * i, end=" ")
        i += 1


printIncreasingPower(10)
print()
printIncreasingPower(50)
print()
printIncreasingPower(100)
print()
