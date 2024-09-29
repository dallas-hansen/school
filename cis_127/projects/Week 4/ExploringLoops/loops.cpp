// ================================================================================
// Name             : 
// Author           : Dallas Hansen
// Course           : CIS 127 - 5541.W24
// Date             : 
// Description      : 
// ================================================================================

#include <iostream>
#include <string>

using namespace std;

int main()
{
	char response;
	while (true)
	{
		cout << "Exit Loop?";
		cin >> response;

		if (response == 'Y')
		{
			break;
		}
	}

	cout << "Out of Loop.";

	int counter = 0;

	while (counter <= 10)
	{
		cout << endl << counter;
		counter++;
	}

	do
	{

		cout << endl << "in do loop";

		cout << endl << "Exit Loop?";
		cin >> response;

		if (response == 'Y')
			break;

	} while (true);

	do
	{
		cout << endl << counter;
		counter--;

	} while (counter >= 0);

	return 0;
}