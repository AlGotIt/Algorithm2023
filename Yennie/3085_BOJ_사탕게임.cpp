#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int N;
char candy_board[51][51];

int return_max_candy(int dir) // 방향(행/열)
{
    int max_num, res = 0;
    char now_candy;

    for (int i=0; i<N; i++){
        now_candy = dir ? candy_board[i][0] : candy_board[0][i];
        max_num = 1;
        for (int j=1; j<N; j++){
            if (now_candy == (dir ? candy_board[i][j] : candy_board[j][i])) {
                max_num++;
            } else {
                max_num = 1;
            }
            now_candy = dir ? candy_board[i][j] : candy_board[j][i];
            res = max(res, max_num);
        }
    }

    return res;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int res = -1;

    cin >> N;
    
    // 캔디보드 채우기
    for (int i=0; i<N; i++){
        for (int j=0; j<N; j++){
            cin >> candy_board[i][j];
        }
    }

    // 탐색
    for (int i=0; i<N; i++){
        for (int j=0; j<N-1; j++){
            // 가로 swap
            if (candy_board[i][j] != candy_board[i][j+1]) {
                swap(candy_board[i][j], candy_board[i][j+1]);

                int row_max = return_max_candy(1); // 가로 방향 체크
                int column_max = return_max_candy(0); // 세로 방향 체크
                res = max(res, max(row_max, column_max));
                if (res == N) break;

                // 원복
                swap(candy_board[i][j], candy_board[i][j+1]);
            }

            // 세로 swap
            if (candy_board[j][i] != candy_board[j+1][i]) {
                swap(candy_board[j][i], candy_board[j+1][i]);

                int row_max = return_max_candy(1); // 가로 방향 체크
                int column_max = return_max_candy(0); // 세로 방향 체크
                res = max(res, max(row_max, column_max));
                if (res == N) break;

                // 원복
                swap(candy_board[j][i], candy_board[j+1][i]);
            }
        }
    }

    cout << res;
}

