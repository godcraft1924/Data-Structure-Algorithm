class Solution {
    List<String> res = new ArrayList<>();
    public List<String> generateParenthesis(int n) {
        StringBuilder s = new StringBuilder();
        solve(n, 0,0,s); 
        return res;

    }
    public void solve(int n ,int open , int close, StringBuilder s  ){
        if (s.length() == 2*n){
             res.add(s.toString());
             return ; 
        }

        //  adding "("
        if (open <n ){
            s.append("(");
            solve(n,open+1 ,close, s );
            s.deleteCharAt(s.length()-1);
        }
        if (close < open){
            s.append(")");
            solve(n, open,close+1,s);
            s.deleteCharAt(s.length()-1); 
        }
    }
}