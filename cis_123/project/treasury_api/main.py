import requests
import json

def get_request(url: str) -> requests.Response:
    response = requests.get(url)
    return response

# This function prints JSON data in a more readable format
def print_json(json_data: dict) -> None:
    print(json.dumps(json_data, indent=4))
    
# Creates a menu based on input dictionary and returns user input
def make_menu(options: dict) -> str:
    option_dict = {}
    count = 0
    for key in options.keys():
        count += 1
        option_dict[str(count)] = key
        
    
    return make_choice(option_dict)

# Returns menu choice
def make_choice(options: dict) -> str:
    
    for k,v in options.items():
        print(f'{k} - {v}')
    
    print('0 - Exit')
    choice = input("Enter your choice: ")
    
    if choice == '0':
        return None
    
    while choice not in options.keys() or choice.isnumeric() == False:
        print('Invalid option, please try again')
        choice = input("Enter your choice: ")

    return options[choice]

def main():
    # API endpoints
    endpoints = {'transactions': '/v1/accounting/dts/deposits_withdrawals_operating_cash',
                 'debts': '/v1/accounting/dts/public_debt_transactions',
                 'balance': '/v1/accounting/dts/operating_cash_balance'}
    
    # API sites
    sites = {'Treasury': 'https://api.fiscaldata.treasury.gov/services/api/fiscal_service'}
    
    
    while True:
        make_menu(sites)
        break        

if __name__ == "__main__":
    main()