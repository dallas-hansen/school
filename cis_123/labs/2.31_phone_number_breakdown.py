phone_number = int(input())

area_code = phone_number // 10000000
first_three = phone_number % 10000000 // 10000
last_four = phone_number % 10000

print(f'({area_code}) {first_three}-{last_four}')
