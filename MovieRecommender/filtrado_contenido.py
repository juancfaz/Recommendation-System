# filtrado_contenido.py
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def cargar_datos():
    """Cargar datos de películas y calificaciones."""
    movies = pd.read_csv('movies.csv')
    ratings = pd.read_csv('ratings.csv')
    return movies, ratings

def crear_matriz_de_caracteristicas(movies):
    """Crear matriz de características (one-hot) para los géneros de las películas."""
    return movies['genres'].str.get_dummies(sep='|')

def recomendar_peliculas_contenido(user_id, ratings, movies, genres_one_hot, top_n=5):
    """Recomendar películas utilizando filtrado basado en contenido."""
    user_ratings = ratings[ratings['userId'] == user_id]
    rated_movie_ids = user_ratings['movieId'].values
    rated_movies_features = genres_one_hot.loc[genres_one_hot.index.isin(rated_movie_ids)]
    
    # Calcular el perfil del usuario
    user_profile = np.dot(user_ratings['rating'].values, rated_movies_features)
    similarities = cosine_similarity([user_profile], genres_one_hot)
    
    similar_indices = np.argsort(similarities[0])[::-1]
    unseen_movies_indices = [i for i in similar_indices if movies['movieId'].iloc[i] not in rated_movie_ids]
    
    # Obtener las películas recomendadas
    recommended_movie_ids = movies['movieId'].iloc[unseen_movies_indices][:top_n]
    recommended_movies = movies[movies['movieId'].isin(recommended_movie_ids)]
    
    return recommended_movies

def main():
    movies, ratings = cargar_datos()
    genres_one_hot = crear_matriz_de_caracteristicas(movies)

    user_id = 8
    recommended_movies = recomendar_peliculas_contenido(user_id, ratings, movies, genres_one_hot)

    print("Películas recomendadas (Filtrado Basado en Contenido) para el usuario", user_id, ":")
    for movie in recommended_movies['title']:
        print(movie)

if __name__ == "__main__":
    main()