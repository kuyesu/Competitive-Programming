# def isValid(s: str) -> bool:
#     stack = []
#     if ch in "({[":
#         stack.append(ch)
#     else:
#         if len(stack) == 0:
#             return False
#         elif ch == ")" and stack.po() != "(":
#             return False
#         elif ch == "}" and stack.pop() != "{":
#             return False
#         elif ch == "[" and stack.pop() != "[":
#             return False

#     if len(stack) == 0:
#         return True

#     else:
#         return False


# def isValid(self, s: str) -> bool:
#     parentheses_mapping = {
#         ")": "(",
#         "}": "{",
#         "]": "[",
#     }

#     if len(s) % 2 != 0:
#         return False

#     stack = []
#     for ch in s:
#         if ch in "({[":
#             stack.append(ch)
#         else:
#             if len(stack) == 0:
#                 return False
#             if stack.pop() != parentheses_mapping[ch]:
#                 return False

#     return len(stack) == 0


def isValid(s: str) -> bool:
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    for ch in s:
        if ch in "({[":
            stack.append(ch)
        else:
            if len(stack) == 0:
                return False
            elif ch == ")" and stack.pop() != "(":
                return False
            elif ch == "}" and stack.pop() != "{":
                return False
            elif ch == "]" and stack.pop() != "[":
                return False

    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    line = input()
    if isValid(line):
        print("valid")
    else:
        print("Invalid")
