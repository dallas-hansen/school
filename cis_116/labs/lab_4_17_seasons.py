month = input()
day = int(input())

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

if month not in months or day > 31 or day < 1:
    print('Invalid')
    month = 'Invalid'
if month == 'September' and day > 30:
    print('Invalid')
    month = 'Invalid'

seasons = {'Spring': ['April', 'May'],
           'Summer': ['July', 'August'],
           'Autumn': ['November', 'October'],
           'Winter': ['January', 'February']}

weirdos = {'March': 20,
           'June': 21,
           'September': 22,
           'December': 21}

for i in seasons:
    if month in seasons[i]:
        print(i)
if day < weirdos[month]:
    if month == 'March':
        print('Winter')
    if month == 'June':
        print('Spring')
    if month == 'September':
        print('Summer')
    if month == 'December':
        print('Autumn')
else:
    if month == 'March':
        print('Spring')
    if month == 'June':
        print('Summer')
    if month == 'September':
        print('Autumn')
    if month == 'December':
        print('Winter')