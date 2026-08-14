name = input("Full name: ").lower().split()
print(" ".join(i[0].upper() + i[1:] for i in name))

while True:
    user = input("Username: ")
    if (6 <= len(user) <= 20 and user[0].isalpha()
            and user.isalnum()
            and any(c.isdigit() for c in user)):
        break
    print("Invalid!")

while True:
    pw = input("Password: ")
    if (len(pw) >= 8 and " " not in pw
            and any(c.isupper() for c in pw)
            and any(c.islower() for c in pw)
            and any(c.isdigit() for c in pw)
            and any(not c.isalnum() for c in pw)):
        break
    print("Invalid!")

print("Your form is succesful!")