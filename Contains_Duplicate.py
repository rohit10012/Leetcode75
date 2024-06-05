class Solution:
    def containDuplicate(nums) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False
    
nums = [1,2,3,5]
print(Solution.containDuplicate(nums))
