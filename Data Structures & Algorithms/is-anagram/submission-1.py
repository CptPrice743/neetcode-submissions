class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dict_s = {}
        
        if len(s) != len(t):
            return False

        for letter in s:
            dict_s[letter] = dict_s.get(letter, 0) + 1

        for letter in t:
            if letter not in dict_s or dict_s[letter] == 0:
                return False
            else: 
                dict_s[letter] = dict_s.get(letter, 0) - 1
        return True
            