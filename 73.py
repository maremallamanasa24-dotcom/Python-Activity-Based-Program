packages = [
    [1, 10, "A", 1],
    [2, 25, "B", 2],
    [3, 15, "A", 1],
    [4, 40, "C", 3],
    [5, 60, "B", 2]
]

capacity = 50
vehicle = 1
used = 0

for p in packages:
    print("\nPackage:", p[0])
    print("Destination:", p[2])
    print("Weight:", p[1])

    if p[1] <= capacity:
        if used + p[1] <= capacity:
            used += p[1]
            print("Allocated to Vehicle", vehicle)
        else:
            vehicle += 1
            used = p[1]
            print("Allocated to Vehicle", vehicle)
    else:
        print("Cannot Dispatch: Exceeds Capacity")
