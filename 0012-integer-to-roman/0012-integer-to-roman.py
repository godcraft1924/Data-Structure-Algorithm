class Solution:
    def intToRoman(self, num: int) -> str:
        key = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        power = 0 
        roman = ""
        while num> 0 :
            negative = False
            digit = num % 10 
            # print(digit)
            real_d  = digit*10**power
            if real_d in key :
                roman =  key[real_d] + roman
                power = power +1
                num = num// 10
                continue
            elif  digit == 9 : # for 9 and it like 
                roman = key[10**power] + key[10**(power+1)] +roman
                power = power +1
                num = num// 10
                continue
                
            minus = digit*10**power - 5*10**power
            if minus>0 :
                negative =  True 
            if  abs(minus) == 10**power: # for 4,6,40,60,400,600
                if negative:
                    roman = key[5*10**power] + key[10**power] + roman
                else:
                    roman = key[10**power] + key[5*10**power] +roman
            else:   # for 2,3,7,8
                if not  negative:          # digit < 5
                    roman = digit * key[10**power] + roman
                else:         
                    print(digit-5)# digit > 5
                    roman = key[5*10**power] + (digit-5) * key[10**power] + roman
                        
            power = power +1
            num = num// 10
        return roman
