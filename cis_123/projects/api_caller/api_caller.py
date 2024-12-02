from classes.api_sites import Api_site
from classes.treasury import Treasury
from classes.save import save_data, load_data
from functions.display import display

#TODO: create add API function
def add_api(api) -> None:
    print('This feature is not yet: implemented.')

def initialize_menu(api_class_list) -> dict:
    menu = {}
    # initializes menu
    for site in api_class_list:
        menu[site.name.capitalize()] = site.sub_menu
    
    menu["Add"] = lambda: add_api(menu)
    menu["Save"] = lambda: save_data(api_class_list, "sites")
    menu["Exit"] = exit
    return menu

def main():
    # TODO: Add support for more APIs
    # api_classes_list = load_data("sites")
    treasury = Treasury("treasury")
    api_classes_list = [treasury]
    
    menu = initialize_menu(api_classes_list)
    
    display(menu)
    save_data(api_classes_list, "sites")

if __name__ == "__main__":
    main()    