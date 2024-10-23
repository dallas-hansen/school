import pandas as pd

class Site():
    def __init__(self, name):
        self.name = name
        self.url = None
        self.endpoints = []
        self.parameters = []

class Treasury(Site):
    def __init__(self):
        super().__init__("Treasury")