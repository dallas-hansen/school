import os
import sys
import requests
import pandas as pd
import xml.etree.ElementTree as ET
from io import StringIO
from datetime import datetime
from dataclasses import dataclass, field

# Was necessary for use in jupyter notebooks, might not be needed anymore
parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
sys.path.append(parent_dir)


@dataclass
class Data:
    url: str
    df: pd.DataFrame = None
    last_accessed: datetime = None
    params: dict = field(default_factory=dict)
    
    def __post_init__(self):
        """
        Initialize the sub_menu dictionary.
        To add more menu options, create the function and add it to the sub_menu dictionary.
        Follow the format shown below. Use nested dictionaries to create sub menus.
        """
        self.sub_menu = {
            "Data": {
                "Back": 'back',
                "View size": self.view_data_size
            },
            "Search": self.search
        }
    
    def json_to_df(self, response) -> pd.DataFrame:
        "Takes JSON as input and adds it to the dataframe"
        
        json_data = response.json().get('data', [])
        df = pd.DataFrame(json_data)
        self.df = pd.concat([self.df, df], ignore_index=True)
    
    def csv_to_df(self, response) -> pd.DataFrame:
        "Takes CSV as input and adds it to the dataframe"
        
        df = pd.read_csv(StringIO(response.content.decode('utf-8')))
        self.df = pd.concat([self.df, df], ignore_index=True)
    
    def xml_to_df(self, response) -> pd.DataFrame:
        "Takes XML as input and adds it to the dataframe"
        
        root = ET.fromstring(response.content)
        data = [{subchild.tag: subchild.text for subchild in child} for child in root]
        df = pd.DataFrame(data)
        self.df = pd.concat([self.df, df], ignore_index=True)
    
    def search(self) -> pd.DataFrame:
        """
        Fetches all data from the API by handling pagination (The amount of data returned at one time).
        """
        while True:
            # Make the request to the API
            response = requests.get(self.url, params=self.params)

            # Check if the request was successful
            if response.status_code != 200:
                break
            
            # Finds out if the content type is JSON, CSV, or XML
            content_type = response.headers.get('Content-Type').split(';')[0].strip().split('/')[1]
            
            match content_type:
                case 'json':
                    self.json_to_df(response)
                case 'csv':
                    self.csv_to_df(response)
                case 'xml':
                    self.xml_to_df(response)
                case _:
                    print(f'Unknown content type: {content_type}')
            
            print(f'Total entries so far({content_type}): {len(self.df)}')

            # Increment the page number for the next request
            self.params['page[number]'] = str(int(self.params['page[number]']) + 1)
        self.params['page[number]'] = '1'

        return
    
    def view_data_size(self):
        print(f'Total entries in dataset: {self.df.shape[0]}')