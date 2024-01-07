#include <iostream>
using namespace std;

const int MAXN = 10;

int board[MAXN];
int n;
int count;
int counter = 0;
bool is_valid(int row, int col) {
    for (int i = 0; i < row; i++) {
        if (board[i] == col || abs(board[i] - col) == abs(i - row)) {
            return false;
        }
    }
    return true;
}

void solve_n_queens(int row) {
    int count = 0;
    if (row == n) {
        count++;
        counter++;
        return;
    }
    for (int col = 0; col < n; col++) {
        if (is_valid(row, col)) {
            board[row] = col;
            solve_n_queens(row + 1);
        }
    }
}

int main() {
    n = 4;
    solve_n_queens(0);
    cout << "Number of solutions: " << counter << endl;
    return 0;
}