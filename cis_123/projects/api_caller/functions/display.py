import inspect
from dataclasses import is_dataclass
from decorators import box_decorator

def display(menu: dict, return_key=False, title=None) -> str | None:
    """
    Displays the menu and returns the selected option.
    """
    
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
            elif isinstance(selected_value, str):
                if return_key:
                    return selected_option
                else:
                    return selected_value
            elif is_dataclass(selected_value):
                display(selected_value.sub_menu)
            elif inspect.isclass(selected_value):
                display(selected_value.menu)
            else:
                # Directly call the function
                selected_value()
        
        except (ValueError, IndexError):
            print("Invalid choice, try again.")
            
def visualize_data(data: dict) -> None:
    pass