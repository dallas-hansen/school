
def add_rating(reviews: dict) -> dict:
    movie = input('Enter your movie: ')
    rating = int(input('Enter your rating: '))
    
    while rating < 0 or rating > 10:
        rating = int(input('Rating needs to be between 0 and 10. Enter your rating: '))
        
    if movie in reviews:
        reviews[movie] = (reviews[movie] + rating) / 2
    else:
        reviews[movie] = rating
    return reviews

def remove_rating(reviews: dict) -> dict:
    movie = input('Enter your movie: ')
    if movie in reviews.keys():
        del reviews[movie]
    return reviews


def display_ratings(reviews: dict) -> None:
    for movie, rating in reviews.items():
        print(f'The movie: {movie} is rated: {rating}')
    

def main():
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