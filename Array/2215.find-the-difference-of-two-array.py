from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        def checkExisting(frequency1, frequency2):
            ans = []
            for element in frequency1:
                if element not in frequency2:
                    ans.append(element)

            return ans

        ans, frequency_nums1, frequency_nums2 = [], {}, {}

        for i in range(len(nums1)):
            if nums1[i] not in frequency_nums1:
               frequency_nums1[nums1[i]] = 1
        for i in range(len(nums2)):
            if nums2[i] not in frequency_nums2:
               frequency_nums2[nums2[i]] = 1

        ans.append(checkExisting(frequency_nums1, frequency_nums2))
        ans.append(checkExisting(frequency_nums2, frequency_nums1))

        return ans
solution = Solution()
print(solution.findDifference([1,2,3,3], [1,1,2,2]))

        
            

