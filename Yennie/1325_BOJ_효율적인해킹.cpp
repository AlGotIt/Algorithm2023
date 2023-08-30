#include <iostream>
#include <vector>
#include <algorithm> // fill 사용

using namespace std;

int N, M;
// int graph[10001][10001]; // 메모리 초과 발생 ㅠㅠ
vector<vector<int>> graph; // 인접 리스트 사용
int visited[10001]; // 방문한 컴터인지 체크

int dfs(int n, int com_num)
{
    for (int c : graph[n]) {
        if (!visited[c]) {
            visited[c] = 1;
            com_num = dfs(c, ++com_num);
        }
    }

    return com_num;
}

int main()
{
    cin >> N >> M;
    graph.resize(N+1);

    int from, to;
    for (int i=0; i<M; i++) {
        cin >> to >> from;
        graph[from].push_back(to);
    }

    int max_pc = 0; // 해킹 가능 최대 컴퓨터 수
    vector<int> res_com; // 컴터 번호 저장
    for (int i=1; i<=N; i++) {
        visited[i] = 1;
        int possible_com = dfs(i, 0);

        if (possible_com >= max_pc) {
            if (possible_com > max_pc) {
                max_pc = possible_com;
                res_com.clear();
            }
            res_com.push_back(i);
        } 
        fill(visited, visited+N+1, 0);  // visited 0으로 초기화
    }

    sort(res_com.begin(), res_com.end()); // 오름차순 정렬

    for (int v : res_com) {
        cout << v << " ";
    }

    return 0;
}