class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        copy = strs.copy()
        for i in range(len(strs)):
            strs[i] = "".join(sorted(strs[i]))
        dict = {}
        for i in range(len(strs)):
            if strs[i] in dict: 
                dict[strs[i]].append(i)
            else:
                dict[strs[i]] = [i]
        result = []
        for i in dict: 
            a = []
            for j in dict[i] :
                a.append(copy[j])
            result.append(a)
        return result