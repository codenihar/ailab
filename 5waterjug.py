def water_jug_problem(capacity_jug1, capacity_jug2, target_amount):
    visited_states = set()
    frontier = [(0, 0)]

    while frontier:
        current_state = frontier.pop(0)
        jug1, jug2 = current_state

        if jug1 == target_amount or jug2 == target_amount:
            return current_state

        visited_states.add(current_state)

        next_states = [
            (jug1, 0),          # Empty jug2
            (0, jug2),          # Empty jug1
            (capacity_jug1, jug2),  # Fill jug1
            (jug1, capacity_jug2),  # Fill jug2
            (jug1 - min(jug1, capacity_jug2 - jug2), jug2 + min(jug1, capacity_jug2 - jug2)),  # Pour from jug1 to jug2
            (jug1 + min(jug2, capacity_jug1 - jug1), jug2 - min(jug2, capacity_jug1 - jug1))   # Pour from jug2 to jug1
        ]

        valid_next_states = [(next_jug1, next_jug2) for next_jug1, next_jug2 in next_states
                             if 0 <= next_jug1 <= capacity_jug1 and 0 <= next_jug2 <= capacity_jug2]

        for next_state in valid_next_states:
            if next_state not in visited_states and next_state not in frontier:
                frontier.append(next_state)

    return None

# Example usage:
capacity_jug1 = 4
capacity_jug2 = 3
target_amount = 2

result = water_jug_problem(capacity_jug1, capacity_jug2, target_amount)

if result:
    print(f"Solution found: Jug 1 = {result[0]}, Jug 2 = {result[1]}")
else:
    print("No solution found.")
