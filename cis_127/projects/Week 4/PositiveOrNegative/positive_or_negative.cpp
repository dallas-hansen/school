// ================================================================================
// Name             : Positive Or Negative
// Author           : Dallas Hansen
// Course           : CIS 127 - 5541.W24
// Date             : February 2, 2024
// Description      : Determining if a number is positive or negative.
// ================================================================================

#include <iostream>
using namespace std;

int main() {
	double num1;

	cout << "Please enter any number:" << endl;
	cin >> num1;

	if (num1 > 0) {
		cout << num1 << " is a positive number" << endl;
	}
	else if (num1 == 0) {
		cout << num1 << " is exactly zero and is considered an \"unsigned\" number" << endl;
	}
	else {
		cout << num1 << " is a negative number" << endl;
	}

	return 0;
}