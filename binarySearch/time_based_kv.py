from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        result = ''
        values = self.hash_map[key]
        l = 0
        r = len(values) - 1

        while l <= r:
            mid = (l + r) // 2
            curr_ts, val = values[mid]

            if curr_ts <= timestamp:
                result = val
                l = mid + 1
            else:
                r = mid - 1
        
        return result
        
