// ================================================================================
// Name         : Zybooks Testing
// Author       : Dallas Hansen
// Course       : CIS 127 - 5541.W24
// Date         : 
// Description  : 
// ================================================================================

#include <iostream>
using namespace std;

int Fibonacci(int n) {
	if (n <= 1) {
		return n; // Base case: Return n if n is 0 or 1
	}

	int curr_num = 1; // Initialize current Fibonacci number to 1
	int prev_num = 0; // Initialize previous Fibonacci number to 0

	// Generate the nth Fibonacci number
	for (int i = 2; i <= n; ++i) {
		int temp = curr_num; // Store current Fibonacci number in a temporary variable
		curr_num += prev_num; // Calculate the new current Fibonacci number
		prev_num = temp; // Update previous Fibonacci number to the previous current Fibonacci number
	}

	return curr_num; // Return the nth Fibonacci number
}


int main() {
	int startNum;

	cin >> startNum;
	cout << "Fibonacci(" << startNum << ") is " << Fibonacci(startNum) << endl;

	return 0;
}