from collections import deque

# Map
maze = [['#','#','#','#','#','#','#','#','#','#','#'],
        ['#','S','#',' ',' ',' ',' ',' ','#',' ','#'],
        ['#',' ','#',' ','#','#','#',' ','#',' ','#'],
        ['#',' ','#',' ','#','G',' ',' ','#',' ','#'],
        ['#',' ','#',' ','#','#','#',' ','#',' ','#'],
        ['#',' ','#',' ','#',' ',' ',' ',' ',' ','#'],
        ['#',' ','#',' ','#','#','#','#','#',' ','#'],
        ['#',' ',' ',' ',' ',' ','#',' ',' ',' ','#'],
        ['#',' ','#',' ','#','#','#','#','#',' ','#'],
        ['#',' ','#',' ',' ',' ',' ',' ',' ',' ','#'],
        ['#','#','#','#','#','#','#','#','#','#','#']]

def bfs(maze):
    # Up, Down, Left, Right
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0), ]

    # Find the starting position
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 'S':
                start = (row, col)

    # Queue for BFS
    queue = deque([(start, [])])

    while queue: # While not empty
        (row, col), path = queue.popleft()

        # Check Goal
        if maze[row][col] == 'G':
            return path  # Path Found

        # Explore all directions
        for dr, dc in directions:
            r, c = row + dr, col + dc

            # Valid move
            if 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] != '#':
                new_path = path + [(r, c)]
                queue.append(((r, c), new_path))

    return None  # No Path Found

for r, c in bfs(maze):
    if maze[r][c] == 'S' or maze[r][c] == 'G':
        pass
    else:
        maze[r][c] = 'X'
for row in maze:
    print(' '.join(row))
