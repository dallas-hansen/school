first, last, year = input().split()

if len(first) > 6:
    first = first[:6]

print(f'Your login name: {first}{last[0]}_{year[-1]}')