def check_range(filename: str, lower_bound: str, upper_bound: str) -> None:
    try:
        # Open the file and read all lines
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        # Loop through each line in the file
        for line in lines:
            word = line.strip()  # Remove any leading/trailing whitespace
            
            # Check if the word is within the specified range (inclusive)
            if lower_bound <= word <= upper_bound:
                print(f"{word} - in range")
            else:
                print(f"{word} - not in range")
                
    except FileNotFoundError:
        print("The specified file does not exist.")

# Read inputs from the user
filename = input()
lower_bound = input()
upper_bound = input()

# Call the function with the inputs
check_range(filename, lower_bound, upper_bound)
