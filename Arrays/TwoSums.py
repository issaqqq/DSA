# only for sorted arrays:
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         i = 0
#         j = len(nums) - 1
#         while (i<j):
#             CurrentSum = nums[i] + nums[j]

#             if(CurrentSum == target):
#                 return [i,j]
#             elif(CurrentSum < target):
#                 i += 1
#             else:
#                 j -= 1
#         return []
    

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            need = target - num

            if need in seen:
                return [seen[need], i]

            seen[num] = i

        return []