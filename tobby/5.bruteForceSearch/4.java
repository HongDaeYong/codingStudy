class Solution {
    public int[] solution(int brown, int red) {
        int l = brown/2 + 2;
        
        int a = (l+1)/2;
        int b = l - a;
        
        while(a != l){ 
            if((a-2)*(b-2)==red){
                if(brown==(a*b-red)){
                    return new int [] { a, b};
                }
            } 
            a++;
            b--;
        }
        
        return new int [] { 0, 0};
    }
}
