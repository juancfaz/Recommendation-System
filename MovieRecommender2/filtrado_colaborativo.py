import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def cargar_datos():
    """Cargar datos de películas y calificaciones."""
    movies = pd.read_csv('movies.csv')
    ratings = pd.read_csv('ratings.csv')
    return movies, ratings

def recomendar_peliculas_colaborativas(user_id, ratings, movies, top_n=5):
    """Recomendar películas utilizando filtrado colaborativo."""
    # Crear matriz de utilidad
    X = ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)
    
    # Calcular la similitud entre usuarios
    user_similarity = cosine_similarity(X)
    user_similarity_df = pd.DataFrame(user_similarity, index=X.index, columns=X.index)

    # Obtener similitudes para el usuario objetivo
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)
    
    # Obtener películas que el usuario ha visto
    watched_movies = X.loc[user_id][X.loc[user_id] > 0].index
    
    # Inicializar un diccionario para las puntuaciones
    movie_scores = {}

    # Sumar las puntuaciones de usuarios similares
    for similar_user, similarity_score in similar_users.items():
        if similar_user != user_id:  # Ignorar al usuario mismo
            # Obtener las películas que el usuario similar ha visto y el puntaje
            for movie_id in X.loc[similar_user][X.loc[similar_user] > 0].index:
                if movie_id not in watched_movies:
                    if movie_id not in movie_scores:
                        movie_scores[movie_id] = 0
                    movie_scores[movie_id] += similarity_score * X.loc[similar_user, movie_id]

    # Ordenar las películas recomendadas
    recommended_movies = sorted(movie_scores.items(), key=lambda x: x[1], reverse=True)

    # Devolver las mejores N recomendaciones
    recommended_movie_ids = [movie_id for movie_id, score in recommended_movies[:top_n]]
    
    return movies[movies['movieId'].isin(recommended_movie_ids)]['title']

# Cargar datos y realizar recomendaciones
movies, ratings = cargar_datos()
user_id = 4  # Cambia el ID del usuario según sea necesario
recommendations = recomendar_peliculas_colaborativas(user_id, ratings, movies, top_n=5)
print("Recomendaciones para el usuario: ")
print(recommendations)