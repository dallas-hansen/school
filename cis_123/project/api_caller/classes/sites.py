import pandas as pd
from decorators import box_decorator

class Site():
    def __init__(self, name):
        self.name = name
        self.url = None
        self.endpoints = {}
        self.parameters = []
        self.menu = {}
    
    @box_decorator
    def list_items(self, input_list: list) -> None:
        return input_list
    
    def edit(self):
        def change_name() -> None:
            new_name = input("Enter new name: ")
            self.name = new_name
            print("Name changed successfully.")

        def change_url() -> None:
            new_url = input("Enter new url: ")
            self.url = new_url
            print("URL changed successfully.")

        def add_endpoints() -> None:
            while True:
                new_endpoint = input("\nEnter name of new endpoint: ")
                new_endpoint_url = input("Enter url of new endpoint: ")
                self.endpoints[new_endpoint] = new_endpoint_url
                print("Endpoint added successfully.")
                choice = input("Do you want to add another endpoint? (y/n) ")
                if choice.lower() == "n":
                    return
        
        def remove_endpoints() -> None:
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
        
        def add_parameters() -> None:
            while True:
                new_parameter = input("\nEnter new parameter: ")
                self.parameters.append(new_parameter)
                print("Parameter added successfully.")
                choice = input("Do you want to add another parameter? (y/n) ")
                if choice.lower() == "n":
                    return
        
        def remove_parameters() -> None:
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

        self.menu = {
            "Back": 'back',
            "Change name": change_name,
            "Change url": change_url,
            "Add/Remove endpoints": {
                "Back": 'back',
                "Add endpoints": add_endpoints,
                "Remove endpoints": remove_endpoints
                },
            "Add/Remove parameters": {
                "Back": 'back',
                "Add parameters": add_parameters,
                "Remove parameters": remove_parameters
                }
        }
        return self.menu
    
        
class Treasury(Site):
    def __init__(self, name):
        super().__init__(name)
        
    def spending_report(self):
        print("Treasury spending report")