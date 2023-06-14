#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;

int N; // 도시 개수
ll dist[100002]; // 거리
ll cost[100002]; // 비용

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;

    for (int i=0; i<N-1; i++) {
        cin >> dist[i];
    }
    for (int i=0; i<N; i++) {
        cin >> cost[i];
    }

    ll result = 0;
    ll min_cost = cost[0]; // 주유 최소 비용

    for (int i=0; i<N-1; i++){
        if (min_cost >= cost[i]) { // 도착한 마을의 주유 비용이 더 저렴한 경우
            min_cost = cost[i];
        }

        result += min_cost * dist[i];
    }

    cout << result;

    return 0;
}