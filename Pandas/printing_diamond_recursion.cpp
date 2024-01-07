#include <iostream>
using namespace std;

void print_spaces(int n) {
    if (n <= 0) {
        return;
    }
    cout << " ";
    print_spaces(n - 1);
}

void print_asterisks(int n) {
    if (n <= 0) {
        return;
    }
    cout << "*";
    print_asterisks(n - 1);
}

void print_diamond(int n, int i = 0) {
    if (n <= 0) {
        return;
    }
    print_spaces(n - 1);
    print_asterisks(2 * i + 1);
    cout << endl;
    print_diamond(n - 1, i + 1);
    print_spaces(n - 1);
    print_asterisks(2 * i + 1);
    cout << endl;
}

int main() {
    print_diamond(4);
    return 0;
}