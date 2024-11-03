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
    # Construir el perfil del usuario (movieId, rating)
    user_ratings = ratings[ratings['userId'] == user_id][['movieId', 'rating']]
    
    # Codificar los generos de las películas con el metodo one hot encoding (OHE)
    genres = movies['genres'].str.get_dummies(sep='|')
    
    # Filtrar los géneros solo para las películas que el usuario ha calificado
    rated_movies = movies[movies['movieId'].isin(user_ratings['movieId'])]
    rated_genres = genres.loc[rated_movies.index].values
    
    # Filtrar las calificaciones de las películas que el usuario ha calificado
    ratings = (user_ratings['rating'].values * 2) - 1

    # Calcular el perfil del usuario
    user_profile = rated_genres.T.dot(ratings)
    
    # Ponderacion para llevar los valores a una escala de 0 a 1
    user_profile = user_profile / user_profile.sum()
    
    # Que peliculas no ha visto el usuario
    unseen_movies = movies[~movies['movieId'].isin(user_ratings['movieId'])]
    unrated_genres = genres.loc[unseen_movies.index]
    
    # Multiplicar matriz de perfil de usuario x géneros de películas no calificadas
    scores = unrated_genres.dot(user_profile)
    
    # Retornar las top_n películas recomendadas
    return movies.loc[scores.sort_values(ascending=False).head(top_n).index]

movies, ratings = cargar_datos()

user_id = 5
recommended_movies = recomendar_peliculas_contenido(user_id, ratings, movies, top_n=5)
print("Las películas recomendadas para el usuario {} son:".format(user_id))
print(recommended_movies['title'])