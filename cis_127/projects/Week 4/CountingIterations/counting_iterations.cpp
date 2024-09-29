// ================================================================================
// Name             : Counting Iterations
// Author           : Dallas Hansen
// Course           : CIS 127 - 5541.W24
// Date             : February 2, 2024
// Description      : Displays iteration number, quits when user inputs 'q'
// ================================================================================

#include <iostream>
#include <string>
using namespace std;

int main() {
	string quit;
	int count = 0;

	cout << "Type anything other than \"Q\" and hit enter to start the loop" << endl;
	getline(cin, quit);

	cout << "To exit the loop, please type \"Q\" and hit enter when prompted - case sensitive" << endl;

	while (quit != "Q") {
		++count;
		cout << "This is loop #" << count << "." << endl;
		cout << "\"Q\" to quit" << endl;
		cin >> quit;
	}
	return 0;
}