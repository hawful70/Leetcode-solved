from typing import Collection, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      counter = Collection.defaultdict(int)
      
      for num in nums:
        counter[num] += 1
      
      sorted_Frequent = sorted(counter.items(), key=lambda x:x[1], reverse=True)
      
      return [sorted_Frequent[i][0] for i in range(k)]