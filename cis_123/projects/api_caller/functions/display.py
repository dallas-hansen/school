import inspect
from dataclasses import is_dataclass
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from dataclasses import is_dataclass
import inspect

def display(original_menu: dict, return_key=False, root=False, key_only=True) -> str | None:
    """
    Displays the menu and returns the selected option.
    """
    # Add 'Back' or 'Exit' as needed
    if not root:
        menu = {"Back": "back", **original_menu}
    else:
        menu = {**original_menu, "Exit": "exit"}
    
    while True:
        print("\nChoose an option:")
        options = list(menu.keys())  # Get all the options in the current menu
        max_key_length = max(len(key) for key in options)  # For alignment

        # Display the menu
        for i, option in enumerate(options, 1):
            description = menu[option] if not key_only else ""
            print(f"{i}. {option.capitalize().ljust(max_key_length)} {description}")

        # Handle user input
        choice = input("\nEnter your choice: ").strip()

        try:
            # Convert choice to zero-indexed integer
            choice = int(choice) - 1
            selected_option = options[choice]
            selected_value = menu[selected_option]

            # Handle special cases
            if selected_option in {"Back", "Exit"}:
                return selected_option

            # Handle sub-menus
            if isinstance(selected_value, dict):
                display(selected_value, return_key=return_key, root=False, key_only=key_only)
            elif is_dataclass(selected_value):
                display(selected_value.sub_menu, return_key=return_key, root=False, key_only=key_only)
            elif inspect.isclass(selected_value):
                display(selected_value.menu, return_key=return_key, root=False, key_only=key_only)

            # Return or execute the selected value
            elif callable(selected_value):
                selected_value()  # Call the function
            elif return_key:
                return selected_option
            else:
                return selected_value

        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number.")

            
def visualize_data(df: pd.DataFrame, x_axis: list, y_axis: str, y_axis_label=None) -> None:
    color_mapping = {'Deposits': 'green', 'Withdrawals': 'red'}
    df['color'] = df['transaction_type'].map(color_mapping).fillna('gray')

    # Adjust withdrawals to be negative
    df.loc[df['transaction_type'] == 'Withdrawals', y_axis] *= -1

    # Group by parent department and sum the amounts
    grouped_df = df.groupby(x_axis, as_index=False)[y_axis].sum()

    # Assign colors for the grouped data
    grouped_df['color'] = grouped_df['transaction_type'].map(color_mapping)

    # Plot the results
    plt.figure(figsize=(10, 6))
    bars = plt.bar(grouped_df['parent_department'], grouped_df[y_axis], color=grouped_df['color'])
    plt.xlabel('Department')
    plt.ylabel(f'Total {y_axis_label.lower()} amount (USD)')

    # Add title
    plt.title(f'Previous {y_axis_label.capitalize()} by Parent Department')

    # Custom tick formatting for the y-axis (dynamic scaling based on values)
    def format_ticks(value, tick_number):
        if value >= 1e9:  # Billions
            return f'${value / 1e9:.1f}B'
        elif value >= 1e6:  # Millions
            return f'${value / 1e6:.1f}M'
        elif value >= 1e3:  # Thousands
            return f'${value / 1e3:.1f}K'
        else:
            return f'${value:.1f}'

    # Apply the custom tick formatting to the y-axis
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(format_ticks))

    # Add a legend for the color mapping
    legend_elements = [
        plt.Line2D([0], [0], color='green', lw=4, label='Deposits'),
        plt.Line2D([0], [0], color='red', lw=4, label='Withdrawals')
    ]
    plt.legend(handles=legend_elements, loc='upper center')

    # Rotate x-axis labels and adjust layout for readability
    plt.xticks(rotation=45, ha='right')
    plt.axhline(0, color='black', linewidth=0.8)  # Add x-axis at y=0 for clarity
    plt.tight_layout()

    # Show the plot
    plt.show()

    return