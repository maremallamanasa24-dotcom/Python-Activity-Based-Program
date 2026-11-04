routes = [
    ["Route A", 40, 60, 8, 10],
    ["Route B", 70, 60, 10, 8],
    ["Route C", 50, 50, 7, 9],
    ["Route D", 30, 60, 6, 12]
]

for r in routes:
    name = r[0]
    passengers = r[1]
    capacity = r[2]
    journey_time = r[3]
    fuel = r[4]

    print("\nRoute:", name)
    print("Passengers:", passengers)
    print("Capacity:", capacity)
    print("Journey Time:", journey_time)
    print("Fuel Used:", fuel)

    if passengers > capacity:
        print("Status: Overloaded")
    else:
        print("Status: Normal")

    efficiency = passengers / fuel
    print("Fuel Efficiency:", round(efficiency, 2))
