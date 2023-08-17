#include <iostream>
#include <vector>
#include <algorithm>
 
using namespace std;
 
int H, W, n;
typedef pair<int, int> stk; // pair<가로, 세로>

bool check_stk(stk s1, stk s2) {
    // 원본
    if (max(s1.second, s2.second) <= H && (s1.first + s2.first) <= W) return true;
    if (max(s1.first, s2.first) <= W && (s1.second + s2.second) <= H) return true;

    // 1번 회전
    if (max(s1.first, s2.second) <= H && (s1.second + s2.first) <= W) return true;
    if (max(s1.second, s2.first) <= W && (s1.first + s2.second) <= H) return true;

    // 2번 회전
    if (max(s1.second, s2.first) <= H && (s1.first + s2.second) <= W) return true;
    if (max(s1.first, s2.second) <= W && (s1.second + s2.first) <= H) return true;

    // 둘 다 회전
    if (max(s1.first, s2.first) <= H && (s1.second + s2.second) <= W) return true;
    if (max(s1.second, s2.second) <= W && (s1.first + s2.first) <= H) return true;

    return false;
}
 
// BOJ 16937 두 스티커
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    cin >> H >> W;
    cin >> n; // 스티커
 
    vector<stk> stv;
 
    int x, y;
    for (int i=0; i<n; i++) {
        cin >> x >> y;
 
        // 스티커가 모눈종이보다 큰 경우
        if (max(x, y) > max(H, W)) continue;
 
        stv.push_back(make_pair(x, y));
    }

    int result = 0;
    for (int i = 0; i < stv.size(); i++) {
        for (int j = i+1; j < stv.size(); j++) {
            if (check_stk(stv[i], stv[j])) {
                int width = stv[i].first*stv[i].second + stv[j].first*stv[j].second;
                result = max(result, width);
            }
        }
    }

    cout << result;
 
    return 0;
}
 