students = [
    [101, "Ravi", 5000, 5000, 85, 75],
    [102, "Sita", 3000, 5000, 90, 80],
    [103, "Ram", 5000, 5000, 60, 35],
    [104, "Priya", 5000, 5000, 80, 25]
]

for s in students:
    print("\nStudent:", s[1])
    reasons = []

    if s[2] < s[3]:
        reasons.append("Fee Pending")
    if s[4] < 75:
        reasons.append("Attendance Shortage")
    if s[5] < 40:
        reasons.append("Internal Marks Low")

    if reasons:
        print("Not Eligible:", ", ".join(reasons))
    else:
        print("Eligible for Examination")
