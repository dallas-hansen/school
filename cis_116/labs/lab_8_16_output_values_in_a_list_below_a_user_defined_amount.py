def get_user_values():
    index = int(input())
    tmp = []
    for i in range(index):
        tmp.append(int(input()))
    threshold = int(input())
    return tmp, threshold


def ints_less_than_or_equal_to_threshold(user_values, upper_threshold):
    vals = []
    for i in user_values:
        if i <= upper_threshold:
            vals.append(i)
    return vals


if __name__ == '__main__':
    user_values, upper_threshold = get_user_values()
    res_values = ints_less_than_or_equal_to_threshold(user_values, upper_threshold)

    for value in res_values:
        print(value)
