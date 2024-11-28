from classes.sites import Treasury, Site
from classes.save import save_data, load_data
from functions.display import display

#TODO: create add API function
def add_api(api) -> None:
    print('This feature is not yet: implemented.')

def initialize_menu(api_class_list) -> dict:
    menu = {}
    # initializes menu
    for site in api_class_list:
        menu[site.name.capitalize()] = site.menu
    
    menu["Add"] = lambda: add_api(menu)
    menu["Save"] = lambda: save_data(api_class_list, "sites")
    menu["Exit"] = exit
    return menu

def main():
    api_classes_list = load_data("sites")
    
    menu = initialize_menu(api_classes_list)
    
    display(menu)
    save_data(api_classes_list, "sites")

if __name__ == "__main__":
    main()    