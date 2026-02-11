#include <iostream>
#include <algorithm>
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

    sort(arr, arr + n);

    cout << "Missing numbers:\n";

    for(int i = 0; i < n-1; i++) {
        for(int j = arr[i] + 1; j < arr[i+1]; j++) {
            cout << j << " ";
        }
    }

    return 0;
}
