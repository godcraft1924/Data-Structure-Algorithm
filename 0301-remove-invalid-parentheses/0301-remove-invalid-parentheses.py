class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        # Find minimum number of '(' and ')' to remove
        left_remove = 0
        right_remove = 0

        for ch in s:
            if ch == '(':
                left_remove += 1

            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        result = set()

        def solve(i, current, balance, left_remove, right_remove):

            # Invalid
            if balance < 0:
                return

            # End
            if i == len(s):
                if balance == 0 and left_remove == 0 and right_remove == 0:
                    result.add(current)
                return

            ch = s[i]

            # Remove '('
            if ch == '(' and left_remove > 0:
                solve(
                    i + 1,
                    current,
                    balance,
                    left_remove - 1,
                    right_remove
                )

            # Remove ')'
            if ch == ')' and right_remove > 0:
                solve(
                    i + 1,
                    current,
                    balance,
                    left_remove,
                    right_remove - 1
                )

            # Keep character
            if ch == '(':
                solve(
                    i + 1,
                    current + ch,
                    balance + 1,
                    left_remove,
                    right_remove
                )

            elif ch == ')':
                if balance > 0:
                    solve(
                        i + 1,
                        current + ch,
                        balance - 1,
                        left_remove,
                        right_remove
                    )

            else:
                solve(
                    i + 1,
                    current + ch,
                    balance,
                    left_remove,
                    right_remove
                )

        solve(0, "", 0, left_remove, right_remove)

        return list(result)