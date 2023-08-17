#include <iostream>
#include <vector>
 
using namespace std;
 
int N, S, result;
 
// 백트래킹을 이용하여 부분 수열 생성
void generateSubsequences(vector<int>& sequence, vector<int>& current, int index) {
    if (index == sequence.size()) {
        // 현재 부분 수열 출력
        int sum = 0;
        for (int num : current) {
            //cout << num << " ";
            sum += num;
        }
        //cout << "\t res: " << sum;
        //cout << endl;
        if (current.size() != 0 && sum == S) result++;
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
 
    cin >> N >> S;
 
    int num;
    for (int i=0; i<N; i++) {
        cin >> num;
        sequence.push_back(num);
    }
 
    //cout << "부분 수열:" << endl;
    generateSubsequences(sequence, current, 0);
    cout << result << endl;
 
    return 0;
}
 