import pandas as pd
from classes.save import save_data
from decorators import box_decorator

class Site():
    
    def __init__(self, name, menu={}):
        self.name = name.lower()
        self.url = None
        self.endpoints = {}
        self.parameters = {}
        self.main_menu = menu
        self.menu = {}
        self.page_size = None
        self.data = []
    
    @box_decorator
    def list_items(self, input_list: list) -> None:
        return input_list
    
    def edit(self):
        menu = {
            "Back": 'back',
            "Change name": self.change_name,
            "Change url": self.change_url,
            "Edit endpoints": {
                "Back": 'back',
                "Add endpoints": self.add_endpoints,
                "Remove endpoints": self.remove_endpoints
                },
            "Edit parameters": {
                "Back": 'back',
                "Auto Search": self.populate_parameters,
                "Add parameters": self.add_parameters,
                "Remove parameters": self.remove_parameters,
                "Advanced" : {
                    "Back": 'back',
                    "Default page size": self.default_page_size,
                    "Edit page size": self.edit_page_size
                    }
                },
            "Reset": self.reset
            }
        return menu
    
    def reset(self) -> None:
        print("WARNING: This will reset all changes made to this site.")
        print("You will lose all data associated with this site.")
        print("Are you sure you want to continue? (y/n) ")
        if input().lower() == "y":
            self.__init__(self.name)
            print("Site reset successfully.", end='\n\n')
        
    def change_name(self) -> None:
        name = input("Enter new name: ")
        self.name = name.lower()
        self.main_menu[name] = self.name
        print("Name changed successfully.")

    def change_url(self) -> None:
        new_url = input("Enter new url: ")
        self.url = new_url
        print("URL changed successfully.")

    def add_endpoints(self) -> None:
        while True:
            new_endpoint = input("\nEnter name of new endpoint: ")
            new_endpoint_url = input("Enter url of new endpoint: ")
            self.endpoints[new_endpoint] = new_endpoint_url
            print("Endpoint added successfully.")
            choice = input("Do you want to add another endpoint? (y/n) ")
            if choice.lower() == "n":
                return
    
    def remove_endpoints(self) -> None:
        while True:
            print('\nList of current endpoints:')
            self.list_items(self.endpoints)
            choice = input('Enter the name of the endpoint you want to remove: ')
            if choice in self.endpoints:
                self.endpoints.pop(choice)
                print('Endpoint removed successfully.')
            else:
                print('Endpoint not found.')
            choice = input('Do you want to remove another endpoint? (y/n) ')
            if choice.lower() == "n":
                return
    
    def add_parameters(self) -> None:
        while True:
            new_parameter = input("\nEnter new parameter: ")
            self.parameters.append(new_parameter)
            print("Parameter added successfully.")
            choice = input("Do you want to add another parameter? (y/n) ")
            if choice.lower() == "n":
                return
    
    def remove_parameters(self) -> None:
        while True:
            print('\nList of current parameters:')
            self.list_items(self.parameters)
            choice = input('Enter the name of the parametersyou want to remove: ')
            if choice in self.parameters:
                self.parameters.remove(choice)
                print('Parameter removed successfully.\n')
            else:
                print('Parameter not found.\n')
            choice = input('Do you want to remove another parameter? (y/n) ')
            if choice.lower() == "n":
                return
    
    #TODO: create a way to use the api to populate the parameters
    def populate_parameters(self) -> None:
        print('This feature is not yet implemented.')
    
    def default_page_size(self) -> None:
        self.page_size = None
        print('Page size reset to default.')
    
    def current_page_size(self) -> None:
        print(f'Current page size: {self.page_size}\n\n')

    def edit_page_size(self) -> None:
        print("\nPlease be reasonable with your page size.")
        if 'page[size]' in self.parameters:
            self.current_page_size()
            prompt = input('Do you want to continue? (y/n) ')
            while prompt.lower() == 'y':
                try:
                    page_size = int(input('Enter page size (Enter to go back): '))
                    if page_size == '':
                        break
                    else:
                        self.parameters['page[size]'] = str(page_size)
                        self.page_size = page_size
                        break
                except:
                    print('Invalid input. Must be an integer. \nTry again.')
        else:
            print('No page size parameter found.')
            prompt = input('Would you like to add one? (y/n) ')
            while prompt.lower() == 'y':
                try:
                    page_size = int(input('Enter page size (Enter to go back): '))
                    if page_size == '':
                        break
                    else:
                        self.page_size = page_size
                        break
                except:
                    print('Invalid input. Must be an integer. \nTry again.')
            return 

        print(f'Page size changed to {self.parameters["page[size]"]}.', end='\n\n')
    
        
class Treasury(Site):
    def __init__(self, name):
        super().__init__(name)
        self.sub_menu = {
            "Back": 'back',
            "Spending": self.spending_report,
            "Edit": super().edit()
            }
        
    def spending_report(self):
        print("Treasury spending report")