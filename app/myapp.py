import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests
from sklearn import preprocessing
from dotenv import load_dotenv
import os

# Fetching API-Key
def configure():
    load_dotenv()

def fetch_poster(movie_id):
    configure()
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={os.getenv('API_KEY')}&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


# Load data
movies = pickle.load(open("movies_list.pk1", "rb"))
movies_overview = pickle.load(open("overview.pk1", "rb"))
similarity = pickle.load(open("similarity.pk1", 'rb'))
kmeans_df = pickle.load(open('df_numeric.pk1', 'rb'))
apriori_df = pickle.load(open("apriori_df.pk1", "rb"))
movies_list = movies['title'].values

# Front-End
st.header("Movie Recommendation System")

# Create a dropdown to select a Movie
selected_movie = st.selectbox("Select a movie:", movies_list)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movie, recommend_poster, recommend_rating, recommend_overview = [], [], [], []
    
    for i in distance[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movie_id))
        recommend_rating.append(movies.iloc[i[0]].vote_average)
        recommend_overview.append(movies_overview.iloc[i[0]].overview)

    # Sort recommendations based on ratings (highest to lowest)
    sorted_recommendations = sorted(zip(recommend_movie, recommend_poster, recommend_rating, recommend_overview),
                                    key=lambda x: x[2], reverse=True)

    # Unpack the sorted recommendations
    sorted_movies, sorted_posters, sorted_ratings, sorted_overviews = zip(*sorted_recommendations)

    return sorted_movies, sorted_posters, sorted_ratings, sorted_overviews


if st.button("Show Recommendations"):
    movie_name, movie_poster, movie_rating, movie_overview = recommend(selected_movie)
    num_recommendations = len(movie_name)

    # Display recommendations with posters and toggleable overview
    for i in range(num_recommendations):
        col1, col2 = st.columns([1, 2])  # Adjust the column ratios as needed

        with col1:
            st.image(movie_poster[i], width=150, use_column_width=True)

        with col2:
            st.markdown(f"**{movie_name[i]}**", unsafe_allow_html=True)
            st.write(f"Rating: {movie_rating[i]}")

            # Use st.expander for toggleable overview
            with st.expander("Movie Overview"):
                st.write(movie_overview[i])












