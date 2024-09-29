def get_num_of_characters(words):
    return len(words)


def output_without_whitespace(words):
    return ''.join(words.split())


if __name__ == '__main__':
    phrase = input('Enter a sentence or phrase:\n')
    print(f'\nYou entered: {phrase}\n')

    print(f'Number of characters: {get_num_of_characters(phrase)}')
    print(f'String with no whitespace: {output_without_whitespace(phrase)}')
