class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        for i in range(len(tasks)):
            tasks[i].append(i)

        tasks.sort(key=lambda x: x[0])
        available = []
        res = []
        i = 0
        time = tasks[0][0]

        # Continue while unadded or available tasks remain
        while i < len(tasks) or available:

            # Add all tasks that have arrived
            while i < len(tasks) and tasks[i][0] <= time:

                # Add (processing time, original index) to the heap
                heapq.heappush(available, (tasks[i][1], tasks[i][2]))

                # Move to the next unadded task
                i += 1

            # Check whether there is an available task
            if available:

                # Remove the task with the shortest processing time
                processing_time, index = heapq.heappop(available)

                # Add its original index to the result
                res.append(index)

                # Move time forward by its processing time
                time += processing_time

            else:
                # Jump to the next task's enqueue time
                time = tasks[i][0]

        # Return the task processing order
        return res