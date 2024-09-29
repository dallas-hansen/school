// ================================================================================
// Name         : 
// Author       : Dallas Hansen
// Course       : CIS 127 - 5541.W24
// Date         : 
// Description  : 
// ================================================================================

#include <iostream>
#include <string>

using namespace std;

int main() 
{
	
	string GroceryList[] = {"Milk", "Butter"};
	unsigned short	int Numbers[] = { 1, 3, 4, 5, 6 };

	cout << GroceryList[0] << endl;
	cout << GroceryList[1] << endl;

	cout << Numbers[4] << endl;
	
	Numbers[4] = 10;
	cout << "New number: " << Numbers[4] << endl;

	for (int index = 0; index < 2; index++)
	{
		cout << GroceryList[index] << endl;
	}

	double Gas_Prices[3];

	int ArraySize = ((sizeof(Gas_Prices) / sizeof(int) / 2));

	for (int index = 0; index < ArraySize; index++)
	{
		Gas_Prices[index] = index;
	}

	for (int index = 0; index < ArraySize; index++)
	{
		cout << Gas_Prices[index] << endl;
	}
	return 0;
}