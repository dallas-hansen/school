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
        """
        Selects data from the API.
        """
        self.selected_df = display(self.data)
        return
    
    def view_data(self):
        """
        Displays the data. Has user select time frame to use.
        """
        
        # If no data has been searched, return
        if self.selected_df is None:
            if not self.data:
                print('No data found. Please search for data.')
                return
        self.get_departments()
        
        # Clean the data
        df = self.clean_data(self.selected_df)
        
        choices = {
            'Day': 'transaction_today_amt',
            'Month': 'transaction_mtd_amt',
            'Year': 'transaction_fytd_amt'
        }
        x_axis = ['parent_department', 'transaction_type']
        
        # Choose the y-axis
        print(f'\nWhat would you like to use as the y-axis?')
        y_axis_label = display(choices, return_key=True)
        chosen_y_axis = choices[y_axis_label]
        if y_axis_label == 'Back':
            return
        print('Visualizing data...')
        
        # Visualize the data
        visualize_data(df, x_axis, chosen_y_axis, y_axis_label)
        return
    
    def clean_data(self, original_df: pd.DataFrame) -> pd.DataFrame:
        """
        Removes unwanted rows from the data that are irrelevant.
        """
        df = original_df.dropna(subset=['transaction_catg'])
        remove = [
            'Sub-Total Deposits',
            'Sub-Total Withdrawals',
            'Public Debt Cash Issues (Table IIIB)',
            'Public Debt Cash Redemp. (Table IIIB)'
        ]
        
        # Remove unwanted rows
        df = df[~df['transaction_catg'].isin(remove)]
        
        # Create a mapping of sub-departments to parent departments
        sub_to_parent = {f'{parent} - {sub}': parent for parent, sub_departments in self.departments.items() for sub in sub_departments}
        
        # Add a new column for parent departments
        df['parent_department'] = df['transaction_catg'].map(sub_to_parent)
        
        # Create a mapping of sub-departments to parent departments
        sub_to_parent = {f'{parent} - {sub}': parent for parent, sub_departments in self.departments.items() for sub in sub_departments}

        # Add a new column for parent departments
        df['parent_department'] = df['transaction_catg'].map(sub_to_parent)
        return df
    
    def get_departments(self, print_departments=False) -> dict:
        """
        Combs through the data and creates a dictionary of parent departments and their sub-departments.
        """
        # If print_departments is True, print the departments
        if self.departments:
            if print_departments:
                for k, v in self.departments.items():
                    print(f'{k} - {v}')
            return self.departments
        else:
            # If departments have not been created, create them
            data_list = list(self.selected_df['transaction_catg'].dropna().unique())
            departments = {}
            for i in data_list:
                try:
                    if ' - ' in i:  # Only split if ' - ' is present
                        code, name = i.split(' - ', maxsplit=1)
                        
                        # Check if code is actually in parenthesis using regex
                        match = re.search(r'\((.*?)\)', code)
                        cleaned_text = re.sub(r'\s*\(.*\)', '', code)

                        if match:
                            code = match.group(1)
                            name = cleaned_text
                            
                        if code in departments:
                            departments[code].append(name)
                        else:
                            departments[code] = [name]
                # Catch ValueError            
                except ValueError:
                    print(f'Value Error: {i}')
            self.departments = departments
            return self.departments