arr = [3, 5, 7, 8, 2]
nums = [32, 4, 88, 64, 111, 100]

# def Squaring(array):
#     return [i ** 2 for i in array]
# print(Squaring(arr))


# def Squaring(array):

#     for i in range(len(array)):
#         arr[i] = arr[i] ** 2
# print(arr)


# def SquaringSorting(arr):
#     print(arr)
#     arr.sort()
#     for i in range(len(arr)):
#         return [x ** 2 for x in arr]
# print(SquaringSorting(arr))




from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = [0] *  n

        left = 0
        right = n - 1
        position = n - 1
        

        while left <= right:
            left_sq = nums[left] ** 2
            right_sq = nums[right] **2 

            if left_sq > right_sq:
                result[position] = left_sq
                left += 1

            else:
                result[position] = right_sq
                right -= 1

            position -= 1
        return result