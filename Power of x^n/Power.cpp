#include <iostream>
using namespace std;

int main() {
    int x, n;
    
    cout << "Enter value of x: ";
    cin >> x;

    cout << "Enter value of n: ";
    cin >> n;

    long long result = 1;

    for(int i = 1; i <= n; i++) {
        result = result * x;
    }

    cout << x << " raised to " << n << " = " << result;

    return 0;
}
