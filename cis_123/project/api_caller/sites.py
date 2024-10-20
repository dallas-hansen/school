import pickle

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
    
    def set_level(self, level) -> None:
        self.level = level
    
    def add_endpoints(self, endpoints) -> None:
        name = input('Enter endpoint name: ')
        url = input('Enter endpoint url: ')
        self.endpoints = endpoints

    def add_parameters(self, parameters) -> None:
        name = input('Enter parameter name: ')
        self.parameters.append(parameters)
    
    def del_endpoint(self) -> None:
        name = input('Enter endpoint name: ')
        self.endpoints.pop(name)

    def del_parameter(self) -> None:
        name = input('Enter parameter name: ')
        self.parameters.pop(name)
    
    def list_endpoints(self) -> None:
        for name in self.endpoints:
            print(f'{name}')

    def list_parameters(self) -> None:
        for name in self.parameters:
            print(f'{name}')
            
    def save(self) -> None:
        with open(self.name, 'wb') as f:
            pickle.dump(self, f)
    
    def load(self) -> None:
        with open(self.name, 'rb') as f:
            return pickle.load(f)