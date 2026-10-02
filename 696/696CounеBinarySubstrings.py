class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        curr = 1
        prev = 0
        answer = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                answer += min(prev, curr)
                prev = curr
                curr = 1
        answer += min(prev, curr)
        return answer
