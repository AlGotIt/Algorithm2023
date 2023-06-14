#include <iostream>
#include <algorithm>

using namespace std;

int A[200001];
int dp[200001];

int main()
{
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    
    int N;
    cin >> N;

    int min_plus_num = 1000000000;
    for(int i=1; i<=N; i++){
        cin >> A[i];
        
        if (A[i] < min_plus_num) {
            min_plus_num = A[i];
        }
        
        dp[i] = max(A[i] - min_plus_num, dp[i-1]);
        cout << dp[i] << " ";
    }
    
    return 0;
}
