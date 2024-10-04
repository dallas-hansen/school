nums = list(map(int, input().split()))
bounds = list(map(int, input().split()))

for numbers in nums:
    if numbers in range(bounds[0], bounds[1] + 1):
        print(f'{numbers},', end='')