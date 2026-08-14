products = []
n = int(input("number of product: "))

for i in range(n):
    while True:
        code = input("product ID: ")
        if all(code != p[0] for p in products):
            break
        print("Product already has ID")

    name = input("Name: ")

    while True:
        price = float(input("Price: "))
        if price > 0:
            break

    while True:
        quantity = int(input("Quantity: "))
        if quantity >= 0:
            break

    products.append((code, name, price, quantity))

print("Money:")
for p in products:
    print(p[1], ":", p[2] * p[3])

print("Max value:", max(products, key=lambda x: x[2] * x[3]))

print("Not has much:")
for p in products:
    if p[3] < 5:
        print(p)

code = input("Input your ID: ")
for p in products:
    if p[0] == code:
        print(p)

print("Sum: ", sum(p[2] * p[3] for p in products))