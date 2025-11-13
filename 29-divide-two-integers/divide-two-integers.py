class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)

        while abs_dividend >= abs_divisor:
            temp = abs_divisor
            multiple = 1
            while abs_dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            abs_dividend -= temp
            result += multiple

        if (dividend > 0) ^ (divisor > 0):
            result = -result

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        return max(INT_MIN, min(INT_MAX, result))
