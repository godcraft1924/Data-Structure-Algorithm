import java.util.*; 
class Solution {
    public boolean isValid(String s) {
        int n = s.length();
        Stack<Character> stack = new Stack<>();
        HashMap<Character,Character> Hp = new HashMap<>();
        Hp.put('(',')');
        Hp.put('[',']');
        Hp.put('{','}');
        for(int i = 0 ; i<n ; i++){
            if (Hp.containsKey(s.charAt(i))){
                stack.push(s.charAt(i));
            }else {
                if(!stack.isEmpty()){
                    if (Hp.get(stack.peek()) == s.charAt(i)){
                        stack.pop();
                    }else{
                        return false; 
                    }
                }else {
                    return false; 
                }
            }
        }

        if(stack.size() !=0){
            return false; 
        }
        return  true ;
    }
}