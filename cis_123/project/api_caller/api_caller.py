from calendar import c
import os
import requests
import json
import pickle
from typing import Any
from sites import Site

def separator(symbol='-', length=50) -> None:
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f'{symbol * length}')
            result = func(*args, **kwargs)
            return result
        return wrapper 
    return decorator 

def load_data(filename: str) -> Any: 
    if os.path.exists(fr'data\{filename}.pkl'):
        with open('{filename}.pkl', 'r') as file:
            data = pickle.load(file)
            return data
    else:
        data = []
        return data
    
def save_data(data: Any, filename: str) -> None:
    for cls in data:
        cls.save()
    with open (fr'data\{filename}.pkl', 'w') as file:
        pickle.dump(data, file)

def get_request(url: str) -> requests.Response:
    response = requests.get(url)
    return response

# This function prints JSON data in a more readable format
def print_json(json_data: dict) -> None:
    print(json.dumps(json_data, indent=4))
    
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

@separator()
def list_sites(sites: list) -> None:
    print('Sites:')
    for index, site in enumerate(sites):
        print(f'{index+1} - {site.name.capitalize()}')

@separator()
def add_site(sites: list, name=None) -> None:
    if name is None:
        name = input('Enter site name: ').lower()
    name = Site(name)
    sites.append(name)
    
def delete_site(sites: list) -> None:
    list_sites(sites)
    name = input('Enter site name: ').lower()
    for site in sites:
        if site.name.lower() == name:
            name = site
            sites.remove(name)
            print(f'Site "{name.name.capitalize()}" deleted')
            break
    else:
        print('Site not found')
    
    
    

def main():
    # categories = {
    # # API sites
    # 'sites': {'Treasury': 'https://api.fiscaldata.treasury.gov/services/api/fiscal_service'},
    
    # # API endpoints
    # 'treasury': {'transactions': '/v1/accounting/dts/deposits_withdrawals_operating_cash',
    #              'debts': '/v1/accounting/dts/public_debt_transactions',
    #              'balance': '/v1/accounting/dts/operating_cash_balance'}    
    # }
    
    # treasury = Site()
    menu = {'List Sites': list_sites,
            'Add Site': add_site,
            'Delete Site': delete_site}
    
    first_time = True
    current_choice = None
    
    while current_choice != 'exit':
        if first_time:
            current_choice = make_menu(menu, 0)
            print(current_choice)
            if current_choice != 'exit' and current_choice != 'back':
                menu[current_choice](sites)
            first_time = False
        else:
            current_choice = make_menu(menu, 0)
            if current_choice != 'exit' and current_choice != 'back':
                menu[current_choice](sites)

if __name__ == "__main__":
    # sites = load_data('sites')
    
    
    sites = []
    add_site(sites, 'Treasury')
    
    main()
    
    print('Saving Progress...')
    
    # save_data(sites, 'sites')
    
    print('Saved')
    