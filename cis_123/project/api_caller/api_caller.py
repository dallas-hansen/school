import requests
import json
from sites import Site
from save import *
from decorators import separator
from menu import *

def get_request(url: str) -> requests.Response:
    response = requests.get(url)
    return response

# This function prints JSON data in a more readable format
def print_json(json_data: dict) -> None:
    print(json.dumps(json_data, indent=4))

@separator()
def list_sites(sites: list) -> None:
    print('Sites:')
    for site in sites:
        print(f'{site.name.capitalize()}')

@separator()
def add_site(sites: list, name=None) -> None:
    if name is None:
        name = input('Enter site name: ').lower()
    name = Site(name)
    sites.append(name)
    
def delete_site(sites: list) -> None:
    list_sites(sites)
    print()
    name = input('Enter site name: ').lower()
    for site in sites:
        if site.name.lower() == name:
            name = site
            sites.remove(name)
            print(f'Site "{name.name.capitalize()}" deleted')
            break
    else:
        print('Site not found')
        
def choose_site(sites: list) -> Site:
    list_sites(sites)
    print()
    name = input('Enter site name: ').lower()
    for site in sites:
        if site.name.lower() == name:
            name = site
            return name
    else:
        return print('Site not found')
    
def list_endpoints(site: Site) -> None:
    print('Endpoints:')
    for name in site.endpoints:
        print(f'{name.capitalize()}')

def add_endpoints(site: Site) -> None:
    name = input('Enter endpoint name: ').lower()
    url = input('Enter endpoint url: ').lower()
    site.endpoints[name] = url

def del_endpoint(site: Site) -> None:
    list_endpoints(site)
    print()
    name = input('Enter endpoint name: ').lower()
    site.endpoints.pop(name)  

def main():
    menus = {'List Sites': list_sites,
                'Add Site': add_site,
                'Delete Site': delete_site,
                'Choose Site': choose_site,
                'Save': save_data}
    
    first_time = True
    current_choice = None
    breakout_words = ['exit', 'back', 'save']
    
    while current_choice != 'exit':
        current_choice = make_menu(menus)
        if current_choice.lower() not in breakout_words:
            
            while current_choice.lower() == 'choose site' and \
                current_choice not in breakout_words:
                    
                current_choice = menus[current_choice](sites)
                current_choice.main()
                current_choice = make_menu(current_choice.menu())
                # current_site = current_choice
                # current_choice = make_menu(current_site.main())
                print(current_choice)
            else:
                menus[current_choice](sites)
            
            if current_choice.lower() in menus:    
                menus[current_choice](sites)   
        elif current_choice.lower() == 'save':
            save_data(sites, 'sites')

if __name__ == "__main__":
    sites = load_data('sites')
    main()
    save_data(sites, 'sites')
    