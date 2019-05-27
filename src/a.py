n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    to_score = max(0, 100 - a - b)
    print('Case #{}: {}'.format(i + 1, to_score))
