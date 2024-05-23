from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
        Finds two numbers in a List which sum up to the target number
        """
        index_list = {}
        for number, index in enumerate(nums):
            solution_num = target - number
            if solution_num in index_list[number]:
                return [index, index_list[solution_num]]
            index_list[number] = index
        return []


ans = Solution
print(ans.twoSum([2, 7, 11, 15], 9))
