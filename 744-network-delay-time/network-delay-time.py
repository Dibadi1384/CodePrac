import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        # Build adjacency list
        for source, target, time in times:
            graph[source].append((target, time))

        # Min heap stores: total time to reach this node, node
        heap = [(0, k)]
        visited = set()
        max_time = 0

        while heap:
            curr_time, node = heapq.heappop(heap)

            # If we already found the shortest path to this node, skip it
            if node in visited:
                continue

            visited.add(node)
            max_time = curr_time

            # Add all neighbors with updated travel time
            for target, time in graph[node]:
                if target not in visited:
                    heapq.heappush(heap, (curr_time + time, target))

        # If not all nodes were reached
        if len(visited) < n:
            return -1

        return max_time