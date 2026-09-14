class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        # max heap using negative frequencies
        heap = []
        for char, freq in count.items():
            heapq.heappush(heap, (-freq, char))

        res = ""

        # character we used last cannot immediately be reused
        prev_freq = 0
        prev_char = ""

        while heap:
            freq, char = heapq.heappop(heap)

            # use this character
            res += char
            freq += 1   # -3 -> -2, because one was used

            # now the previous character is allowed back in
            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_char))

            # current character must wait one turn
            prev_freq = freq
            prev_char = char

        # if a character is still left over, impossible
        if prev_freq < 0:
            return ""

        return res