import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = 0 if parent is None else parent.cost + 1

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.state == other.state

def is_goal(state):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return state == goal_state

def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(node):
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = []

    blank_i, blank_j = get_blank_position(node.state)

    for move_i, move_j in moves:
        new_i, new_j = blank_i + move_i, blank_j + move_j

        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row[:] for row in node.state]
            new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]
            neighbors.append(PuzzleNode(new_state, node, (new_i, new_j)))

    return neighbors

def solve_8_puzzle(initial_state):
    initial_node = PuzzleNode(initial_state)
    frontier = [initial_node]
    explored = set()

    while frontier:
        node = heapq.heappop(frontier)

        if is_goal(node.state):
            path = []
            while node:
                path.append(node.state)
                node = node.parent
            return path[::-1]

        explored.add(tuple(map(tuple, node.state)))

        for neighbor in get_neighbors(node):
            if tuple(map(tuple, neighbor.state)) not in explored:
                heapq.heappush(frontier, neighbor)

    return None

# Example usage:
initial_state = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
solution_path = solve_8_puzzle(initial_state)

if solution_path:
    for step, state in enumerate(solution_path):
        print(f"Step {step + 1}:")
        for row in state:
            print(row)
        print("--------")
else:
    print("No solution found.")
