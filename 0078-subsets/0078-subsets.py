class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        path= []
        def solve(i,result:list):
            if i== len(nums) :
                path.append(result.copy()) 
                return
            #  add 
            result.append(nums[i])
            solve(i+1,result)
            result.pop()
            #  skip 
            solve(i+1,result)
        solve(0,[])
        return path