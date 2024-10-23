import pandas as pd

class Site():
    def __init__(self, name):
        self.name = name
        self.url = None
        self.endpoints = []
        self.parameters = []
    
    def edit(self):
        pass

class Treasury(Site):
    def __init__(self):
        super().__init__("Treasury")