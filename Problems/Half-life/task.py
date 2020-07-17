N = int(input())
R = int(input())
T = 0
while N >= R:
    N = N / 2
    T += 1
A = T * 12
print(A)
