def word_multiple_finder(strings: list) -> dict:
    # builds dictionary
    word_count_dict = {}
    for i in strings:
        if i not in word_count_dict:
            word_count_dict[i] = 0
        else:
            word_count_dict[i] = 1
    return word_count_dict


def print_dictionary(my_dict):
    sorted_dict = {}
    for key, value in sorted(my_dict.items()):
        if value == 1:
            print(f'{key} - True')
        else:
            print(f'{key} - False')


def main():
    sentence = input().split()
    count = word_multiple_finder(sentence)
    print_dictionary(count)


if __name__ == "__main__":
    main()
