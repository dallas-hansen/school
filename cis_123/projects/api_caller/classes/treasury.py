from classes.api_sites import Api_site
import re
import pandas as pd

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
            "Back": 'back',
            "Spending": self.spending_report,
            "Departments": self.view_departments,
            "Search": super().search,
            "Edit": super().edit()
            }
     
    def spending_report(self):
        print("Treasury spending report")
    
    def view_departments(self):
        if self.departments:
            for k, v in self.departments.items():
                print(f'{k} - {v}')
            return
        else:
            print('Search required...')
            return
        
        # data_list = list(self.data.df['transaction_catg'].dropna().unique())
        # departments = {}
        # for i in data_list:
        #     print(i)
        #     try:
        #         if ' - ' in i:  # Only split if ' - ' is present
        #             code, name = i.split(' - ', maxsplit=1)
                    
        #             # Check if code is actually in parenthesis
        #             match = re.search(r'\((.*?)\)', code)
        #             cleaned_text = re.sub(r'\s*\(.*\)', '', code)

        #             if match:
        #                 code = match.group(1)
        #                 name = cleaned_text
                        
        #             if code in departments:
        #                 departments[code].append(name)
        #             else:
        #                 departments[code] = [name]
        #     except ValueError:
        #         print(f'Value Error: {i}')