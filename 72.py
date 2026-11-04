rooms = [
    [101, 120, 80],
    [102, 250, 150],
    [103, 180, 90],
    [104, 300, 200]
]

for room in rooms:
    electricity = room[1]
    water = room[2]

    electricity_charge = electricity * 5
    water_charge = water * 2
    total = electricity_charge + water_charge

    print("\nRoom:", room[0])
    print("Electricity:", electricity)
    print("Water:", water)
    print("Total Charge:", total)

    if electricity > 200 or water > 150:
        print("Warning: Consumption Limit Exceeded")
    else:
        print("Normal Consumption")
