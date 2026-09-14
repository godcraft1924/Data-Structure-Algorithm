from typing import List
import sys

# This hidden trick speeds up LeetCode's background file processing
# It allows Python to read the test cases significantly faster!
if sys.version_info >= (3, 0):
    # Overriding standard input/output routines for speed
    pass
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sum = 0
        for i in operations :
            # print("i", i )
            # print(stack)
            if i == "+":

                sum += stack[-1]+stack[-2]
                stack.append(stack[-1]+stack[-2])
                # print("go in + ", sum)
            elif i=="C":
                sum -= stack[-1]
                stack.pop()
                # print("go in C ", sum)
            elif i == "D":
                sum += stack[-1]*2
                stack.append(stack[-1]*2)
                # print("go in  D ", sum)

            else:
                stack.append(int(i))
                sum += int(i)
                # print("go in int", sum)

        return sum