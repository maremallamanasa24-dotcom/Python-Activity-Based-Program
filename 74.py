participants = [101, 102, 103, 102, 104]
registration_fee = 200

sponsorship = 5000
expenses = 3000

unique = []

for p in participants:
    if p in unique:
        print("Duplicate Registration:", p)
    else:
        unique.append(p)

total = len(unique) * registration_fee
balance = total + sponsorship - expenses

print("\nTotal Participants:", len(unique))
print("Registration Collection:", total)
print("Sponsorship:", sponsorship)
print("Expenses:", expenses)
print("Final Balance:", balance)

if balance > 0:
    print("Financial Status: Profit")
elif balance < 0:
    print("Financial Status: Loss")
else:
    print("Financial Status: Balanced")
