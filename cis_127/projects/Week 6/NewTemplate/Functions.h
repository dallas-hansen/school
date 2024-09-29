#pragma once
#include <iostream>
#include <string>
using namespace std;

// the count loop that uses a pass by reference parameter.
void countingIterations(int& count) {
	++count;
	cout << "This is loop #" << count << "." << endl;
}

// Checks if user wants to continue loop. Q quits the loop.
bool continueLoop() {
	string quit;
	cout << "Press Q or q to quit. Enter anything else to continue loop." << endl;
	getline(cin, quit);
	if (quit != "Q" && quit != "q")
		return true;
	else
		return false;
}

// Takes in three numbers and prints out the largest of the three
void largestNumber() {
	cout << "Given three numbers I'll find the biggest of them." << endl;
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
	cout << endl << max << " is the largest number" << endl;
}

// determines if the number input by users is positive or negative
void positiveOrNegative() {
	double num1;

	cout << "If you tell me a number, I can tell you if it's positive or negative."<< endl;

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

}
	
// adds space between functions in the program to make it cleaner.
void spaceBetweenFunctions() {
	cout << endl;
	cout << "===========================================================" << endl;
	cout << endl;
}