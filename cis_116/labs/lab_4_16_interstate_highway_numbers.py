# highway = int(input())
#
# if highway / 100 < 1:
#     if highway == 0:
#         print(f'{highway} is not a valid interstate highway number.')
#     elif highway % 2 == 0:
#         print(f'I-{highway} is primary, going east/west.')
#     else:
#         print(f'I-{highway} is primary, going north/south.')
# else:
#     if highway % 100 == 00:
#         print(f'{highway} is not a valid interstate highway number.')
#     elif highway % 2 == 0:
#         print(f'I-{highway} is auxiliary, serving I-{highway % 100}, going east/west.')
#     else:
#         print(f'I-{highway} is auxiliary, serving I-{highway % 100}, going north/south.')


highway_number = int(input())

''' Type your code here. '''

if 100 < highway_number > 999 and highway_number % 100 != 0:
    print(f'{highway_number} is auxilary, going', end=' ')
    primary_highway = highway_number % 100
    if highway_number % 2 == 0:
        print('north/south')
    else:
        print('east/west')

elif 1 <= highway_number <= 99 and highway_number != 0:
    print(f'{highway_number} is primary, going', end=' ')
    if highway_number % 2 == 0:
        print('north/south')
    else:
        print('east/west')

else:
    print(f'{highway_number} is not a valid interstat highway number.')