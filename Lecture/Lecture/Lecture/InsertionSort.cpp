/*Insertion Sort : »ğÀÔÁ¤·Ä*/

#include <iostream>

using namespace std;

int main() {
	int array[10] = { 1,10,5,8,7,6,4,3,2,9 };
	int j,temp;
	for (int i = 0; i < 9; i++) {
		j = i;
		while (j > 0 && array[j-1] > array[j ]) {
			temp = array[j-1];
			array[j-1] = array[j];
			array[j ] = temp;
			j--;
		}
	}
	for (int i = 0; i < 10; i++) {
		cout << array[i] << " ";
	}
}