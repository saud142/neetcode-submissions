class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        need = {}    
        for c in s1:
            need[c] = need.get(c, 0) + 1
        window = {}    
        k = len(s1)
        for i in range(k): 
            c = s2[i]
            window[c] = window.get(c, 0) + 1

        if window == need:
            return True

        for right in range(k, len(s2)):
            c = s2[right]
            window[c] = window.get(c, 0) + 1

            left_char = s2[right - k]
            window[left_char] -= 1

            if window[left_char] == 0:
                del window[left_char]

            if window == need:
                return True

        return False
