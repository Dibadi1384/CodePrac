from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)

        highest_frequency = max(counts.values())
        number_of_highest = sum(
            count == highest_frequency for count in counts.values()
        )

        minimum_time = (
            (highest_frequency - 1) * (n + 1)
            + number_of_highest
        )

        return max(len(tasks), minimum_time)





