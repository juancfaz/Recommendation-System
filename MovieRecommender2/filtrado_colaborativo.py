import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def cargar_datos():
    """Cargar datos de películas y calificaciones."""
    movies = pd.read_csv('movies.csv')
    ratings = pd.read_csv('ratings.csv')
    return movies, ratings

def crear_matriz_usuario_pelicula(ratings):
    """Crear matriz de usuario-película a partir de las calificaciones."""
    return ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)

def recomendar_peliculas_colaborativas(user_id, user_movie_matrix, user_similarity, movies, top_n=5):
    """Recomendar películas utilizando filtrado colaborativo."""
    user_similarities = user_similarity[user_id - 1]
    similar_users_indices = np.argsort(user_similarities)[::-1][1:]  # Excluir al propio usuario
    similar_users_ratings = user_movie_matrix.iloc[similar_users_indices]
    
    # Calcular calificación predicha
    predicted_ratings = similar_users_ratings.mean(axis=0)
    unrated_movies = user_movie_matrix.iloc[user_id - 1] == 0
    predicted_ratings = predicted_ratings[unrated_movies]
    
    # Ordenar y obtener películas recomendadas
    recommended_movie_ids = predicted_ratings.sort_values(ascending=False).index.tolist()
    recommended_movies = movies[movies['movieId'].isin(recommended_movie_ids)].iloc[:top_n]['title'].tolist()
    
    return recommended_movies

def main():
    movies, ratings = cargar_datos()
    user_movie_matrix = crear_matriz_usuario_pelicula(ratings)
    user_similarity = cosine_similarity(user_movie_matrix)

    user_id = 8
    recommended_movies = recomendar_peliculas_colaborativas(user_id, user_movie_matrix, user_similarity, movies)

    print("Películas recomendadas (Filtrado Colaborativo) para el usuario", user_id, ":")
    for movie in recommended_movies:
        print(movie)

if __name__ == "__main__":
    main()
