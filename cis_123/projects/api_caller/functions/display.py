import inspect
from dataclasses import is_dataclass
from sys import exception
from decorators import box_decorator
import pandas as pd
import matplotlib.pyplot as plt

def display(original_menu: dict, return_key=False, root=False, key_only=True) -> str | None:
    """
    Displays the menu and returns the selected option.
    """
    if not root:
        back = {'Back': 'back'}
        combined_data = back | original_menu
        
    else:
        combined_data = original_menu
        combined_data['Exit'] = 'exit'
    menu = combined_data
    
    while True:
        print("\nChoose an option:")
        options = list(menu.keys())  # Get all the options in the current menu
        
        max_key_length = max(len(key) for key in options)
        
        if key_only:
            for i, option in enumerate(menu.keys(), 1):
                print(f"{i}. {option.capitalize().ljust(max_key_length)}")
        else:
            for i, option in enumerate(menu.keys(), 1):
                print(f"{i}. {option.capitalize().ljust(max_key_length)}: {menu[option]}")
        
        choice = input("\nEnter your choice: ")

        try:
            choice = int(choice) - 1  # Convert to zero-indexed
            selected_option = options[choice]
            selected_value = menu[selected_option]
            
            if selected_option == "Back":
                return "Back"
            
            elif selected_option == "Exit":
                return "Exit"
            
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
        
        except ValueError as e:
            print("Invalid choice. Please enter a number.")
            
def visualize_data(df: pd.DataFrame, x_axis: list, y_axis: list) -> None:
    color_mapping = {'Deposits': 'green', 'Withdrawals': 'red'}
    df['color'] = df['transaction_type'].map(color_mapping).fillna('gray')

    # Group by parent department and sum the amounts
    grouped_df = df.groupby(x_axis, as_index=False)[y_axis].sum()

    # Assign colors for the grouped data
    grouped_df['color'] = grouped_df['transaction_type'].map(color_mapping)

    
    
    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.bar(grouped_df['parent_department'], grouped_df[y_axis], color=grouped_df['color'])
    plt.xlabel('Parent Department')
    plt.ylabel('Total FYTD Amount')
    plt.title('Total FYTD Amount by Parent Department')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()