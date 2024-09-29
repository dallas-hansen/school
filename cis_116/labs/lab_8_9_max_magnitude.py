def max_magnitude(user_val1, user_val2, user_val3):
    mag = 0
    vals = [user_val1, user_val2, user_val3]
    for i in vals:
        if abs(i) > abs(mag):
            mag = i
    return mag


if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    print(max_magnitude(num1, num2, num3))
