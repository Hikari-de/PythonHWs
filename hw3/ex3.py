
hobbies_a = input("Enter hobbies of A: ")
hobbies_b = input("Enter hobbies of B: ")

set_a = set()
set_b = set()

for hobby in hobbies_a.split(","):
    hobby = hobby.strip().title()
    set_a.add(hobby)

for hobby in hobbies_b.split(","):
    hobby = hobby.strip().title()
    set_b.add(hobby)

print("Hobbies of A:")
print(set_a)

print("\nHobbies of B:")
print(set_b)

common = set_a & set_b

print("\nCommon hobbies:")
if len(common) > 0:
    print(common)
else:
    print("No common hobbies.")

only_a = set_a - set_b

print("\nOnly A has:")
print(only_a)

all_hobbies = set_a | set_b

print("\nAll hobbies:")
print(all_hobbies)

if len(all_hobbies) == 0:
    similarity = 0
else:
    similarity = len(common) / len(all_hobbies) * 100

print("\nSimilarity: {:.2f}%".format(similarity))