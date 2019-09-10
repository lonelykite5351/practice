#Two Sum 給目標，找出兩數字和的位置
# =============================================================================
# class Solution(object):
#     def twoSum(nums,target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for idx1,n1 in enumerate(nums):
#             for idx2,n2 in enumerate(nums):
#                 if idx1 != idx2:
#                     sum = n1 + n2
#                     if sum == target:
#                         return(idx1,idx2)
#                     else:
#                         sum = 0
#                 else:
#                     continue
# 
# 
#     a = [2, 7, 11, 15]
#     target=10                    
#     print(twoSum(a,target))
# =============================================================================

class Solution(object):
    def twoSum(nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        h_nums = {}
        for i in range(len(nums)):
            if nums[i] in h_nums:
                return(h_nums[nums[i]],i)
            else:
                h_nums[target - nums[i]] = i
        
    a = [2, 7, 11, 15]
    target=18                    
    print(twoSum(a,target))   
        
        