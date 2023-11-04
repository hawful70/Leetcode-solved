from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = set()
        ans = []
        for i in range(len(nums1)):
            dic.add(nums1[i])
        
        for i in range(len(nums2)):
            if nums2[i] in dic:
                ans.append(nums2[i])
                dic.remove(nums2[i])

        return ans