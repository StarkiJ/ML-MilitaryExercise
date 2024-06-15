from collections import deque


def find_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右

    # 检查是否越界或者是障碍物
    def is_valid(x, y):
        return (0 <= x < rows and 0 <= y < cols) and (grid[x][y] != '#' or (x, y) == end)

    # BFS队列
    queue = deque([(start[0], start[1], 0)])  # (x, y, steps, direction)
    visited = {start}  # 记录访问过的节点
    parent = {start: (None, None)}  # 记录每个节点的前驱节点和方向

    while queue:
        x, y, steps = queue.popleft()

        # 如果到达目标点，构建方向序列
        if (x, y) == end:
            directions_seq = []
            while parent[(x, y)][1] is not None:
                directions_seq.append(parent[(x, y)][1])
                x, y = parent[(x, y)][0]
            directions_seq.reverse()
            return steps, directions_seq

        # 遍历四个方向
        for i in range(4):
            nx, ny = x + directions[i][0], y + directions[i][1]
            if is_valid(nx, ny) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))
                parent[(nx, ny)] = ((x, y), i)

    # 如果没有找到路径
    return -1, []


def find_base(grid, start, aim):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 四个方向：右，下，左，上

    # 检查是否越界
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    # BFS队列
    queue = deque([(start[0], start[1], 0)])  # (x, y, steps)
    visited = set((start[0], start[1]))  # 记录访问过的节点

    while queue:
        x, y, steps = queue.popleft()

        # 如果找到星星，返回步数
        if grid[x][y] == aim:
            return steps, (x, y)

        # 遍历四个方向
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and (nx, ny) not in visited and grid[nx][ny] != '#':
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    # 如果没有找到星星
    return -1, None


def main():
    # 示例地图
    grid = [
        ['.', '.', '.', '.', '.', '.', '*', '.', '.'],
        ['.', '.', '#', '.', '.', '.', '.', '.', '.'],
        ['.', '#', '#', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '*', '.'],
        ['.', '.', '.', '.', '.', '.', '*', '*', '*'],
        ['.', '.', '.', '#', '.', '.', '.', '.', '.']
    ]

    # 起点和终点坐标
    start = (0, 6)
    end = (0, 6)

    # 计算最短路径方向序列
    steps, path = find_path(grid, start, end)
    print("最短路径长度:", steps)
    print("方向序列:", path)


if __name__ == "__main__":
    main()
