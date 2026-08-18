class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        answer= []
        for k in range(len(nums)-2):
            if k> 0 and nums[k] == nums[k-1]:
                continue
            second = len(nums)-1
            first = k+1
            while first<second: 
                sum = nums[k]+ nums[first]+nums[second]
                if  sum == 0 :
                    answer.append([nums[k],nums[first],nums[second]])
                    first += 1
                    second -= 1
                    while first < second and nums[first] == nums[first - 1]:
                        first += 1

                    while first < second and nums[second] == nums[second + 1]:
                        second -= 1
                elif sum > 0:
                    second = second -1 
                else: 
                    first  = first + 1 

        return answer



        