def dathuc(x, a):
    sum = 0
    n = len(a)-1
    for i in a:
     sum += i * (x**n)
     n -= 1
    return sum
x = int(input("nhap x: " ))
a = list(map(int,input().split()))
print(dathuc(x,a))
