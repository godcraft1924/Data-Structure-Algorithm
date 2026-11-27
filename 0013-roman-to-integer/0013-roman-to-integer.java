import java.util.*;
class Solution {
    public int romanToInt(String s) {
        int n = s.length();
        HashMap<Character, Integer> dict = new HashMap<>();
        dict.put('I',1);
        dict.put('V',5);
        dict.put('X',10);
        dict.put('L',50);
        dict.put('C',100);
        dict.put('D',500);
        dict.put('M',1000);
        int total = 0 ; 
        for (int i = 0 ; i<n ;i++ ){
            System.out.print(dict.get(s.charAt(i)));
            if (i+1 < n && (dict.get(s.charAt(i)) <  dict.get(s.charAt(i+1)))){
                total -= dict.get(s.charAt(i));
            }else {

                total +=  dict.get(s.charAt(i));
            }
        }

        return total;
    }
    
}