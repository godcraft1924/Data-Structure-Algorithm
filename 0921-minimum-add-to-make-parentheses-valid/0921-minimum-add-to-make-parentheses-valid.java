class Solution {
    public int minAddToMakeValid(String s) {
        int n = s.length();
        int total = 0 ; 
        int count = 0 ; 
        for (int i =0 ; i< n ;i++){
            if (s.charAt(i) =='('){
                count++;
            }else{
                count--; 
                if (count< 0 ){
                    count = 0 ;
                    total++;
                }

            }
        }
        return total+count;
        
    }
}