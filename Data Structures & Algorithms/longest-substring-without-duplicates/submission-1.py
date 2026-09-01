class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
    
        seen = set()
        max_window = 0
    
        for i in range(len(s)):
            
                while s[i] in seen:
                    seen.remove(s[left])
                    left += 1

                seen.add(s[i])
                length = i - left + 1
                
                if length > max_window:
                    max_window = length

        return max_window          


                






        