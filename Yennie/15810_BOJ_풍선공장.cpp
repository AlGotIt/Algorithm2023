#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

typedef pair<long, long> pa;

int N, M;

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> M; // 스탭 수, 풍선 수
    int res = 0;

    priority_queue<pa, vector<pa>, greater<pa>> pq;

    for (int i=0; i<N; i++) {
        long long v;
        cin >> v;
        pq.push(make_pair(v, v)); // 실시간 누적 작업시간 / 스탭별 필요 작업시간
    }

    for (int i=0; i<M-1; i++){
        long long now_time = pq.top().first;
        long long staff_time = pq.top().second;

        pq.pop();
        pq.push(make_pair(now_time + staff_time, staff_time));
    }

    cout << pq.top().first;
    
    return 0;
}