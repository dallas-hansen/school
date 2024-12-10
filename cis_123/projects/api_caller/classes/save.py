import pickle
import os
from typing import Any
from decorators import separator

# Loads data from a file
def load_data(filename: str) -> Any: 
    filepath = f'data\{filename}.pkl'
    os.makedirs('data', exist_ok=True)
    
    if os.path.exists(filepath):
        with open(f'{filepath}', 'rb') as file:
            data = pickle.load(file)
            return data
    else:
        with open (f'data\{filename}.pkl', 'wb') as file:
            pickle.dump([], file)
        data = []
        return data

# Saves data to a file
@separator()
def save_data(data: Any, filename: str, message: str = None) -> None:
    with open (f'data\{filename}.pkl', 'wb') as file:
        if message:
            pickle.dump(data, file)
            print(f'{message} saved successfully')
        else:
            print(f'Saving your progress...')
            pickle.dump(data, file)
            print('Saved successfully')