import math
print("Input your A(x1,y1) value: ")
x1 = int(input())
y1 = int(input())
print("Input your B(x2,y2) value: ")
x2 = int(input())
y2 = int(input())
v1 = (x1-x2)**2
v2 = (y1-y2)**2
sum = v1 + v2
d = math.sqrt(sum)
print(f"distant of A and B axix is: {d:.3f}")