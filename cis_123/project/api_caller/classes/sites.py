import pandas as pd

class Site():
    def __init__(self, name):
        self.name = name
        self.url = None
        self.endpoints = []
        self.parameters = []
        self.menu = {}
    
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
                new_endpoint = input("Enter new endpoint: ")
                self.endpoints.append(new_endpoint)
                print("Endpoint added successfully.")
                choice = input("Do you want to add another endpoint? (y/n) ")
                if choice.lower() == "n":
                    return
        #TODO: Remove endpoints
        def remove_endpoints() -> None:
            print('Not implemented yet')
        
        def add_parameters() -> None:
            while True:
                new_parameter = input("Enter new parameter: ")
                self.parameters.append(new_parameter)
                print("Parameter added successfully.")
                choice = input("Do you want to add another parameter? (y/n) ")
                if choice.lower() == "n":
                    return

        #TODO: Remove parameters
        def remove_parameters() -> None:
            print('Not implemented yet')
            return

        self.menu = {
            "Change name": change_name,
            "Change url": change_url,
            "Add/Remove endpoints": {
                "Add endpoints": add_endpoints,
                "Remove endpoints": remove_endpoints,
                "Back": 'back'
                },
            "Add/Remove parameters": {
                "Add parameters": add_parameters,
                "Remove parameters": remove_parameters,
                "Back": 'back'
                },
            "Back": 'back'
        }
        return self.menu
    
        
class Treasury(Site):
    def __init__(self):
        super().__init__("Treasury")