def solution(nums):
    nhalf = len(nums) // 2
    nunique = len(set(nums))
    
    return min(nunique, nhalf)