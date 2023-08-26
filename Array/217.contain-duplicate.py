class Solution(object):
    def containsDuplicate(self, nums):
        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        for num in frequency:
            if frequency[num] >= 2:
                return True
        return False