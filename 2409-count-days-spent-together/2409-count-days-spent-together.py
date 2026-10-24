from datetime import date

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def compute(s):  # s : date 
            return date(2026, int(s[:2]), int(s[3:]))# retruning the date in format 
        # print(compute(arriveAlice))
        start = max(compute(arriveAlice), compute(arriveBob))  # who come late 
        end = min(compute(leaveAlice), compute(leaveBob)) # who goes early 
        # print(start ,end )
        # (end - start).days   
        return max(0, (end - start).days + 1)