# filtrado_contenido.py
import pandas as pd
import numpy as np

def cargar_datos():
    """Cargar datos de películas y calificaciones."""
    movies = pd.read_csv('movies.csv')
    ratings = pd.read_csv('ratings.csv')
    return movies, ratings

def recomendar_peliculas_contenido(user_id, ratings, movies, top_n=5):
    """Recomendar películas utilizando filtrado basado en contenido."""
    user_ratings = ratings[ratings['userId'] == user_id][['movieId', 'rating']]
    
    genres = movies['genres'].str.get_dummies(sep='|')
    
    rated_movies = movies[movies['movieId'].isin(user_ratings['movieId'])]
    rated_genres = genres.loc[rated_movies.index].values
    
    ratings = (user_ratings['rating'].values * 2) - 1

    user_profile = rated_genres.T.dot(ratings)
    
    user_profile = user_profile / user_profile.sum()
    
    unseen_movies = movies[~movies['movieId'].isin(user_ratings['movieId'])]
    unrated_genres = genres.loc[unseen_movies.index]
    
    scores = unrated_genres.dot(user_profile)
    
    return movies.loc[scores.sort_values(ascending=False).head(top_n).index]

movies, ratings = cargar_datos()

user_id = 5
recommended_movies = recomendar_peliculas_contenido(user_id, ratings, movies, top_n=5)
print("Las películas recomendadas para el usuario {} son:".format(user_id))
print(recommended_movies['title'])
