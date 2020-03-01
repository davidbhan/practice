class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        num_unique_chars = len(set(s))
        max_length = 0
        for i in range(len(s)):
            for j in range(i+num_unique_chars, max_length, -1):
                if i+j > len(s):
                    continue
                print(s[i:i+j], j, len(set(s[i:i+j])))
                if len(set(s[i:i+j])) == j: 
                    max_length = j
                    break
                if max_length == num_unique_chars:
                    return max_length
        return max_length

solution = Solution()
print(solution.lengthOfLongestSubstring('aaaaa'))

