#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
 
using namespace std;
 
int N, M;
set<vector<int>> unique_row; // 부분 수열을 저장할 집합
 
// 백트래킹을 이용하여 부분 수열 생성
void generateSubsequences(vector<int>& sequence, vector<int>& current, int index) {
    if (index == sequence.size()){
        if (current.size() == M) {
            vector<int> temp;
            for (int num : current) {
                temp.push_back(num);
            }

            sort(temp.begin(), temp.end()); // 오름차순 정렬
            unique_row.insert(temp);
        }
        return;
    }
 
    // 현재 원소를 선택하지 않고 다음 원소로 이동
    generateSubsequences(sequence, current, index + 1);
 
    // 현재 원소를 선택하고 다음 원소로 이동
    current.push_back(sequence[index]);
    generateSubsequences(sequence, current, index + 1);
 
    // 백트래킹을 위해 선택한 원소 제거
    current.pop_back();
}
 
int main() {
    vector<int> sequence;
    vector<int> current;
 
    cin >> N >> M;
 
    int num;
    for (int i=0; i<N; i++) {
        cin >> num;
        sequence.push_back(num);
    }
 
    generateSubsequences(sequence, current, 0);
 
    for (const auto& row : unique_row) {
        for (int v : row) {
            cout << v << " ";
        }
        cout << endl;
    }
 
    return 0;
}