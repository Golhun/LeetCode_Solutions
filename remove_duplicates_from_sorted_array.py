class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Rearranges a sorted list and removes duplicates
        """
        if not nums:
            return o
        
        write_index = 1
        for i in range(write_index, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[write_index] = nums[i]
                write_index += 1
        return write_index



