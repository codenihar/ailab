from collections import deque

def find_blank(puzzle):
    for i, row in enumerate(puzzle):
        if 0 in row:
            return i, row.index(0)

def possible_moves(puzzle):
    moves = []
    row, col = find_blank(puzzle)
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_puzzle = [list(row) for row in puzzle]
            new_puzzle[row][col], new_puzzle[new_row][new_col] = new_puzzle[new_row][new_col], new_puzzle[row][col]
            moves.append(new_puzzle)
    return moves

def bfs(puzzle):
    visited = set()
    queue = deque([(puzzle, [])])

    while queue:
        node, path = queue.popleft()
        if node == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            return path
        visited.add(str(node))
        for move in possible_moves(node):
            if str(move) not in visited:
                queue.append((move, path + [move]))

initial_puzzle = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

solution = bfs(initial_puzzle)
print("Solution Steps:")
for step in solution:
    print(step)
