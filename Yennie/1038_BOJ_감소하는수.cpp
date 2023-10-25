#include <iostream>
#include <vector>
#include <set> 
#include <sstream>
#include <algorithm>

using namespace std;
 
int N;
vector<int> nums = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
set<long long> decrease_nums; // 감소하는 수의 집합

// 백트래킹을 이용하여 감소하는 수 찾기
void generate_combination(vector<int>& current, int index) {
    if (index == nums.size()) {
        vector<int> sorted_nums = current;
        sort(sorted_nums.begin(), sorted_nums.end(), [](int a, int b) {
            return to_string(a) > to_string(b);
        });

        string num = "";
        for (int c : sorted_nums) {
            num += to_string(c);
        }

        long long input;
        istringstream(num) >> input;
        decrease_nums.insert(input);
        return;
    }
 
    // 현재 원소를 선택하지 않고 다음 원소로 이동
    generate_combination(current, index + 1);
 
    // 현재 원소를 선택하고 다음 원소로 이동
    current.push_back(nums[index]);
    generate_combination(current, index + 1);
 
    // 백트래킹을 위해 선택한 원소 제거
    current.pop_back();
}
 
int main() {
    vector<int> current;
    long long result = -1;

    cin >> N;
 
    generate_combination(current, 0);

    if (N < decrease_nums.size()) {
        auto it = decrease_nums.begin();
        advance(it, N);

        result = *it;
    }
    
    cout << result << endl;
 
    return 0;
}
 