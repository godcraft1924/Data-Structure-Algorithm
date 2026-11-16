class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) >  k :
            tmp  = [ ]
            length = len(s)
            for i in range(0,length,k):
                val = 0 
                for  j in range(i,min(i+k,length)):
                    val += int(s[j])
                tmp.append(str(val))
            s = "".join(tmp)
        return s

            
        