class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        number1 = 0
        number2 = 0

        power = 1
        while power <= len(num1):
            digit = ord(num1[-power]) - ord("0")
            number1 += digit * (10 ** (power - 1))
            power += 1

        power = 1
        while power <= len(num2):
            digit = ord(num2[-power]) - ord("0")
            number2 += digit * (10 ** (power - 1))
            power += 1

        return str(number1 * number2)