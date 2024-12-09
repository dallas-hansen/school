from classes.save import save_data
from decorators import box_decorator
from functions.display import display
from classes.data import Data
from datetime import datetime

class Api_site():
    def __init__(self, name, menu={}):
        self.name = name.lower()
        self.url = None
        self.endpoints = {}
        self.parameters = {}
        self.main_menu = menu
        self.menu = {} # key = name, value = function
        self.page_size = None
        self.data = {} # key = parameters, value = Dataframe
        self.selected_df = None
    
    @box_decorator
    def list_items(self, input_list: list) -> None:
        return input_list
 
    def search(self) -> Data:
        """Takes in a query and returns the results.
        Checks to see if the query has already been searched.
        If it has, returns the results.
        If it hasn't, searches the API for the query and returns the results."""
        
        # verifies that the parameters are correct, if not, allows user to edit
        self.view_parameters()
        parameters = self.parameters
        # TODO: allow user to edit parameters
        # proceed = input('Are these parameters correct? (y/n)\n').lower()
        # if proceed == 'n':
        #     while True:
        #         print('\nPlease select a parameter to edit.')
        #         parameters = {x : x for x in self.parameters}
        #         key = display(parameters)
        #         if key == 'Back':
        #             break
        #         print('Refer to API documentation for possible values.')
        #         value = input('Enter new value: ')
        #         parameters[key] = value
        #         for key, value in parameters.items():
        #             print(f'{key}: {value}')
        #         proceed = input('Are these parameters correct? (y/n)\n').lower()
        #         if proceed == 'y':
        #             print()
        #             break
        
        # user selects endpoint
        print('Which endpoint would you like to search?')
        endpoint = display(self.endpoints)
        if endpoint == 'Back':
            return
        url = self.url + endpoint
        query = Data(url=url, params=parameters)
        
        # checks to see if data already exists
        for key, item in self.data.items():
            if item.params == query.params and item.url == query.url:
                item.last_accessed = datetime.now()
                print('Data already exists.')
                print(f'Last accessed: {item.last_accessed}')
                print(f'Total entries: {item.df.shape[0]}')
                choice = input('Do you want to use this data? (y/n) ').lower()
                if choice == 'n':
                    break
                print('Using existing data.')
                self.selected_df = item
                return item
        
        print('Searching...')
        query.search()
        print('Search complete.')
        print('Current selection updated.')
        self.selected_df = query.df
        param_str = ''
        for key, item in query.params.items():
            param_str += f'{key}: {item}\n'
        self.data[param_str] = query
        return query
    
    def edit(self) -> dict:
        """
        Creates a menu for editing a site.
        To add more menu options, create the function and add it to the sub_menu dictionary.
        Follow the format shown below. Use nested dictionaries to create sub menus.
        
        Returns: None
        """
        menu = {
            "Change name": self.change_name,
            "Change url": self.change_url,
            "Edit endpoints": {
                "Back": 'back',
                "List endpoints": self.view_endpoints,
                "Add endpoints": self.add_endpoints,
                "Remove endpoints": self.remove_endpoints,
                "Modify endpoints": self.edit_endpoints
                },
            "Edit parameters": {
                "Back": 'back',
                "Auto Search": self.populate_parameters,
                "List parameters": self.view_parameters,
                "Modify parameters": {
                    "Edit parameters": self.edit_parameters,
                    "Add parameters": self.add_parameters,
                    "Remove parameters": self.remove_parameters},
                "Advanced" : {
                    "Back": 'back',
                    "Default page size": self.default_page_size,
                    "Edit page size": self.edit_page_size
                    }
                },
            "Reset": self.reset
            }
        return menu
    
    def not_fully_implemented(self) -> None:
        print('This feature is not fully implemented yet. Changes here may break the code.')
    
    def are_you_sure(self) -> bool:
        while True:
            choice = input('Are you sure you want to continue? (y/n) ').lower()
            try:
                if choice == 'y':
                    return True
                elif choice == 'n':
                    return False
            except:
                print('Invalid input. Try again.')
                continue
    
    def reset(self) -> None:
        print("WARNING: This will reset all changes made to this site.")
        print("You will lose all data associated with this site.")
        if self.are_you_sure():
            self.name = None
            self.url = None
            self.endpoints = {}
            self.parameters = {}
            self.page_size = None
            print("Site reset successfully.", end='\n\n')
        
    def change_name(self) -> None:
        print(f"Current name: {self.name}")
        if self.are_you_sure():
            name = input("Enter new name: ")
            self.name = name.lower()
            self.main_menu[name] = self.name
            print("Name changed successfully.")
        else:
            print("Name not changed.")

    def change_url(self) -> None:
        print(f"Current url: {self.url}")
        if self.are_you_sure():
            new_url = input("Enter new url: ")
            self.url = new_url
            print("URL changed successfully.")
        else:
            print("URL not changed.")
    
    def view_endpoints(self) -> None:
        print(f'\nCurrent endpoints:')
        for endpoint, url in self.endpoints.items():
            print(f'  {endpoint}: {url}')
    
    def view_parameters(self, param=None) -> None:
        print(f'\nCurrent parameters:')
        if not param:
            param = self.parameters
        for parameter, value in param.items():
            print(f'  {parameter}: {value}')
        print()

    def add_endpoints(self) -> None:
        self.view_endpoints()
        
        if self.are_you_sure():
            while True:
                new_endpoint = input("\nEnter name of new endpoint: ")
                new_endpoint_url = input("Enter url of new endpoint: ")
                self.endpoints[new_endpoint] = new_endpoint_url
                print("Endpoint added successfully.")
                choice = input("Do you want to add another endpoint? (y/n) ")
                if choice.lower() == "n":
                    return
        else:
            print("Endpoint not added.")
    
    def remove_endpoints(self) -> None:
        self.view_endpoints()
            
        if self.are_you_sure():    
            while True:
                print('\nList of current endpoints:')
                self.list_items(self.endpoints)
                choice = input('Enter the name of the endpoint you want to remove: ').capitalize()
                if choice in self.endpoints:
                    self.endpoints.pop(choice)
                    print('Endpoint removed successfully.')
                else:
                    print('Endpoint not found.')
                choice = input('Do you want to remove another endpoint? (y/n) ')
                if choice.lower() == "n":
                    return
        else:
            print('Endpoint not removed.')
    
    
    
    def edit_endpoints(self) -> None:
        self.not_fully_implemented()
        print('Which endpoint would you like to edit?')
        
        while True:
            self.view_endpoints()
            endpoint_dict = {x : x for x in self.endpoints}
            endpoint_to_edit = display(endpoint_dict)
            if endpoint_to_edit == 'Back':
                return
            
            if self.are_you_sure():
                # sets endpoint_to_edit to the value of the selected endpoint and removes it from the dictionary
                endpoint_to_edit = endpoint_to_edit.pop(self.endpoints[endpoint_to_edit])
                self.endpoints[endpoint_to_edit] = input('Enter new value: ')
                print('Endpoint modified successfully.')
            choice = input('Do you want to modify another endpoint? (y/n) ')
            if choice.lower() != "y":
                return
    
    # TODO: Add support to select possible parameter options from a list
    def add_parameters(self) -> None:
        self.view_parameters()
        
        if self.are_you_sure():
            while True:
                new_parameter = input("\nEnter new parameter: ")
                parameter_value = input("Enter value of new parameter: ")
                self.parameters[new_parameter] = parameter_value
                print("Parameter added successfully.")
                choice = input("Do you want to add another parameter? (y/n) ")
                if choice.lower() == "n":
                    return
        else:
            print("Parameter not added.")
    
    def remove_parameters(self) -> None:
        self.view_parameters()

        print('Which parameter would you like to remove?')
        
        while True:
            self.view_parameters()
            parameter_dict = {x : x for x in self.parameters}
            parameter_to_edit = display(parameter_dict)
            
            if self.are_you_sure():
                self.parameters.remove(parameter_to_edit)
                print('Parameter removed.')
            choice = input('Do you want to remove another parameter? (y/n) ')
            if choice.lower() != "y":
                return
    
    def edit_parameters(self) -> None:
        self.not_fully_implemented()
        print('Which parameter would you like to edit?')
        
        while True:
            self.view_parameters()
            parameter_dict = {x : x for x in self.parameters}
            parameter_to_edit = display(parameter_dict)
            print(f'you chose {parameter_to_edit}')
            print(self.parameters)
            if parameter_to_edit == 'Back':
                return
            
            if self.are_you_sure():
                
                self.parameters[parameter_to_edit] = input('Enter new value: ')
                print('Parameter modified successfully.')
            choice = input('Do you want to modify another parameter? (y/n) ')
            if choice.lower() != "y":
                return
    
    #TODO: create a way to use the api to populate the parameters
    def populate_parameters(self) -> None:
        print('This feature is not yet implemented.')
    
    def default_page_size(self) -> None:
        self.page_size = None
        print('Page size reset to default.')
    
    #TODO: create max page size feature
    def find_max_page_size(self) -> None:
        print('This feature is not yet implemented.')
        # if not self.page_size:
        #     prompt = input('Do you know the maximum page size that the API allows? (y/n) ')
        #     while prompt.lower() == 'y':
        #         try:
        #             max_page_size = input('Enter the maximum page size (Hit enter to default 100): ')
        #             if max_page_size == '':
        #                 break
        #             else:
        #                 self.page_size = int(max_page_size)
        #                 break
        #         except:
        #             print('Invalid input. Try again.')
    
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