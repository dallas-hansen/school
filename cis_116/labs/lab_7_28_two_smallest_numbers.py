# Creates a sorted list of integers from a single input string
nums = sorted(list(map(int, input().split())))

# Prints out first two items in sorted list (smallest two)
print(f'{nums[0]} and {nums[1]}')
