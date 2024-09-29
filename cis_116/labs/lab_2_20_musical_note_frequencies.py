def freq(n):
    """
    Prints frequency r ** n
    """
    r = pow(2, (1 / 12))
    value = initial * pow(r, n)
    print(f'{value:.2f} Hz')


if __name__ == '__main__':
    initial = int(input())
    freq(0)
    freq(1)
    freq(2)
    freq(3)
