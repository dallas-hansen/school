def int_to_reverse_binary(integer_value):
    binary = ''
    while integer_value > 0:
        binary += str(integer_value % 2)
        integer_value //= 2
    return binary


def string_reverse(input_string):
    r_string = input_string[::-1]
    return r_string


if __name__ == '__main__':
    num = int(input())
    print(string_reverse(int_to_reverse_binary(num)))
