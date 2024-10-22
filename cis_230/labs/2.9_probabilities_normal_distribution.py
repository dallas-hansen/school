# Import norm from scipy.stats
from scipy.stats import norm

# Input two IQs, making sure that IQ1 is less than IQ2
IQ1 = float(input())
IQ2 = float(input())

while IQ1 > IQ2:
    print("IQ1 should be less than IQ2. Enter numbers again.")
    IQ1 = float(input())
    IQ2 = float(input())

# Mean and standard deviation for IQ scores
mean_IQ = 100
std_dev_IQ = 15

# Convert IQ1 and IQ2 to z-scores
z1 = (IQ1 - mean_IQ) / std_dev_IQ
z2 = (IQ2 - mean_IQ) / std_dev_IQ

# Calculate the probability that a randomly selected person has an IQ less than or equal to IQ1.
probLT = norm.cdf(z1)

# Calculate the probability that a randomly selected person has an IQ between IQ1 and IQ2
probBetw = norm.cdf(z2) - norm.cdf(z1)

# Print results
print("The probability that a randomly selected person \n has an IQ less than or equal to " + str(IQ1) + " is ", end="")
print('%.3f' % probLT + ".")
print("The probability that a randomly selected person \n has an IQ between " + str(IQ1) + " and " + str(IQ2)+ " is ", end="")
print('%.3f' % probBetw + ".")
