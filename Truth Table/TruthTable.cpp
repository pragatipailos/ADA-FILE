#include <iostream>
using namespace std;

int main() {

    cout << "A B C | F\n";
    cout << "-------------\n";

    for(int A = 0; A <= 1; A++) {
        for(int B = 0; B <= 1; B++) {
            for(int C = 0; C <= 1; C++) {

                int F = (A && B) || C;

                cout << A << " " << B << " " << C << " | " << F << endl;
            }
        }
    }

    return 0;
}
