students = [
    {"name": "Tran Thi B", "score": {"Math": 8, "Literature": 7, "English": 9}},
    {"name": "Nguyen Van A", "score": {"Math": 9, "Literature": 6, "English": 9}},
    {"name": "Le Van C", "score": {"Math": 9, "Literature": 8, "English": 8}},
    {"name": "Pham Thi D", "score": {"Math": 6, "Literature": 5, "English": 7}}
]

math_sorted = sorted(
    students,
    key=lambda student: student["score"]["Math"],
    reverse=True
)

print("1. Sort by Math score:")
for student in math_sorted:
    print(student["name"])

top_english = max(
    students,
    key=lambda student: student["score"]["English"]
)

print("\n2. Highest English score:")
print(top_english["name"])

total_sorted = sorted(
    students,
    key=lambda student: (
        -(student["score"]["Math"] +
          student["score"]["Literature"] +
          student["score"]["English"]),
        student["name"]
    )
)

print("\n3. Sort by total score:")
for student in total_sorted:
    print(student["name"])

excellent_students = list(
    map(
        lambda student: student["name"],
        sorted(
            filter(
                lambda student:
                student["score"]["Math"] +
                student["score"]["Literature"] +
                student["score"]["English"] >= 24,
                students
            ),
            key=lambda student:
            student["score"]["Math"] +
            student["score"]["Literature"] +
            student["score"]["English"],
            reverse=True
        )
    )
)

print("\n4. Excellent students:")
print(excellent_students)