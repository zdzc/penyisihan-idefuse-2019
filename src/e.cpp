#include <algorithm>
#include <iostream>
#include <utility>
#include <queue>
#include <vector>

int total_running_time(std::vector<int> &processes, int num_processor)
{
    std::priority_queue<int, std::vector<int>, std::greater<int> > heap;
    for (int i = 0; i < num_processor; ++i)
    {
        heap.push(0);
    }

    for (auto &p : processes)
    {
        auto time = heap.top();
        heap.pop();
        heap.push(time + p);
    }

    int last;
    while (!heap.empty())
    {
        last = heap.top();
        heap.pop();
    }
    return last;
}

int main()
{
    int t;
    std::cin >> t;

    for (int i = 1; i <= t; ++i)
    {
        int num_process, num_processor;
        std::cin >> num_process >> num_processor;

        std::vector<int> v;
        v.assign(num_process, 0);
        for (int j = 0; j < num_process; ++j)
        {
            std::cin >> v[j];
        }

        std::cout << "Case #" << i << ": " << total_running_time(v, num_processor) << '\n';
    }
}
