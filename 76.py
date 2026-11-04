students = [
    ["Ravi", 35, 38, 40],
    ["Sita", 28, 32, 35],
    ["Ram", 45, 48, 50]
]

moderation = 5
maximum = 100

for s in students:
    original = sum(s[1:])
    moderated_marks = []

    for mark in s[1:]:
        new_mark = min(mark + moderation, maximum)
        moderated_marks.append(new_mark)

    final = sum(moderated_marks)

    print("\nStudent:", s[0])
    print("Original Marks:", original)
    print("Moderated Marks:", final)

    if final >= 120:
        print("Result: Pass")
    else:
        print("Result: Fail")
