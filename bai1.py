a = int(input("a value: "))
b = int(input("b value: "))
sum = a + b
neg = a - b
multi = a * b
div = a / b

print("sum = ", sum)
print("neg = ", neg)
print("multi = ", multi)
if b != 0:
     print("div = ", div)
else:
    print("cannot div for zero")