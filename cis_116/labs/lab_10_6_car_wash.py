# services = {'Air freshener': 1, 'Rain repellent': 2, 'Tire shine': 2, 'Wax': 3, 'Vacuum': 5}
# base_wash = 10
# total = 0
#
# service_choice1 = input()
# service_choice2 = input()
#
# print('''ZyCar Wash
# Base car wash - $10''')
#
# if service_choice1 in services.keys():
#     total += services[service_choice1]
#     print(f'{service_choice1} - ${services[service_choice1]}')
# if service_choice2 in services.keys():
#     total += services[service_choice2]
#     print(f'{service_choice2} - ${services[service_choice2]}')
#
# print('-----')
# print(f'Total price: ${total + base_wash}')


###################################################

# Professors Example

services = {'Air freshener': 1,
            'Rain repellent': 2,
            'Tire shine': 2,
            'Wax': 3,
            'Vacuum': 5}

base_wash = 10
total = 0

service_choice1 = input()
service_choice2 = input()
total += base_wash
print(f'ZyCar Wash\nBase Wash - ${base_wash}')
print_list = []

for key, value in services.items():
    if service_choice1 == key:
        total += value
        print_list.insert(0, f'{key} - ${value}')

    if service_choice2 == key:
        total += value
        print_list.append(f'{key} - ${value}')

for elem in print_list:
    print(elem)

print('-----')
print(f'Total price: ${total}')