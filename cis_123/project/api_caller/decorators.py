def separator(symbol='-', length=50) -> None:
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f'{symbol * length}')
            result = func(*args, **kwargs)
            return result
        return wrapper 
    return decorator