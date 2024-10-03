def build_dictionary(words: list) -> dict:
    count = {}
    for i in words:
        count[i] = count.get(i, 0) + 1
    return count


def main():
    words = input().split()
    your_dictionary = build_dictionary(words)
    sorted_keys = sorted(your_dictionary.keys())
    for key in sorted_keys:
        print(f'{key} - {str(your_dictionary[key])}') 


if __name__ == '__main__':
    main()
