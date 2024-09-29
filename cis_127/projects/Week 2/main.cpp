// ================================================================================
// Name             : Assignment 1
// Author           : Dallas Hansen
// Course           : CIS 127 - 5541.W24
// Date             : January 20, 2024
// Description      : Outputs a sentence using "age" and "name" provided by user.
// ================================================================================

#include <iostream>
#include <cstring>

using namespace std;

int main()
{
	string userName;
	int userAge;

	cout << "What is your name?" << endl; // asks user for name
	cin >> userName;

	cout << "What is your age?" << endl; // asks user for age
	cin >> userAge;

	cout << userName << " welcome to CIS 127 C++ 1. When you took this class you were " << userAge << " years old." << endl;

	return 0;
}
