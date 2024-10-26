from classes.sites import Treasury
from classes.save import save_data, load_data

def display(menu: dict) -> None:
    while True:
        print("\nChoose an option:")
        options = list(menu.keys())  # Get all the options in the current menu
        for i, option in enumerate(options, 1):
            print(f"{i}. {option.capitalize()}")
        
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
def initialize_menu(api_class_list) -> dict:
    menu = {}
    # initializes menu
    for site in api_class_list:
        print(site.name)
        menu[site.name.capitalize()] = site.menu
    
    menu["Save"] = lambda: save_data(api_class_list, "sites")
    menu["Exit"] = exit
    return menu

def main():
    api_classes_list = load_data("sites")
    # api_classes_list = []
    # treasury = Treasury("Treasury")
    # api_classes_list.append(treasury)
    
    menu = initialize_menu(api_classes_list)
    
    display(menu)
    save_data(api_classes_list, "sites")

if __name__ == "__main__":
    main()    