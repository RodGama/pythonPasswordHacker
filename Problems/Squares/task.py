n = int(input())


def squares():
    for num in range(1, n+1, 1):
        yield num**2


# Don't forget to print out the first n numbers one by one here
for x in squares():
    print(x)
