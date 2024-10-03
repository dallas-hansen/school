from tabulate import tabulate

def add_rating(reviews: dict) -> dict:
    movie = input('Enter your movie: ').title() # .title() capitalizes the first letter of each word
    rating = float(input('Enter your rating: '))
    
    # Checks if rating is between 0 and 10
    while rating < 0 or rating > 10:
        rating = float(input('Rating needs to be between 0 and 10. Enter your rating: '))
    
    # Checks if movie is in dictionary, adds rating to dictionary    
    if movie in reviews:
        reviews[movie] = (reviews[movie] + rating) / 2
    else:
        reviews[movie] = rating
    return reviews

def remove_rating(reviews: dict) -> dict:
    movie = input('Enter your movie: ').title()
    
    # Checks if movie is in dictionary, removes rating from dictionary
    if movie in reviews.keys():
        del reviews[movie]
    return reviews


def display_ratings(reviews: dict) -> None:
    # Creates a list of movies and ratings
    data = [[movie, rating] for movie, rating in reviews.items()]
    
    # Uses tabulate library to create a pretty table
    print(tabulate(data, headers=['Movie', 'Rating'], tablefmt='fancy_grid'))
    
    # for movie, rating in reviews.items():
    #     print(f'The movie: {movie} is rated: {rating}')
    

def main():
    # Test movie-rating pairs
    movies_ratings = {
    "Inception": 9.0,
    "The Dark Knight": 9.1,
    "Interstellar": 8.6,
    "The Matrix": 8.7,
    "Parasite": 8.6,
    "Forrest Gump": 8.8,
    "The Godfather": 9.2,
    "Pulp Fiction": 8.9
}

    menu = '''
    1. Add a rating
    2. Remove a rating
    3. Display all ratings
    4. Exit
    '''
    
    # Main loop for menu
    while True:
        print(menu)
        choice = int(input('Enter your choice: '))
        if choice == 1:
            movies_ratings = add_rating(movies_ratings)
        elif choice == 2:
            movies_ratings = remove_rating(movies_ratings)
        elif choice == 3:
            display_ratings(movies_ratings)
        elif choice == 4:
            break


if __name__ == "__main__":
    main()