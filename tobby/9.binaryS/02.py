def solution(n, times):
    answer = 0;
    times.sort();
    start = 0;
    end = n * times[len(times) - 1];
    
    while start <= end :
        mid = int((end + start) / 2);
        s = sum(int(mid / t) for t in times)
        
        if s >= n : 
            end = mid -1;
            answer = mid;
        else :
            start = mid +1;

    return answer;