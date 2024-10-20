import pickle
import os
from typing import Any
from decorators import separator

def load_data(filename: str) -> Any: 
    filepath = f'data\{filename}.pkl'
    if os.path.exists(filepath):
        with open(f'{filepath}', 'rb') as file:
            data = pickle.load(file)
            return data
    else:
        data = []
        return data

@separator()
def save_data(data: Any, filename: str) -> None:
    with open (f'data\{filename}.pkl', 'wb') as file:
        print(f'Saving your progress...')
        pickle.dump(data, file)
        print('Saved successfully')