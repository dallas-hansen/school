from decorators import box_decorator


@box_decorator
def list_items(input_list) -> None:
    return input_list

list_items(['a', 'boeuoe', 'c'])
