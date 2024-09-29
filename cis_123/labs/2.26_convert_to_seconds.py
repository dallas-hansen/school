seconds = int(input())
minutes = int(input())
hours = int(input())

total_seconds = seconds + (minutes * 60) + (hours * 60 * 60)

print(f'{total_seconds} seconds')