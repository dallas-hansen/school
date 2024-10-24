from classes import sites, save
from classes.sites import Treasury

def display(menu: dict) -> None:
    while True:
        print("\nChoose an option:")
        options = list(menu.keys())  # Get all the options in the current menu
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        choice = input("\nEnter your choice: ")

        try:
            choice = int(choice) - 1  # Convert to zero-indexed
            selected_option = options[choice]
            selected_value = menu[selected_option]
            
            if selected_option == "Back":
                return
            
            elif selected_option == "Exit":
                break
            
            # If the selected option is a sub-menu (i.e., a dictionary), recurse
            elif isinstance(selected_value, dict):
                display(selected_value)
            else:
                # Directly call the function
                selected_value()
        
        except (ValueError, IndexError):
            print("Invalid choice, try again.")

#TODO: create add API function
# def add_api(api) -> None:
#     name = input('What is the name of the API you would like to add?')
#     name = sites.Site(name)
#     api.append(name)
    
    
#     print('\nWhat would you like to add?\n')
    
#     def add_attributes(attribute: str) -> None:
#         pass
    
#     attributes = {
#         'Back': 'back',
#         'Url': lambda: add_attributes('Url'),
#         'Endpoints': lambda: add_attributes('Endpoints'),
#         'Parameters': lambda: add_attributes('Parameters')
#     }
#     display(attributes)

#TODO: create initializer
# def initialize(api_list, name) -> None:
#     for item in api_list:
#         if item.name == name:
#             return item

def main():
    # api_classes_list = save.load_data("sites")
    treasury = Treasury("Treasury")
    
    menu = {
        "Treasury":{
            "Back": None,
            "Spending": lambda: treasury.spending_report(),
            "Edit": lambda: display(treasury.edit())
            }, 
        # "Add API": lambda: add_api(api_classes_list),
        "Exit": exit
    }
    display(menu)
    # save.save_data(api_classes_list, "sites")

if __name__ == "__main__":
    main()    