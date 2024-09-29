// ================================================================================
// Name             : Largest Number
// Author           : Dallas Hansen
// Course           : CIS 127 - 5541.W24
// Date             : February 2, 2024
// Description      : Find the largest of three numbers that are provided by the user
// ================================================================================

#include <iostream>
using namespace std;

int main() {
	int num1;
	int num2;
	int num3;
	int max;

	cout << "Please enter the first number:" << endl;
	cin >> num1;

	cout << "Please enter the second number:" << endl;
	cin >> num2;

	cout << "Please enter the third number:" << endl;
	cin >> num3;

	if ((num1 > num2) && (num1 > num3)) {
		max = num1;
	}
	else if ((num2 > num1) && (num2 > num3)) {
		max = num2;
	}
	else {
		max = num3;
	}

	cout << "1st Number = " << num1 << ",	2nd Number = " << num2 << ",	3rd Number = " << num3 << endl;
	cout << max << " is the largest number" << endl;

	return 0;
}