#include <iostream>
#include <string>

using namespace std;

int N, M;
int level_num[100001];
string level_name[100001];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    
    cin >> N >> M;

    for (int i=0; i<N; i++){
        cin >> level_name[i] >> level_num[i];
    }
    
    for (int i=0; i<M; i++){
        long lv;
        cin >> lv;

        int left = 0;
        int right = N;
        int mid;

        while (left <= right) {
            mid = (left + right) / 2;
            if (level_num[mid] < lv) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }
        if (lv > level_num[mid]) {
            cout << level_name[mid+1] << "\n";
        } else {
            cout << level_name[mid] << "\n";
        }
    }

    return 0;
}