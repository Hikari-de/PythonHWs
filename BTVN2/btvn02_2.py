day = int(input("Date: "))
month = int(input("Month: "))

if month < 1 or month > 12:
    print("Invalid input")
else:
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif month in [4, 6, 9, 11]:
        max_day = 30
    else:
        max_day = 28

    if day < 1 or day > max_day:
        print("Invalid input")
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        print("Bạch Dương")
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        print("Kim Ngưu")
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        print("Song Tử")
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        print("Cự Giải")
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        print("Sư Tử")
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        print("Xử Nữ")
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        print("Thiên Bình")
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        print("Bọ Cạp")
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        print("Nhân Mã")
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        print("Ma Kết")
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        print("Bảo Bình")
    else:
        print("Song Ngư")