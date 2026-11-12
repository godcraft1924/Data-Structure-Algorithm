class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()
        def solve(i,path :list,sum):
            if i >= len(candidates):
                return 
            if sum == target :
                print(sum,target)
                result.append(path.copy())
                return 
            if target-sum < 2 :
                solve(i+1,path,sum)
                return 
            sum += candidates[i]
            path.append(candidates[i])
            solve(i,path, sum)
            path.pop()
            sum -= candidates[i] 
            solve(i+1,path, sum)

        solve(0,[],0)
        return (result)