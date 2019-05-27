import math

from collections import deque

N = 2000000


def can_traverse(towers, radius):
    visited = [False] * len(towers)
    queue = deque([(0, towers[0])])

    while queue:
        num, (x1, y1) = queue.popleft()
        if visited[num]:
            continue

        visited[num] = True

        for i, (x2, y2) in enumerate(towers):
            if i != num:
                dx = abs(x1 - x2)
                dy = abs(y1 - y2)
                dist = dx*dx + dy*dy
                if dist <= radius:
                    queue.append((i, (x2, y2)))

    return all(visited)


def search_radius(coordinates):
    lower = 0
    upper = (N**2) * 2

    while lower < upper:
        mid = (lower + upper) // 2
        if can_traverse(coordinates, mid):
            upper = mid
        else:
            lower = mid + 1

    for radius in sorted([lower, mid, upper]):
        if can_traverse(coordinates, radius):
            return radius


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        coords = [list(map(int, input().split())) for _ in range(n)]

        print('Case #{}: {}'.format(i + 1, search_radius(coords)))


main()
