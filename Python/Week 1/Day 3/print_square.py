#User function Template for python3
n = int(input())

print((n - 1) * "* ", end="")
print("*")

for i in range(n - 2):
    print("*", end="")
    print(" "  * (2 * n - 3), end="")
    print("*")

print((n - 1) * "* ", end="")
print("*")
