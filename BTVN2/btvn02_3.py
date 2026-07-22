n = int(input("Input number: "))

temp = abs(n)

if temp == 0:
    count = 1
    total = 0
else:
    count = 0
    total = 0
    while temp > 0:
        total += temp % 10
        temp //= 10
        count += 1

if n < 2:
    prime = False
else:
    prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break

print("count number:", count)
print("Total number:", total)

if prime:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")