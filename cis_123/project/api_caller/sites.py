from save import *
from menu import *

class Site:
    def __init__(self, name) -> None:
        self.name = name
        self.url = ''
        self.level = None
        self.endpoints = {}
        self.parameters = []
        self.data = {}

    def set_url(self, url) -> None:
        self.url = url
    
    def set_level(self) -> None:
        level = input('Enter level: ')
        self.level = level
    
    def add_endpoints(self) -> None:
        name = input('Enter endpoint name: ')
        url = input('Enter endpoint url: ')
        self.endpoints[name] = url

    def add_parameters(self) -> None:
        name = input('Enter parameter name: ')
        self.parameters.append(name)
    
    def del_endpoint(self) -> None:
        name = input('Enter endpoint name: ')
        self.endpoints.pop(name)

    def del_parameter(self) -> None:
        name = input('Enter parameter name: ')
        self.parameters.pop(name)
    
    def list_endpoints(self) -> None:
        for name in self.endpoints:
            print(f'{name.capitalize()}')

    def list_parameters(self) -> None:
        for name in self.parameters:
            print(f'{name.capitalize()}')
    
    def menu(self) -> None:
        menu ={'List Endpoints': self.list_endpoints,
               'Add Endpoint': self.add_endpoints,
               'Delete Endpoint': self.del_endpoint,
               'Save': 'save'}
        return menu
    
    def main(self) -> None:
        sites = load_data('sites')
        choice = make_menu(self.menu())
        while choice.lower() != 'back' and choice.lower() != 'save':
            self.menu()[choice]()
            choice = make_menu(self.menu())
        if choice.lower() == 'save':
            save_data(sites, 'sites')