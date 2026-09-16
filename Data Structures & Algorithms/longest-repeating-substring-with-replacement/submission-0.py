class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        right = 0
        left = 0
        ans = 0
        max_freq = 0
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right],0) + 1

            window_length = right - left + 1
            max_freq = max(max_freq,freq[s[right]])
            replacement = window_length - max_freq

            if replacement > k:
                freq[s[left]] -= 1
                left += 1
            ans = max(ans,right - left + 1)    
        return ans