class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        depth = 0 
        result = [ 0]*len(seq)
        for i in range(len(seq)):
            if seq[i] == '(': 
                depth += 1 
                if depth%2 == 0 :
                    result[i] = 1 
                else:
                    result[i] = 0
            else: # for closing bracket 
                if depth%2 == 0 :
                    result[i] = 1
                else:
                    result[i] =0 
                depth -= 1 
        return result
                    
