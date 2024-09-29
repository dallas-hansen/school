def print_menu():
    menu = ('MENU\n'
            'c - Number of non-whitespace characters\n'
            'w - Number of words\n'
            'f - Fix capitalization\n'
            'r - Replace punctuation\n'
            's - Shorten spaces\n'
            'q - Quit\n')
    print(menu)


def user_choice(text):
    options = ['c', 'w', 'f', 'r', 's']
    choice = input('Choose an option:\n')
    while choice != 'q':
        if choice not in options:
            print('Invalid option, choose again:\n')
            print_menu()
            choice = input('Choose an option:\n')
        if choice in options:
            execute_menu(choice, text)
            print_menu()
            choice = input('Choose an option:\n')
    return None


def execute_menu(choice, text):
    choices = {'c': get_num_of_non_WS_characters,
               'w': get_num_of_words,
               'f': fix_capitalization,
               'r': replace_punctuation,
               's': shorten_space
               }
    choices[choice](text)
    return None


def get_num_of_non_WS_characters(text):
    count = 0
    for letter in text:
        if letter != ' ':
            count += 1
    print(f'Number of non-whitespace characters: {count}\n')
    return count


def get_num_of_words(text):
    list_of_words = text.split()
    num_words = len(list_of_words)
    print(f'Number of words: {num_words}\n')
    return num_words


def fix_capitalization(text):
    # This is the most stupid function, they want extra spaces where there shouldn't be any.
    # I give up, this somehow works, so I'm not messing with it.
    count = 0
    new_text = ''
    split_text = text.split('.')
    for sentence in split_text:
        cap = False
        sentence += '.'
        if sentence == '.':
            continue
        for letter in sentence:
            if cap is False and letter != ' ':
                new_text += letter.upper()
                cap = True
                count += 1
            else:
                new_text += letter
    if new_text[-2] == '!':
        new_text = new_text[:-1]
    print(f'Number of letters capitalized: {count}')
    print(f'Edited text: {new_text}\n')
    return new_text, count


def replace_punctuation(text, exclamation_count=0, semicolon_count=0):
    punctuation_to_replace = {'!': '.', ';': ','}
    exclamation_count = 0
    semicolon_count = 0
    edited_text = ''
    for i in text:
        if i == ';':
            semicolon_count += 1
            text.replace(i, punctuation_to_replace[i])
            edited_text += punctuation_to_replace[i]
        elif i == '!':
            exclamation_count += 1
            text.replace(i, punctuation_to_replace[i])
            edited_text += punctuation_to_replace[i]
        else:
            edited_text += i
    print(f'Punctuation replaced')
    print(f'exclamation_count: {exclamation_count}')
    print(f'semicolon_count: {semicolon_count}')
    print(f'Edited text: {edited_text}\n')
    return edited_text


def shorten_space(text):
    space = False
    extra_space_removed_text = ''
    for i in text:
        if i.isspace() and space is False:
            space = True
            extra_space_removed_text += i
        if i.isspace() and space is True:
            continue
        else:
            space = False
            extra_space_removed_text += i
    print(f'Edited text: {extra_space_removed_text}\n')
    return extra_space_removed_text


def main():
    text = input('Enter a sample text:\n\n')
    print(f'You entered: {text}\n')

    print_menu()
    user_choice(text)


if __name__ == '__main__':
    main()
