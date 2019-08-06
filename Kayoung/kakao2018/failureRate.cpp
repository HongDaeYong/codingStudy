#include <string>
#include <vector>
#include <queue>

using namespace std;

struct failureRate {
    double rate;
    int stage;
};

bool operator<(failureRate a, failureRate b){
    if(a.rate == b.rate){
        return a.stage > b.stage;
    }
    return a.rate < b.rate;
}

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    priority_queue<failureRate> fr;
    vector<int> challengerCnt(N+2);
    vector<int> sucessCnt(N+1);
    
    for(int i=0; i<stages.size(); i++) {
        for(int j=1; j<stages[i]; j++) {
            challengerCnt[j]++;
            sucessCnt[j]++;
        }
        challengerCnt[stages[i]]++;
    }
    
    for(int i=1; i<=N; i++) {
        failureRate f;
        if(challengerCnt[i] == 0) {
            f.rate = 0;
        }
        else {
            f.rate = (challengerCnt[i] - sucessCnt[i]) / (double)challengerCnt[i];
        }
        f.stage = i;
        fr.push(f);
    }
    
    while(!fr.empty()) {
        answer.push_back(fr.top().stage);
        fr.pop();
    }
    return answer;
}