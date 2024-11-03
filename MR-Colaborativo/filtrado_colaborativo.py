import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def cargar_datos():
    """Cargar datos de películas y calificaciones."""
    movies = pd.read_csv('movies.csv')
    ratings = pd.read_csv('ratings.csv')
    return movies, ratings

def recomendar_peliculas_colaborativas(user_id, ratings, movies, top_n=5):
    """Recomendar películas utilizando filtrado colaborativo."""
    X = ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)
    
    user_similarity = cosine_similarity(X)
    user_similarity_df = pd.DataFrame(user_similarity, index=X.index, columns=X.index)

    similar_users = user_similarity_df[user_id].sort_values(ascending=False)
    
    watched_movies = X.loc[user_id][X.loc[user_id] > 0].index
    
    movie_scores = {}

    for similar_user, similarity_score in similar_users.items():
        if similar_user != user_id:
            for movie_id in X.loc[similar_user][X.loc[similar_user] > 0].index:
                if movie_id not in watched_movies:
                    if movie_id not in movie_scores:
                        movie_scores[movie_id] = 0
                    movie_scores[movie_id] += similarity_score * X.loc[similar_user, movie_id]

    recommended_movies = sorted(movie_scores.items(), key=lambda x: x[1], reverse=True)

    recommended_movie_ids = [movie_id for movie_id, score in recommended_movies[:top_n]]
    
    return movies[movies['movieId'].isin(recommended_movie_ids)]['title']

movies, ratings = cargar_datos()
user_id = 4
recommendations = recomendar_peliculas_colaborativas(user_id, ratings, movies, top_n=5)
print("Recomendaciones para el usuario: ")
print(recommendations)
