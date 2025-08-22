from collections import deque

def get_neighbors(state):
    neighbors = []
    zero_idx = state.index(0)
    row, col = divmod(zero_idx, 3)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        nr, nc = row + dr, col + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            swap_idx = nr * 3 + nc
            new_state = list(state)
            new_state[zero_idx], new_state[swap_idx] = new_state[swap_idx], new_state[zero_idx]
            neighbors.append(tuple(new_state))

    return neighbors

def solve_bfs(initial, goal):
    queue = deque([initial])
    visited = {initial}
    parent = {initial: None}

    while queue:
        state = queue.popleft()
        if state == goal:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return path[::-1]

        for neigh in get_neighbors(state):
            if neigh not in visited:
                visited.add(neigh)
                parent[neigh] = state
                queue.append(neigh)

    return None

def solve_dfs(initial, goal, max_depth=50000):
    stack = [(initial, [initial])]
    visited = set()

    while stack:
        state, path = stack.pop()
        if state == goal:
            return path

        if state not in visited and len(path) <= max_depth:
            visited.add(state)
            for neigh in get_neighbors(state):
                if neigh not in visited:
                    stack.append((neigh, path + [neigh]))

    return None

if __name__ == "__main__":
    start = (1, 2, 3,
             4, 0, 6,
             7, 5, 8)

    goal = (1, 2, 3,
            4, 5, 6,
            7, 8, 0)

    bfs_path = solve_bfs(start, goal)
    print(f"BFS encontrou em {len(bfs_path)-1} movimentos:")
    for step in bfs_path:
        print(step)

    dfs_path = solve_dfs(start, goal)
    if dfs_path:
        print(f"\nDFS encontrou em {len(dfs_path)-1} movimentos:")
        for step in dfs_path:
            print(step)
    else:
        print("\nDFS não encontrou solução dentro do limite de profundidade.")
