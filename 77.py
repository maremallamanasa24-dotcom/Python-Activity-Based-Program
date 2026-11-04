apartments = [
    [101, 100],
    [102, 250],
    [103, 400],
    [104, 150]
]

for a in apartments:
    units = a[1]

    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    else:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5

    fixed_charge = 50
    total = bill + fixed_charge

    if units < 100:
        total -= 20

    print("\nApartment:", a[0])
    print("Units:", units)
    print("Electricity Bill:", total)
