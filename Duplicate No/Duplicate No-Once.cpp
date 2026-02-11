#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter number of elements: ";
    cin >> n;

    int arr[n];

    cout << "Enter elements:\n";
    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    cout << "Duplicate elements (printed once):\n";

    for(int i = 0; i < n; i++) {
        int count = 0;

        for(int j = 0; j < i; j++) {
            if(arr[i] == arr[j]) {
                count = 1;   
                break;
            }
        }

        if(count == 0) {
            for(int k = i+1; k < n; k++) {
                if(arr[i] == arr[k]) {
                    cout << arr[i] << " ";
                    break;
                }
            }
        }
    }

    return 0;
}
