// ================================================================================
// Name         : Assignment #4
// Author       : Dallas Hansen
// Course       : CIS 127 - 5541.W24
// Date         : 2/22/2024
// Description  : This program is a combination of 3 programs. 
//                The countingIterations function will keep track of the amount
//                of times the user would like to loop through, requiring
//                user input at the beginning of each function. The "count"
//                variable is stored in the scope of main() and is passed to
//                countingIterations as a pass by reference parameter. Passing
//                the parameter this way keeps "count" outside of the while loop
//                and allows for keeping track of the number of iterations.
// 
//                The other two are pretty simple programs.
//                largestNumber simply asks the user for 3 inputs, and then 
//                outputs the largest of the three.
// 
//                positiveOrNegative takes in only one input from user
//                (within the function) and prints whether it was positive
//                or negative to the screen. This function returns nothing.
// ================================================================================

#include <iostream>
#include <string>
#include "Functions.h"
using namespace std;

int main() {
	int count = 0;

	// continueLoop returns true or false depending on user input.
	while (continueLoop()) {
		countingIterations(count);
	}
	spaceBetweenFunctions();
	largestNumber();
	spaceBetweenFunctions();
	positiveOrNegative();
	return 0;
}