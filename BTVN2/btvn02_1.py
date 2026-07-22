month = int(input("Month: "))
year = int(input("Year: "))

if month < 1 or month > 12:
    print("Month Invalid")
elif month in [1, 3, 5, 7, 8, 10, 12]:
    print(31)
elif month in [4, 6, 9, 11]:
    print(30)
else:
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(29)
    else:
        print(28)