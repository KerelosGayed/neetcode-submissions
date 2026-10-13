class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_dict = {'}': '{', ')': '(', ']': '['}
        if s[0] in valid_dict:
            return False
        for i in range(len(s)):
            if s[i] in valid_dict:
                if stack:
                    if stack.pop() != valid_dict.get(s[i]):
                        return False
                else:
                    return False
            else:
                stack.append(s[i])
        if stack:
            return False
        return True