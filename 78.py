wards = [
    ["General", 20, 18, 5, 6],
    ["ICU", 10, 10, 3, 5],
    ["Emergency", 15, 12, 4, 3],
    ["Children", 12, 8, 2, 4]
]

for w in wards:
    name = w[0]
    beds = w[1]
    occupied = w[2]
    staff = w[3]
    equipment = w[4]

    available = beds - occupied

    print("\nWard:", name)
    print("Available Beds:", available)
    print("Staff:", staff)
    print("Equipment:", equipment)

    if available == 0 or staff < 3 or equipment < 4:
        print("Warning: Resource Shortage")
    else:
        print("Resources Available")
