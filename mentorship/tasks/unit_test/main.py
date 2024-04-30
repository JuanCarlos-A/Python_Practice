class Solution():
    def twoSum(self, nums, target):
        dicc = {}
        for index in range(len(nums)):
            if nums[index] in dicc:
                print(dicc)
                return [dicc[nums[index]], index]
            dicc[target - nums[index]] = index
                    
# print(Solution().twoSum([-1,-2,-3,-4,-5], -8))


# def twoSum(self, nums, target):
#         for item in nums:
#             num = nums.index(item)
#             for i in range(num+1, len(nums)):
#                 if item + nums[i] == target and num != i:
#                     return [num, i]