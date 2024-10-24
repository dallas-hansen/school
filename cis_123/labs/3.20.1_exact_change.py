change = int(input())

dollars = change // 100
quarters = change % 100 // 25
dimes = change % 25 // 10
nickles = change % 25 % 10 // 5
pennies = change % 25 % 10 % 5

if change == 0:
    print('No change')
    
change_type = {'Dollar': dollars, 
               'Quarter': quarters, 
               'Dime': dimes, 
               'Nickel': nickles, 
               'Penny': pennies}

for k,v in change_type.items():
    if v == 1:
        print(f'{v} {k}')
    elif v > 0 and k != 'Penny':
        print(f'{v} {k}s')
    elif v > 0 and k == 'Penny':
        print(f'{v} Pennies')
        
# if dollars == 1:
#     print(f'{dollars} Dollar')
# elif dollars != 0:
#     print(f'{dollars} Dollars')

# if quarters == 1:
#     print(f'{quarters} Quarter')
# elif quarters > 0:
#     print(f'{quarters} Quarters')

# if dimes == 1:
#     print(f'{dimes} Dime')
# elif dimes > 0:
#     print(f'{dimes} Dimes')

# if nickles == 1:
#     print(f'{nickles} Nickel')
# elif nickles > 0:
#     print(f'{nickles} Nickels')

# if pennies == 1:
#     print(f'{pennies} Penny')
# elif pennies > 0:
#     print(f'{pennies} Pennies')
