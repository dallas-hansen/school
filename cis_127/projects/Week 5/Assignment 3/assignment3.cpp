// ================================================================================
// Name         : Assignment 3
// Author       : Dallas Hansen
// Course       : CIS 127 - 5541.W24
// Date         : 2/15/2024
// Description  : This program does three different things. The first thing is it
//				  assumes a 15 gallon gas tank, takes input from the user for the
//                various gas prices of Regular, Mid-Grade, and Premium, and then
//                multiplies each of the gas prices by the size of the tank, which
//                is assumed to be 15 gallons. It'll output this value to the user.
// 
//                The second thing is asking the user how many pets they own. Which
//                is then stored in a variable that is used to resize the vector
//                'petNames'. It then begins a loop that asks the user of each of
//                their pets names and stores them in 'petNames'. The names are not
//                shown to user because the instructions do not specify a need for
//                an output.
// 
//                Lastly, It'll be calculating the average score given a series of
//                inputs. The user will be prompted to give grades on assignments,
//                when they're done they will input 'q' and then the program will
//                sum all the values in the vector gradeList and divide by the 
//                size of the vector to give the mean grade.
// ================================================================================

#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
using namespace std;

int main() {
	unsigned short int i;
	unsigned short int sizeOfTank = 15;
	vector<string> gasTypes{ "Regular", "Mid-Grade", "Premium" };
	vector<float> gasPrices(gasTypes.size());
	vector<string> petNames;
	unsigned short int numOfPets;
	vector<float> gradeList;
	float average = 0;
	float summed = 0;
	string input;
	
	// populates the gasPrices vector with prices input by user
	for (i = 0; i < gasTypes.size(); ++i)
	{
		cout << "Enter the price of " << gasTypes.at(i) << " gas: " << endl;
		cin >> gasPrices.at(i);
	}

	cout << fixed << setprecision(2); // sets floating points to two decimal places

	// outputs the price of each type of gas multiplied by size of the tank
	for (i = 0; i < gasTypes.size(); ++i)
	{
		cout << "The cost to fill a " << sizeOfTank << " gallon tank with "
			<< gasTypes.at(i) << " gas is: $" << (gasPrices.at(i) * sizeOfTank)
			<< endl;
	}
	
	cout << endl;
	// Beginning second part
	cout << endl;

	// Asking user for input to determine vector size
	cout << "Please enter the number of pets that you have: " << endl;
	cin >> numOfPets;

	// Updating size of vector according to previous user input of numOfPets
	petNames.resize(numOfPets);

	// populates the petNames vector
	for (i = 0; i < petNames.size(); ++i)
	{
		cout << "Please enter the name of pet " << i + 1 << ":" << endl;
		cin >> petNames.at(i);
	}

	cout << "Wow! ";
	for (i = 0; i < petNames.size(); ++i) {
		if (i == petNames.size() - 1) {
			cout <<"and " << petNames.at(i) << " ";
		}
		else {
			cout << petNames.at(i) << ", ";
		}
	}
	cout << "are really great names!" << endl;


	cout << endl;
	// Beginning third part
	cout << endl;

	cout << "I will calculate your average grade in a class, please enter your"
		" grades one at a time." << endl;
	cout << endl << "Only numerical grade percentage between \"0-115\" is allowed" << endl;

	// User inputs as many grades as they'd like
	do 
	{
		cout << "Grade ('q' to quit):" << endl;
		cin >> input;

		if (input == "q")
			break;
		else if (isdigit(input[0]))
		{
			float grade = stof(input); // will convert string to float
			if (grade > 115 || grade < 0) {
				cout << "Value not within acceptable range, please try again." << endl;
				continue;
			}
			gradeList.push_back(grade); // adds grade to gradeList
		}
		else
		{
			cout << "That input is not allowed." << endl;
		}

	} while (input != "q");

	// Sums the values within the vector gradeList
	for (i = 0; i < gradeList.size(); ++i)
		summed += gradeList.at(i);

	// computes mean
	average = summed / gradeList.size();

	cout << "Your average grade is: " << average << "%" <<endl;

	return 0;
}