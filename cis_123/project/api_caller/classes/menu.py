from decorators import separator
from classes.save import *

sites = load_data('sites')

# Creates a menu based on input dictionary and returns user input
def make_menu(options: dict, level=0) -> str:
    option_dict = {}
    count = 0
        
    for key in options.keys():
        count += 1
        option_dict[str(count)] = key
    if level == 0:
        option_dict['0'] = 'Exit'
    else:
        option_dict['0'] = 'Back'
    
    return make_choice(option_dict)

# Returns menu choice
@separator()
def make_choice(options: dict) -> str:
    for k,v in options.items():
        print(f'{k} - {v}')
    
    choice = input("Enter your choice: ")
    
    if choice == '0':
        return 'exit'
    
    while choice not in options.keys():
        print('Invalid option, please try again')
        choice = input("Enter your choice: ")

    return options[choice]