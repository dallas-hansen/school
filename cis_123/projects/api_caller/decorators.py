# creates a separator around a function
def separator(symbol='-', length=50) -> None:
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f'{symbol * length}')
            result = func(*args, **kwargs)
            return result
        return wrapper 
    return decorator

# creates a box around a function
def box_decorator(func):
    def wrapper(*args, **kwargs):
        # Call the original function and get the list of items
        items = func(*args, **kwargs)

        # Find the longest item in the list
        if isinstance(items, dict):
            max_length = max(len(key) for key in items.keys())
        else:
            max_length = max(len(item) for item in items)
        box_width = max_length + 2  # Add padding on each side

        print()
        # Top of box
        print('+' + '-' * box_width + '+')

        # Print each item inside the box
        for item in items:
            print(f'| {item.ljust(max_length)} |')

        # Bottom
        print('+' + '-' * box_width + '+')
        print()

    return wrapper