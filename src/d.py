def count_stones(stones):
    iterator = zip(stones, stones[1:])
    count = 0
    try:
        while True:
            a, b = next(iterator)
            if a == b == '0':
                count += 1
                next(iterator)
    except StopIteration:
        return count


def main():
    n = int(input())

    for i in range(n):
        input()
        stones = list(input())
        print('Case #{}: {}'.format(i + 1, count_stones(stones)))


main()
