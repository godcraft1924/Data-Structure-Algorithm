class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3 :
            return False
        word = word.lower()
        vowel = None
        consonant  = None 
        digit = None
        for  i in word :
            if i.isalpha():
                if i in ['a','e','i','o','u']:
                    vowel = True 
                elif i not in  ['a','e','i','o','u']:
                    consonant = True
            elif i.isdigit():
                pass
            else: 
                return False
        if vowel and consonant : 
            return True 
        else:
            return False
                

        