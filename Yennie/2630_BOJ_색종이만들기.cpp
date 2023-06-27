#include <iostream>

using namespace std;

int N;
int paper[130][130];
int res[2];

void check_paper(int col, int row, int line) 
{
    if (col >= N || row >= N || line < 1) return;

    int color = paper[col][row];
    bool is_square = true;

    for (int i=col; i<col+line; i++) {
        if (!is_square) break;
        for (int j=row; j<row+line; j++) {
            if (paper[i][j] != color) {
                check_paper(col, row, line/2);
                check_paper(col, row+line/2, line/2);
                check_paper(col+line/2, row, line/2);
                check_paper(col+line/2, row+line/2, line/2);
                is_square = false;
                break;
            }
        }
    }
    if (is_square) res[color]++;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> N;

    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> paper[i][j];
        }
    }

    check_paper(0, 0, N);

    cout << res[0] << "\n" << res[1];
    
    return 0;
}

/*
1차 시도 코드
#define cp pair<int, int> // (column, row)

vector<cp> find_coordinates(int col, int row, int step)
{
    vector<cp> coordis;

    int ncol = col;
    for (int i=0; i<2; i++) {
        int nrow = row;
        for (int j=0; j<2; j++) {
            if (nrow >= N || ncol >= N) continue;
            coordis.push_back(make_pair(ncol, nrow));
            nrow += step;
        }
        ncol += step;
    }
    return coordis;
}

void check_paper(int col, int row, int line)
{
    // 자른 종이 덩어리 덩어리
    vector<cp> coordis = find_coordinates(col, row, line);
    for (const auto& c : coordis) {
        int col = c.first;
        int row = c.second;
        int color = paper[col][row];

        bool is_square = true;
        for (int i=col; i<col+line; i++) {
            if (!is_square) break;
            for (int j=row; j<row+line; j++) {
                // 범위를 벗어난 경우
                if (i >= N || j >= N) break;
                
                // 시작점과 컬러가 다른 경우 => 종이 N/2으로 쪼개기
                if (paper[i][j] != color) {
                    is_square = false;
                    check_paper(col, row, line/2);
                    break;
                }
            }
        }
        if (is_square) {
            res[color]++;
        }
    }
}
*/