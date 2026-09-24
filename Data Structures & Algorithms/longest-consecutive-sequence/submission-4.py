class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = set(nums)
        max_length = 0
        for num in length:
            if num - 1 not in length:
               current = num
               currentlength = 1

               while current + 1 in length:
                current += 1
                currentlength += 1


               max_length = max(currentlength, max_length)
        return max_length