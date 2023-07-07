#include <iostream>
#include <string>
#include <algorithm>
 
using namespace std;
 
int R, C;
char puz[22][22];
string first_word = "";
 
void find_first_word(int y, int x, int dir)
{
    for (int i=0; i<y; i++) {
        string res = "";
        string temp = "";
        for (int j=0; j<x; j++) {
            char c = dir ? puz[j][i] : puz[i][j];
            if (c == '#') {
                temp = (res.length() > 1) ? ((temp.length() > 1) ? min(temp, res) : res) : ((temp.length() > 1) ? temp : "");
                res = "";
                continue;
            }
            res += c;
        }
        res = (res.length() > 1) ? ((temp.length() > 1) ? min(res, temp) : res) : ((temp.length() > 1) ? temp : "");
        if (res.empty()) continue;
 
        first_word = (first_word.empty()) ? res : min(first_word, res);
    }
}
 
int main()
{
    cin >> R >> C;
 
    for (int i=0; i<R; i++) {
        for (int j=0; j<C; j++) {
            cin >> puz[i][j];
        }
    }
 
    find_first_word(R, C, 0); // row 탐색
    find_first_word(C, R, 1); // column 탐색
 
    cout << first_word << endl;
 
    return 0;
}