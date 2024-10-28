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
            elif isinstance(selected_value, str):
                return selected_value
            else:
                # Directly call the function
                selected_value()
        
        except (ValueError, IndexError):
            print("Invalid choice, try again.")