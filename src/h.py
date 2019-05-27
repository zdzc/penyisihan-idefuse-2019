import math


def min_move(x, y, radius, coords):
    move = 0
    for cx, cy in coords:
        dx = abs(cx - x)
        dy = abs(cy - y)
        result = math.sqrt(dx*dx + dy*dy) - radius
        move += math.ceil(max(0, result))
    return move


def main():
    t = int(input())

    for i in range(t):
        x, y, radius = map(int, input().split())
        n = int(input())
        coords = [list(map(int, input().split())) for _ in range(n)]

        print('Case #{}: {}'.format(i + 1, min_move(x, y, radius, coords)))


main()
