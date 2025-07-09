from typing import List
from collections import Counter
import random

'''
1st approach:
first we count how many elements {counter} of one kind are in entry array
then using quickselect O(n) we find size(counter) - k element and save its value
We iterate through counter and check which one occurs at least amount of times we found

2nd approach:
Use bucket sort -> We will use it in a way that index will be
count of particular elements, so maximum number of buckets will be n, as an element can
occur maximum n times.
Into buckets we will throw elements that occur that many times
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        res = []

        freq = list(counts.values())
        sep = self.quickselect(freq, 0, len(freq) - 1, len(freq) - k)

        for key, value in counts.items():
            if value >= sep:
                res.append(key)
        
        return res

    def partition(self, arr, low, high):
        pivot_idx = random.randint(low, high)
        arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]
        pivot = arr[low]

        i = low + 1
        j = high
        while True:
            while i <= high and arr[i] < pivot:
                i += 1
            
            while j >= low and arr[j] > pivot:
                j -= 1
            
            if i >= j:
                break

            arr[i], arr[j] = arr[j], arr[i]

            i += 1
            j -= 1

        arr[low], arr[j] = arr[j], arr[low]

        return j

    def quickselect(self, arr, low, high, k):
        if low == high:
            return arr[low]

        new_pivot_idx = self.partition(arr, low, high)
        if k == new_pivot_idx:
            return arr[k]
        elif k < new_pivot_idx:
            return self.quickselect(arr, low, new_pivot_idx - 1, k)
        else:
            return self.quickselect(arr, new_pivot_idx + 1, high, k)

    def topKFrequent2(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        left = k
        for i in range(len(freq) - 1, 0, -1):
            for val in freq[i]:
                res.append(val)
                left -= 1
                if left == 0:
                    return res


sol = Solution()
print(sol.topKFrequent([1,2,2,3,3,3], 2))
