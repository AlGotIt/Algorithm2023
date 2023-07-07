#include <iostream>
#include <map>
#include <stack>
#include <string>
#include <iomanip>

using namespace std;

int main() 
{   
    int N;
    string expression;
    string operators = "+-*/";

    cin >> N >> expression;

    map<char, int> alpha;
    for (int i='A'; i<'A'+ N; i++) {
        cin >> alpha[static_cast<char>(i)];
    }

    stack<double> st;
    for (char c : expression) {
        if (operators.find(c) == string::npos) {
            st.push(alpha[c]);
        } else {
            double num2 = st.top(); st.pop();
            double num1 = st.top(); st.pop();
            double res;
            switch (c) {
                case '+':
                    res = num1 + num2;
                    break;
                case '-':
                    res = num1 - num2;
                    break;
                case '*':
                    res = num1 * num2;
                    break;
                case '/':
                    res = num1 / num2;
                    break;
                default:
                    break;
            }
            st.push(res);
        }
    }

    cout << fixed << setprecision(2) << st.top() << endl;    

    return 0;
}