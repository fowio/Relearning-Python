
class Solution:
    def twoSum(self, nums, target):
        map = {}
        for index, number in enumerate(nums):
            difference = target - number
            if difference in map:
                return map[difference], index
            else:
                map[number] = index
            
nums = [2, 7, 11, 15]
target = 9
solution = Solution()                    # no data here — Solution has no __init__
print(solution.twoSum(nums, target)) 