#include <iostream>
using namespace std;

int main() {

    int position = 0;
    int velocity = 2;   

    for(int i = 0; i < 20; i++) {

        position = position + velocity;

        if(position >= 10 || position <= 0) {
            velocity = -velocity;  
        }

        cout << "Position: " << position << endl;
    }

    return 0;
}
