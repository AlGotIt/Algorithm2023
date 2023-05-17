#include <iostream>
#include <algorithm>

using namespace std;

int N;
long long M;
long long trees[1000001];

bool isPossible(unsigned int height) {
	unsigned int taken = 0;
	for (int i = 0; i < N; i++) {
		if (trees[i] >= height)
			taken += (trees[i] - height);
		if (taken >= M) return true;
	}
	return false;
}

int main() {
	cin >> N >> M;
	for (int i = 0; i < N; i++)
		cin >> trees[i];

	unsigned int left = 0;
    unsigned int right = *max_element(trees, trees + N);
	unsigned int mid, answer;

	while (left <= right) {
		mid = (left + right) / 2;
		if (isPossible(mid)) {
			answer = mid;
			left = mid + 1;
		}
		else {
			right = mid - 1;
		}
	}

    cout << answer;
}