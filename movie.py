from imdb import IMDb
import random

def suggest_movie(mood):
    ia = IMDb()
    genres = {'action': 'action', 'comedy': 'comedy', 'drama': 'drama', 'romance': 'romance', 'horror': 'horror'}
    mood_genre = genres[mood.lower()]
    results = ia.get_keyword(mood_genre)
    movies = []
    for result in results:
        movie = ia.get_movie(result.movieID)
        if 'year' in movie:
            if movie['kind'] == 'movie' and movie['year'] >= 2000:
                movies.append(movie)
    if movies:
        random.shuffle(movies)
        return movies[0]
    else:
        return None

mood = input("What mood are you in? ")
movie = suggest_movie(mood)
if movie:
    print(f"Here's a movie suggestion for your {mood} mood: {movie['title']} ({movie['year']})")
else:
    print("Sorry, no movie suggestions for that mood.")
