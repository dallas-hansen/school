def print_menu():
    menu = ('MENU\n'
            'a - Add player\n'
            'd - Remove player\n'
            'u - Update player rating\n'
            'r - Output players above a rating\n'
            't - Output top player\n'
            'o - Output roster\n'
            'q - Quit\n')
    print(menu)


def user_choice(roster):
    options = ['a', 'd', 'u', 'r', 't', 'o']
    choice = input('Choose an option:\n')
    while choice != 'q':
        if choice not in options:
            print('Invalid option, choose again:\n')
            print_menu()
            choice = input('Choose an option:\n')
        if choice in options:
            execute_menu(choice, roster)
            print_menu()
            choice = input('Choose an option:\n')
    return None


def execute_menu(choice, roster):
    choices = {'a': add_player,
               'd': remove_player,
               'u': update_player_rating,
               'r': output_players_above_a_rating,
               't': output_top_player,
               'o': output_roster
               }
    choices[choice](roster)
    return None


def add_player(roster):
    jersey = int(input(f"Enter a new player's jersey number: \n"))
    rating = int(input(f"Enter the player's rating: \n"))
    print()
    roster[jersey] = roster.get(jersey, rating)


def remove_player(roster):
    roster.pop(int(input('Enter a jersey number: \n')))
    print()


def update_player_rating(roster):
    jersey = int(input('Enter a jersey number: \n'))
    rating = int(input('Enter a new rating for player: \n'))
    print()
    roster[jersey] = rating


def output_players_above_a_rating(roster):
    rating = int(input('Enter a rating: \n'))
    print(f'ABOVE {rating}')
    for i in sorted(roster):
        if roster[i] > rating:
            print(f'Jersey number: {i}, Rating: {roster[i]}')
    print()


def output_top_player(roster):
    for key, value in roster.items():
        if value == max(roster.values()):
            print(f'TOP PLAYER: Jersey number: {key}, Rating: {value}\n')


def output_roster(roster):
    print('ROSTER')
    for i in sorted(roster):
        print(f'Jersey number: {i}, Rating: {roster[i]}')
    print()


def main():
    roster = {}
    for i in range(5):
        jersey = int(input(f"Enter player {i + 1}'s jersey number:\n"))
        rating = int(input(f"Enter player {i + 1}'s rating:\n"))
        print()
        roster[jersey] = roster.get(jersey, rating)
    output_roster(roster)
    print_menu()
    user_choice(roster)


if __name__ == '__main__':
    main()
