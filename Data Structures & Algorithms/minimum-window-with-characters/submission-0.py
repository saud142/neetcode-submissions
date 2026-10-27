class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        left = 0
        start = 0    
        min_len = float("inf")
        formed = 0
        need = {}
        window = {}
        for ch in t:
            need[ch] = need.get(ch,0) + 1
        required = len(need)    
        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch,0) + 1
            if ch in need and window[ch] == need[ch]:
                formed +=1  

            while formed == required:
                length = right - left + 1
                if min_len > length:
                    min_len = length
                    start = left
                left_ch = s[left]
                window[left_ch] -= 1
                if (left_ch in need and window[left_ch] < need[left_ch]):
                    formed -= 1
                left +=1
        if min_len == float('inf'):
            return ""  
        result = ""    
        for i in range(start,start + min_len):
            result += s[i]    
        return result    

