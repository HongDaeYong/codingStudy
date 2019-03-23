import java.util.PriorityQueue;
import java.util.Collections;

class Solution {
    public int solution(int stock, int[] dates, int[] supplies, int k) {
        int answer = 0;
        PriorityQueue<Integer> pq= new PriorityQueue<Integer>(Collections.reverseOrder());
        int n = 0;
        int l = dates.length-1;

        for(int i =0 ; i < k ; i++){
            if(dates[n] == i){
                pq.add(supplies[n]);
                if (n <l)
                    n++;
            }
            if (stock==0){
                stock += pq.remove();
                answer++;
            }
            stock--;
        }
        return answer;
    }
}
