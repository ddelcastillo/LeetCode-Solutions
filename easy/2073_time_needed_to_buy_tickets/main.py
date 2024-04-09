class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        n, time, skipped_positions = len(tickets), 0, set()
        while tickets[k] != 0:
            for i in range(n):
                if i in skipped_positions:
                    continue
                if i == k and tickets[i] == 1:
                    return time + 1
                elif tickets[i] != 0:
                    time += 1
                    tickets[i] -= 1
                else:
                    skipped_positions.add(i)
        return time
