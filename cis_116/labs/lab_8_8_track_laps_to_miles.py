def laps_to_miles(loops):
    return loops / 4


if __name__ == '__main__':
    laps = float(input())
    print(f'{laps_to_miles(laps):.2f}')
