#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric>

using namespace std;

vector<int> height;
vector<int> dist;

int main()
{
    int N, K, res=0;

    cin >> N >> K;

    int input = 0;
    for (int i=0; i<N; i++) {
        cin >> input;
        if (i > 0) dist.push_back(input - height.back());

        height.push_back(input);
    }

    sort(dist.begin(), dist.end());

    for (int i=0; i<K-1; i++) {
        dist.pop_back();
    }

    res = accumulate(dist.begin(), dist.end(), 0);
    cout << res;

    return 0;
}