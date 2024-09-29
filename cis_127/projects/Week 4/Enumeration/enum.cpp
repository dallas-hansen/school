// ================================================================================
// Name             : 
// Author           : Dallas Hansen
// Course           : CIS 127 - 5541.W24
// Date             : 
// Description      : 
// ================================================================================

#include <iostream>
using namespace std;

int main() {
	
	enum Light { red, green, yellow };

	Light LightState;

	LightState = red;

	cout << LightState;

	if (LightState == red)
		cout << endl << "Light is red";

	return 0;
}