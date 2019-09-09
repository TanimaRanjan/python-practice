"""

- Enter
    a to add a movie,
    1 to see your movies
    f to find a movie
    q to quit

Tasks :
-- Decide where to store movies
-- What is the format of a movie
-- Show the user the main interface and get their input
-- Allow use to add movies
-- Show all the Movies
-- Find a movie
-- Stop running a program

movies = {
    'name': ...,
    'director': ...,
    'year': ...
}


"""

movies = []


def play_game():

    user_input = input('\nEnter a to add a movie, l to list your movies f to find a movie q to quit : ')

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            list_movie()
        elif user_input == 'f':
            find_movie()
        elif user_input == 'q':
            print('Stopping the program')
        else:
            print('Unknown command - please retry : ')
        user_input = input('\nEnter a to add a movie, l to list your movies f to find a movie q to quit : ')


def add_movie():

    name = input('Enter the movie name : ')
    director = input('Enter the movie director : ')
    year = input('Enter the movie release year : ')

    movies.append({
        'name': name,
        'director': director,
        'year': year
    })


def list_movie():

    for movie in movies:
        show_movie(movie)


def show_movie(movie):
    print(f"Name : {movie['name']}  Director : {movie['director']}  Year : {movie['year']}")


def find_movie():

    find_by = input('What do you want to search movie with : ')
    looking_for = input('What are you searching for : ')

    found_movies = find_by_attr(movies, looking_for, lambda x : x[find_by])

    list_movie(found_movies)


def find_by_attr(items, expected, finder):

    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)

    return found


play_game()
