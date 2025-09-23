import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load MovieLens CSVs
movies = pd.read_csv("data/movies.csv")   # movies.csv with movieId,title,genres
ratings = pd.read_csv("data/ratings.csv") # ratings.csv with userId,movieId,rating

# Create user-item rating matrix
user_item_matrix = ratings.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)

# Compute cosine similarity between users
user_similarity = cosine_similarity(user_item_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

def recommend_movies(user_id, n=10):
    """Recommend top-N movies for a given user (collaborative filtering)"""
    if user_id not in user_item_matrix.index:
        return []

    # Find similar users
    similar_users = user_similarity_df[user_id].sort_values(ascending=False).index[1:]

    # Movies already rated by this user
    user_rated_movies = set(ratings[ratings['userId'] == user_id]['movieId'])

    recommendations = {}

    # Go through similar users' ratings
    for sim_user in similar_users:
        sim_user_ratings = ratings[ratings['userId'] == sim_user]

        for _, row in sim_user_ratings.iterrows():
            if row['movieId'] not in user_rated_movies:
                if row['movieId'] not in recommendations:
                    recommendations[row['movieId']] = row['rating']
                else:
                    recommendations[row['movieId']] += row['rating']

        if len(recommendations) >= n:
            break

    # Sort movies by score
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)[:n]

    # Map IDs to titles
    final_recommendations = [(movies[movies['movieId'] == mid]['title'].values[0], round(score, 2))
                             for mid, score in sorted_recommendations if mid in movies['movieId'].values]

    return final_recommendations
