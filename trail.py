from collections import deque

class State:
    def __init__(self, left_missionaries, left_cannibals, boat, right_missionaries, right_cannibals):
        self.left_missionaries = left_missionaries 
        self.left_cannibals = left_cannibals 
        self.boat = boat
        self.right_missionaries = right_missionaries 
        self.right_cannibals = right_cannibals

    def is_valid(self):
        if (self.left_missionaries < 0 or self.left_cannibals < 0 or
            self.right_missionaries < 0 or self.right_cannibals < 0):
            return False
        if (self.left_missionaries > 0 and self.left_missionaries < self.left_cannibals) or \
           (self.right_missionaries > 0 and self.right_missionaries < self.right_cannibals):
            return False
        return True

    def is_goal(self):
        return self.left_missionaries == 0 and self.left_cannibals == 0


actions = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

def generate_successors(current_state):
    successors = []
    for action in actions:
        if current_state.boat == 0:
            new_left_missionaries = current_state.left_missionaries - action[0]
            new_left_cannibals = current_state.left_cannibals - action[1]
            new_right_missionaries = current_state.right_missionaries + action[0]
            new_right_cannibals = current_state.right_cannibals + action[1]
            new_boat = 1
        else:
            new_left_missionaries = current_state.left_missionaries + action[0]
            new_left_cannibals = current_state.left_cannibals + action[1]
            new_right_missionaries = current_state.right_missionaries - action[0]
            new_right_cannibals = current_state.right_cannibals - action[1]
            new_boat = 0
        new_state = State(new_left_missionaries, new_left_cannibals, new_boat, new_right_missionaries, new_right_cannibals)
        if new_state.is_valid():
            successors.append(new_state)
    return successors

def bfs():
    initial_state = State(3, 3, 0, 0, 0)
    if initial_state.is_goal():
        return [initial_state]
    visited = set()
    queue = deque([initial_state])
    parent = {}
    while queue:
        current_state = queue.popleft()
        for successor in generate_successors(current_state):
            if successor not in visited:
                visited.add(successor)
                queue.append(successor)
                parent[successor] = current_state
            if successor.is_goal():
                path = []
                while successor != initial_state:
                    path.append(successor)
                    successor = parent[successor]
                path.append(initial_state)
                path.reverse()
                return path
    return None

def main():
    solution = bfs()
    if solution:
        print("Solution found:")
        for step, state in enumerate(solution, 1):
            print(f"Step {step}: {state.left_missionaries}M-{state.left_cannibals}C {state.boat} {state.right_missionaries}M-{state.right_cannibals}C")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
