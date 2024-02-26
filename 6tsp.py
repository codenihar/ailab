from itertools import permutations

def calculate_total_distance(route, distances):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distances[route[i]][route[i + 1]]
    total_distance += distances[route[-1]][route[0]]  # Return to the starting city
    return total_distance

def traveling_salesman_bruteforce(distances):
    num_cities = len(distances)
    all_routes = permutations(range(num_cities))

    min_distance = float('inf')
    best_route = None

    for route in all_routes:
        current_distance = calculate_total_distance(route, distances)
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = route

    return best_route, min_distance

# Example usage:
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

best_route, min_distance = traveling_salesman_bruteforce(distances)

print("Best Route:", best_route)
print("Minimum Distance:", min_distance)
