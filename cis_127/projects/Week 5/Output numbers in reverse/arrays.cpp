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
	vector<int> userInts;
	int numInts;
	int i;

	cin >> numInts;
	userInts.resize(numInts);

	for (i = 0; i < userInts.size(); ++i)
	{
		cin >> userInts.at(i);
	}
	
	for (i = userInts.size() - 1; i >= 0; --i)
	{
		cout << userInts.at(i) << ",";
	}
	cout << endl;
	return 0;
}