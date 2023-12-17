class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchingOpenings = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for character in s:
            if character in matchingOpenings:
                if stack and stack[-1] == matchingOpenings[character]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character)
        return True if not stack else False