class Solution():
    def twoSum(self, nums, target):
        dicc = {}
        for index in range(len(nums)):
            if nums[index] in dicc:
                print(dicc)
                return [dicc[nums[index]], index]
            dicc[target - nums[index]] = index
                    