class BruteForce:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)

        close = nums[0] + nums[1] + nums[2]

        for i in range(n):
            for j in range(n-1):
                for k in range(n-2):
                    currentSum = nums[i] + nums[j] + nums[k]

                    if abs(currentSum - target) < abs(close - target):
                        close = currentSum


        return close