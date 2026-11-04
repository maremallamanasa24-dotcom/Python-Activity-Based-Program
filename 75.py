students = [
    (101, "Ravi", 85, 90, "Python"),
    (102, "Sita", 75, 80, "Java"),
    (103, "", 110, 70, "Python"),
    (101, "Ravi", 85, 90, "Python")
]

ids = []

for s in students:
    print("\nStudent ID:", s[0])

    errors = []

    if s[0] in ids:
        errors.append("Duplicate ID")
    else:
        ids.append(s[0])

    if s[1] == "":
        errors.append("Missing Name")

    if s[2] < 0 or s[2] > 100:
        errors.append("Invalid Marks")

    if s[3] < 0 or s[3] > 100:
        errors.append("Invalid Attendance")

    if s[4] == "":
        errors.append("Missing Course")

    if errors:
        print("Errors:", ", ".join(errors))
    else:
        print("Record is Valid")
