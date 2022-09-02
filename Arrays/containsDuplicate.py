class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        _dict = set()
        for i, num in enumerate(nums):
            if num in _dict:
                return True
            _dict.add(num)
        return False
