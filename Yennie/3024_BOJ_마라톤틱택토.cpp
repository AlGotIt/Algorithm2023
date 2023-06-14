#include <iostream>
#include <string>

using namespace std;

int N;
char board[31][31];
int dir[4][2] = {{1, -1}, {1,0}, {1,1}, {0,1}}; //대하좌, 하, 대하우, 우

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> N; 

    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> board[i][j];
        }
    }

    string winner = "ongoing";
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            char ch = board[i][j];
            if (ch == '.') continue; // 빈칸인 경우 탐색 X

            for (int d=0; d<4; d++) {
                int same = 1;
                for (int f=1; f<3; f++) { // 현재 방향으로 2칸 앞까지 확인
                    int ny = i + dir[d][0]*f;
                    int nx = j + dir[d][1]*f;

                    if (ny < 0 || ny >= N || nx < 0 || nx >= N) continue; // 범위를 벗어나는 경우
                    if (ch == board[ny][nx]) same++;
                }
                if (same >= 3){
                    winner = ch;
                    break;
                } 
            }
        }
    }

    cout << winner;

    return 0;
}