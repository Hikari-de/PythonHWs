
text = input("Enter a string: ")
reverse_text = ""

for i in range(len(text) - 1, -1, -1):
    reverse_text += text[i]

print("Reversed string:", reverse_text)

sorted_text = "".join(sorted(text))
print("Sorted string:", sorted_text)

if text == reverse_text:
    print("Palindrome: Yes")
else:
    print("Palindrome: No")

max_count = 0

for char in set(text):
    if text.count(char) > max_count:
        max_count = text.count(char)

most_chars = []

for char in sorted(set(text)):
    if text.count(char) == max_count:
        most_chars.append(char)

print("Most frequent character(s):", " ".join(most_chars))
print("Count:", max_count)

lower_text = text.lower()

vowels = {"a", "e", "i", "o", "u"}

if vowels.issubset(set(lower_text)):
    print("Contains all 5 vowels.")
else:
    print("Does not contain all 5 vowels.")