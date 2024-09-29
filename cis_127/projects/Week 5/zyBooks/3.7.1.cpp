// ================================================================================
// Name         : 
// Author       : Dallas Hansen
// Course       : CIS 127 - 5541.W24
// Date         : 
// Description  : 
// ================================================================================

#include <iostream>
#include <vector>
using namespace std;

int main() {
	vector<int> vect1;
	int value;
	int i;

	cin >> value;
	while (value != -1) {
		vect1.push_back(value);
		cin >> value;
	}

	for (i = vect1.size() - 1; i >= 0; --i)
	{
		if (vect1.at(i) > 0)
		{
			cout << vect1.at(i) << endl;
		}
	}

	return 0;
}