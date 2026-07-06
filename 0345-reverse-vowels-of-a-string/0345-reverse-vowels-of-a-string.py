class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel  = [ ]
        for i in s :
            if i in ["A","E","O","U","I","a","e","i","u","o"]:
                vowel.append(i)
        new = list(s)
        for  i  in range(len(new)):
            if new[i] in ["A","E","O","U","I","a","e","i","u","o"]:
                popped = vowel.pop()
                new[i] = popped
        return( "".join(new))        
        