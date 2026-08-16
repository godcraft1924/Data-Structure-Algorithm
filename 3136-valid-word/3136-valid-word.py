class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowel = False
        consonant = False

        for ch in word:
            if not ch.isalnum():
                return False

            if ch in "aeiouAEIOU":
                vowel = True
            elif ch.isalpha():
                consonant = True

        return vowel and consonant

        # this is version was copied by chatgpt i have solve it but has less conditons 