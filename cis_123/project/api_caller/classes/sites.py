from classes.save import *
from classes.menu import *
from decorators import separator

class Site:
    def __init__(self, name) -> None:
        self.name = name
        self.url = ''
        self.level = None
        self.endpoints = {}
        self.parameters = []
        self.data = {}
        self.menu = {'List Endpoints': self.list_endpoints,
                     'Add Endpoint': self.add_endpoints,
                     'Delete Endpoint': self.del_endpoint,
                     'Save': 'save'}

    def set_url(self, url) -> None:
        self.url = url
    
    def set_level(self) -> None:
        level = input('Enter level: ')
        self.level = level
    
    # Endpoints
    def add_endpoints(self) -> None:
        name = input('Enter endpoint name: ')
        url = input('Enter endpoint url: ')
        self.endpoints[name] = url
        
    def del_endpoint(self) -> None:
        name = input('Enter endpoint name: ')
        self.endpoints.pop(name)
    
    def list_endpoints(self) -> None:
        for name in self.endpoints:
            print(f'{name.capitalize()}')
            
    # Parameters
    def add_parameters(self) -> None:
        name = input('Enter parameter name: ')
        self.parameters.append(name)
    
    def del_parameter(self) -> None:
        name = input('Enter parameter name: ')
        self.parameters.pop(name)

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

class MainMenu(Site):
    def __init__(self) -> None:
        super().__init__('Main Menu')
        self.name = 'Main Menu'
        self.menu = {'List Sites': self.list_sites,
                     'Add Site': self.add_site,
                     'Delete Site': self.delete_site,
                     'Choose Site': self.choose_site}

    def main(self) -> None:
        pass

    def menu(self) -> None:
        pass
    
    # Site menu options
    @separator()
    def list_sites(self, sites: list) -> None:
        print('Sites:')
        for site in sites:
            print(f'{site.name.capitalize()}')

    @separator()
    def add_site(self, sites: list, name=None) -> None:
        if name is None:
            name = input('Enter site name: ').lower()
        name = Site(name)
        sites.append(name)
        
    def delete_site(self, sites: list) -> None:
        self.list_sites(sites)
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
            
    def choose_site(self, sites: list) -> Site:
        self.list_sites(sites)
        print()
        name = input('Enter site name: ').lower()
        for site in sites:
            if site.name.lower() == name:
                name = site
                return name
        else:
            return print('Site not found') 