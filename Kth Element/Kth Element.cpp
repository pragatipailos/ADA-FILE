#include <iostream>
using namespace std;

int partition(int arr[], int low, int high) {
    int pivot = arr[high];   
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;   
}

int quickSelect(int arr[], int low, int high, int k) {
    if (low <= high) {
        int pi = partition(arr, low, high);

        if (pi == k - 1)         
            return arr[pi];
        else if (pi > k - 1)      
            return quickSelect(arr, low, pi - 1, k);
        else                    
            return quickSelect(arr, pi + 1, high, k);
    }
    return -1;
}

int main() {
    int arr[] = {7, 10, 4, 3, 20, 15};
    int n = 6;
    int k = 3;   

    cout << "K-th smallest element is: "
         << quickSelect(arr, 0, n - 1, k);

    return 0;
}
