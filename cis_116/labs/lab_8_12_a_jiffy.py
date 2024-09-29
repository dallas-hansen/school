def jiffies_to_seconds(jif):
    seconds = jif / 100
    return seconds


if __name__ == '__main__':
    jiffy = float(input())
    print(f'{jiffies_to_seconds(jiffy):.3f}')
