def calculate_fare(distance):
    base = 50
    per_km = 10
    return base + per_km * distance

trips = [5, 10, 3]
total = 0

for i, distance in enumerate(trips):
    fare = calculate_fare(distance)
    print(f"Trip {i+1}: ${fare}")
    total += fare

print("Total Fare: $", total)
