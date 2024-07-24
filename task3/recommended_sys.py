import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample data: User preferences for movies
data = {
    'user_id': [1, 1, 1, 2, 2, 3, 3],
    'movie_title': ['Inception', 'Avatar', 'Titanic', 'Inception', 'The Matrix', 'Avatar', 'Titanic'],
    'rating': [5, 4, 3, 4, 5, 5, 3]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Pivot the DataFrame to get users as rows and movies as columns
user_movie_matrix = df.pivot_table(index='user_id', columns='movie_title', values='rating')

# Fill NaN values with 0
user_movie_matrix = user_movie_matrix.fillna(0)

# Compute cosine similarity between users
user_similarity = cosine_similarity(user_movie_matrix)

# Convert the similarity matrix to a DataFrame
user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)

# Function to recommend movies
def recommend_movies(user_id, user_movie_matrix, user_similarity_df, top_n=3):
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)
    similar_users = similar_users.drop(user_id)  # Exclude the user itself

    recommended_movies = pd.Series()

    for similar_user in similar_users.index:
        similar_user_movies = user_movie_matrix.loc[similar_user]
        user_movies = user_movie_matrix.loc[user_id]
        unrated_movies = similar_user_movies[user_movies == 0]

        # Add the unrated movies of similar users to the recommendations using concat
        recommended_movies = pd.concat([recommended_movies, unrated_movies])

    # Sort the recommended movies by their average rating
    recommended_movies = recommended_movies.groupby(recommended_movies.index).mean().sort_values(ascending=False)

    return recommended_movies.head(top_n)


    return recommended_movies.head(top_n)

# Example usage
user_id = 1
recommendations = recommend_movies(user_id, user_movie_matrix, user_similarity_df)
print(f"Recommendations for user {user_id}:")
print(recommendations)
