import requests
import json
from classes.save import *
from classes.menu import *
from classes.sites import *

def get_request(url: str) -> requests.Response:
    response = requests.get(url)
    return response

# This function prints JSON data in a more readable format
def print_json(json_data: dict) -> None:
    print(json.dumps(json_data, indent=4))

def main():
    sites = load_data('sites')
    menus = MainMenu()
        
    current_choice = make_menu(menus.menu)
    breakout_words = ['exit', 'back', 'save']
    
    while current_choice != 'exit':
        if current_choice.lower() not in breakout_words:
            
            while current_choice.lower() == 'choose site' and \
                current_choice not in breakout_words:
                    
                current_choice = menus[current_choice](sites)
                current_choice.main()
                current_choice = make_menu(current_choice.menu)
            else:
                print('Invalid choice')
                current_choice = make_menu(menus.menu)
                
        elif current_choice.lower() == 'save':
            save_data(sites, 'sites')
        
    save_data(sites, 'sites')

if __name__ == "__main__":
    main()
    