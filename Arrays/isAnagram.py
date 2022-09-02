class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        _len = len(s)
        _len2 = len(t)
        if _len != _len2:
            return False
        _list = [0 for i in range(26)]
        _list2 = [0 for i in range(26)]
        for i in range(_len):
            _list[ord(s[i])-ord('a')] += 1
            _list2[ord(t[i])-ord('a')] += 1
        return tuple(_list) == tuple(_list2)
