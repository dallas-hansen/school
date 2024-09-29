def calc_toll(hour, is_morning, is_weekend):
    weekday_toll = {1: 6.15,
                    2: 6.15,
                    3: 6.15,
                    4: 6.15,
                    5: 6.15,
                    6: 6.15,
                    7: 7.95,
                    8: 7.95,
                    9: 7.95,
                    10: 6.90,
                    11: 6.90,
                    12: 6.90,
                    13: 6.90,
                    14: 6.90,
                    15: 8.95,
                    16: 8.95,
                    17: 8.95,
                    18: 8.95,
                    19: 8.95,
                    20: 6.40,
                    21: 6.40,
                    22: 6.40,
                    23: 6.40,
                    24: 6.40
                    }
    weekend_toll = {1: 6.05,
                    2: 6.05,
                    3: 6.05,
                    4: 6.05,
                    5: 6.05,
                    6: 6.05,
                    7: 7.15,
                    8: 7.15,
                    9: 7.15,
                    10: 7.15,
                    11: 7.15,
                    12: 7.15,
                    13: 7.15,
                    14: 7.15,
                    15: 7.15,
                    16: 7.15,
                    17: 7.15,
                    18: 7.15,
                    19: 7.15,
                    20: 6.10,
                    21: 6.10,
                    22: 6.10,
                    23: 6.10,
                    24: 6.10
                    }

    if not is_morning:
        hour += 12

    if not is_weekend:
        return weekday_toll[hour]
    else:
        return weekend_toll[hour]


if __name__ == '__main__':
    print(calc_toll(8, True, False))
    print(calc_toll(1, False, False))
    print(calc_toll(3, False, True))
    print(calc_toll(5, True, True))
