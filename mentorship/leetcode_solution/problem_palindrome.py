#Solution 1
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         num_origin = x
#         num_invert = 0

#         while x > 0:
#             num = x % 10

#             num_invert = (num_invert * 10) + num
#             x //= 10
        
#         return num_origin == num_invert


#Solution 2
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)
    
print(Solution().isPalindrome(121))