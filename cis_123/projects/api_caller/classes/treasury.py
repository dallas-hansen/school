from classes.api_sites import Api_site
import re
import pandas as pd
from functions.display import display, visualize_data

class Treasury(Api_site):
    def __init__(self, name):
        super().__init__(name)
        self.parameters = {
                'page[size]': '5000',
                'page[number]': '1',
                'sort': None,
                'filter': 'record_date:gte:2023-01-01',
                'format': 'csv'
            }
        self.endpoints = {'Operating Cash':'/v1/accounting/dts/deposits_withdrawals_operating_cash'}
        self.url = 'https://api.fiscaldata.treasury.gov/services/api/fiscal_service'
        self.departments = {}
        self.sub_menu = {
            "View": self.view_data,
            #"Departments": self.view_departments,
            "Search": super().search,
            "Edit": super().edit()
            }
    
    def select_data(self) -> None:
        self.selected_df = display(self.data)
        return
    
    def choose_axis(self, side) -> list:
        axis = []
        while True:
            print(f'What would you like to use as the {side}-axis?')
            columns = {x : x for x in self.selected_df.columns}
            columns['Parent Department'] = self.departments
            choice = display(columns)
            if choice == 'Back':
                return
            axis.append(choice)
            if input('Would you like to add another? (y/n) ').lower() == 'n':
                return axis
            
    
    def view_data(self):
        # Create a bar chart
        if self.selected_df is None:
            if not self.data:
                print('No data found. Please search for data.')
                return
        self.get_departments()
        
        df = self.selected_df.dropna(subset=['transaction_catg'])
        remove = [
            'Sub-Total Deposits',
            'Sub-Total Withdrawals',
            'Public Debt Cash Issues (Table IIIB)',
            'Public Debt Cash Redemp. (Table IIIB)'
            ]
        df = df[~df['transaction_catg'].isin(remove)]
        
        # Create a mapping of sub-departments to parent departments
        sub_to_parent = {sub: parent for parent, sub_departments in self.departments.items() for sub in sub_departments}

        # Add a new column for parent departments
        df['parent_department'] = df['transaction_catg'].map(sub_to_parent)
        
        x_axis = self.choose_axis('x')
        y_axis = self.choose_axis('y')
        visualize_data(self.selected_df, x_axis, y_axis)
        return
    
    def get_departments(self, print=False) -> dict:
        if self.departments:
            if print:
                for k, v in self.departments.items():
                    print(f'{k} - {v}')
            return self.departments
        else:
            data_list = list(self.selected_df['transaction_catg'].dropna().unique())
            departments = {}
            for i in data_list:
                # TODO: Type error Bool is not callable. I think I'm getting a series of bools from data_list
                print(i)
                try:
                    if ' - ' in i:  # Only split if ' - ' is present
                        code, name = i.split(' - ', maxsplit=1)
                        
                        # Check if code is actually in parenthesis
                        match = re.search(r'\((.*?)\)', code)
                        cleaned_text = re.sub(r'\s*\(.*\)', '', code)

                        if match:
                            code = match.group(1)
                            name = cleaned_text
                            
                        if code in departments:
                            departments[code].append(name)
                        else:
                            departments[code] = [name]
                except ValueError:
                    print(f'Value Error: {i}')
                self.departments = departments
            return self.departments