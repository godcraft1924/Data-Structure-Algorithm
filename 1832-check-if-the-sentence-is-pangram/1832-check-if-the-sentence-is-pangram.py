class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        check = 0 
        for i in sentence:
            if check & 1<<(ord(i)-ord("a")) == 0 :
                check |= 1<<(ord(i)-ord("a")) 
        # print(check)
        return check == (1 << 26) - 1

        