orders = [
    [101, "Laptop", 20, 15, 1],
    [102, "Mouse", 30, 40, 2],
    [103, "Keyboard", 25, 10, 1],
    [104, "Monitor", 15, 15, 3]
]

for o in orders:
    order_id = o[0]
    product = o[1]
    demand = o[2]
    stock = o[3]
    priority = o[4]

    fulfilled = min(demand, stock)
    pending = demand - fulfilled

    print("\nOrder ID:", order_id)
    print("Product:", product)
    print("Priority:", priority)
    print("Fulfilled Quantity:", fulfilled)
    print("Outstanding Quantity:", pending)

    if pending == 0:
        print("Status: Fully Fulfilled")
    else:
        print("Status: Partially Fulfilled")
