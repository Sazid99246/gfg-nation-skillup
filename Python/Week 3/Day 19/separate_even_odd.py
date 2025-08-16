# User function Template for python3


def evenOdd(arr):
    even = []
    odd = []

    # Write your code below to append odd elements in numbers to odd list
    # Write your code below to append even elements in numbers to even list
    for i in arr:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    return (even, odd)  # This is the return statement
