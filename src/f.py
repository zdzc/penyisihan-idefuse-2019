def main():
    t = int(input())
    for i in range(t):
        n = int(input())

        triangle = n - 2
        edges = triangle * 2 + 1
        print('Case #{}: {} triangle(s) with {} edges.'.format(
            i + 1, triangle, edges))


main()
