class Solution:
    def myAtoi(self, s: str) -> int:
        value, state, position, sign = 0, 0, 0, 1
        maxii = 2 ** 31 - 1  # 2147483647
        minii = -(2 ** 31)  # -2147483648

        if not s:
            return 0

        while position < len(s):
            current_char = s[position]
            if state == 0:
                if current_char == ' ':
                    pass
                elif current_char in ['+', '-']:
                    state = 1
                    sign = 1 if current_char == '+' else -1
                elif current_char.isdigit():
                    state = 2
                    value = 10 * value + int(current_char)
                else:
                    return 0
            elif state == 1:
                if current_char.isdigit():
                    state = 2
                    value = 10 * value + int(current_char)
                else:
                    return 0
            elif state == 2:
                if current_char.isdigit():
                    state = 2
                    value = 10 * value + int(current_char)
                else:
                    break
            else:
                break
            position += 1
        value = value * sign
        value = min(value, maxii)
        value = max(minii, value)
        return value


a = Solution()
# print(a.myAtoi("   -42"))
# print(a.myAtoi("4193 with words"))
print(a.myAtoi("words and 987"))
