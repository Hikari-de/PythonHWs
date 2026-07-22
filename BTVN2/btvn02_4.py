money = int(input("Input coin: "))

beer = money // 28
total = beer
empty = beer

while empty >= 3:
    new_beer = empty // 3
    total += new_beer
    empty = empty % 3 + new_beer

print("The number of beer can buy:", total)