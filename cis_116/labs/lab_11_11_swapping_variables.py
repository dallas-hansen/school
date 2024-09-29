def swap_values(user_val1, user_val2, user_val3, user_val4):
    copy = [user_val1, user_val2, user_val3, user_val4]
    user_val1 = copy[1]
    user_val2 = copy[0]
    user_val3 = copy[3]
    user_val4 = copy[2]
    return user_val1, user_val2, user_val3, user_val4


def main():
    val1 = int(input())
    val2 = int(input())
    val3 = int(input())
    val4 = int(input())

    val1, val2, val3, val4 = swap_values(val1, val2, val3, val4)
    print(val1, val2, val3, val4)


if __name__ == '__main__':
    main()
