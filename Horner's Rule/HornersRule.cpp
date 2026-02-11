#include <iostream>
using namespace std;

int main() {
    int n;
    
    cout << "Enter degree of polynomial: ";
    cin >> n;

    int a[n+1];

    cout << "Enter coefficients from highest degree to constant:\n";
    for(int i = 0; i <= n; i++) {
        cin >> a[i];
    }

    int x;
    cout << "Enter value of x: ";
    cin >> x;

    int result = a[0];

    for(int i = 1; i <= n; i++) {
        result = result * x + a[i];
    }

    cout << "Value of polynomial = " << result;

    return 0;
}
