# Movie Recommendation System

This Python script provides a basic movie recommendation system using user ratings data. It uses cosine similarity to find users with similar preferences and recommends movies based on ratings from similar users.

## Features

- **User-Item Matrix Creation**: Converts user ratings into a matrix with users as rows and movies as columns.
- **Cosine Similarity Calculation**: Computes the similarity between users based on their movie ratings.
- **Movie Recommendations**: Recommends movies to a user based on the ratings of similar users.

## Requirements

- Python 3.x
- `pandas`
- `scikit-learn`

You can install the required libraries using pip:

```bash
pip install pandas scikit-learn
