from decorators import separator
from classes.sites import Site
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

# TODO: change menu into a class
# class Menu:
#     def __init__(self) -> None:
#         self.sites = {}
#         self.choice = None
#         self.level = 0
#         self.menu = {}

#     def main(self) -> None:
#         pass
    
#     def menu(self) -> None:
#         pass
    
#     def __call__(self) -> None:
#         pass
    
#     def make_menu(self, options: dict, level=0) -> str:
#         option_dict = {}
#         count = 0
        
#         for key in options.keys():
#             count += 1
#             option_dict[str(count)] = key
#         if level == 0:
#             option_dict['0'] = 'Exit'
#         else:
#             option_dict['0'] = 'Back'
        
#             return make_choice(option_dict)

#     # Returns menu choice
#     @separator()
#     def make_choice(self, options: dict) -> str:
#         for k,v in options.items():
#             print(f'{k} - {v}')
        
#         choice = input("Enter your choice: ")
        
#         if choice == '0':
#             return 'exit'
        
#         while choice not in options.keys():
#             print('Invalid option, please try again')
#             choice = input("Enter your choice: ")

#         return options[choice]

#     # Site menu options
#     @separator()
#     def list_sites(self, sites: list) -> None:
#         print('Sites:')
#         for site in sites:
#             print(f'{site.name.capitalize()}')

#     @separator()
#     def add_site(self, sites: list, name=None) -> None:
#         if name is None:
#             name = input('Enter site name: ').lower()
#         name = Site(name)
#         sites.append(name)
        
#     def delete_site(self, sites: list) -> None:
#         list_sites(sites)
#         print()
#         name = input('Enter site name: ').lower()
#         for site in sites:
#             if site.name.lower() == name:
#                 name = site
#                 sites.remove(name)
#                 print(f'Site "{name.name.capitalize()}" deleted')
#                 break
#         else:
#             print('Site not found')
            
#     def choose_site(self, sites: list) -> Site:
#         list_sites(sites)
#         print()
#         name = input('Enter site name: ').lower()
#         for site in sites:
#             if site.name.lower() == name:
#                 name = site
#                 return name
#         else:
#             return print('Site not found') 