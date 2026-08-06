celsius_to_fahrenheit = lambda c: c * 9 / 5 + 32

even_or_odd = lambda n: "Even" if n % 2 == 0 else "Odd"

calculate_tip = lambda bill, tip_percent: bill * tip_percent / 100

uppercase_name = lambda name: name.upper()

print(celsius_to_fahrenheit(30))
print(even_or_odd(15))
print(calculate_tip(500000, 10))
print(uppercase_name("tran thi b"))