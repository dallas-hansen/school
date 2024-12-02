from classes.api_sites import Api_site
import re

class Treasury(Api_site):
    def __init__(self, name):
        super().__init__(name)
        self.sub_menu = {
            "Back": 'back',
            "Spending": self.spending_report,
            "Departments": self.view_departments,
            "Edit": super().edit()
            }
        
    def spending_report(self):
        print("Treasury spending report")
    
    def view_departments(self):
        data_list = list(self.data.df['transaction_catg'].dropna().unique())
        departments = {}
        for i in data_list:
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
        for k, v in departments.items():
            for i in v:
                print(f'{k} - {i}')