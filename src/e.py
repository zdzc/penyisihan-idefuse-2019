import heapq


def total_running_time(processes, num_processor):
    heap = [0 for i in range(num_processor)]

    for process in processes:
        time = heapq.heappop(heap)
        time += process
        heapq.heappush(heap, time)

    return max(heap)


def main():
    t = int(input())

    for i in range(t):
        _, processor = map(int, input().split())
        processes = list(map(int, input().split()))
        print('Case #{}: {}'.format(
            (i + 1), total_running_time(processes, processor)))


main()
