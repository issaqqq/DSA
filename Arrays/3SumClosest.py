# Brute Force Approch
class BruteForce:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)

        close = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    currentSum = nums[i] + nums[j] + nums[k]

                    if abs(currentSum - target) < abs(close - target):
                        close = currentSum

        return close
    


# Solution
class Closest:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        n = len(nums)
        
        ClosestSum = float('inf')

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i -1]:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                CurrentSum = a + nums[l] + nums[r]

                if abs(CurrentSum - target) < abs(ClosestSum - target):
                    ClosestSum = CurrentSum
                
                if CurrentSum == target:
                    return CurrentSum
                elif CurrentSum < target:
                    l += 1
                else:
                    r -= 1
        
        return ClosestSum 