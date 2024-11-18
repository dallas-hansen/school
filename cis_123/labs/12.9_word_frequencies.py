import csv
from collections import Counter

def count_word_frequencies(filename: str) -> None:
    try:
        with open(filename, 'r') as file:
            # Use csv.reader to read the comma-separated values
            reader = csv.reader(file)
            
            # Read the first row (assuming all words are in a single line)
            words = next(reader)
            
            # Use Counter to count frequencies of each word
            word_count = Counter(words)
            
            # Print out each word with its frequency
            for word, count in word_count.items():
                print(f"{word} - {count}")
    
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Read the input filename from the user
filename = input()

# Call the function to count word frequencies
count_word_frequencies(filename)
