def is_list_mult10(nums: list):
    for num in nums:
        if num % 10 == 0:
            continue
        else:
            return False
    return True


def is_list_no_mult10(nums: list):
    for num in nums:
        if num % 10 != 0:
            continue
        else:
            return False
    return True


if __name__ == '__main__':
    list_length = int(input())
    int_list = []

    # Adds integers to list
    for i in range(list_length):
        int_list.append(int(input()))

    if is_list_mult10(int_list):
        print('all multiples of 10')
    elif is_list_no_mult10(int_list):
        print('no multiples of 10')
    else:
        print('mixed values')
