import streamlit as st
import pickle
import pandas as pd
# import requests

# def fetch_poster(movie_id):
#     requests.get('https://api.themoviedb.org/3/movie/1363/api_key=2475dc9816ef8850e86a4cb8744da088&language=en-US')


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),
                         reverse=True, key=lambda x: x[1])[1:6]
    # sort the similarity list in descending order
    # and it keeps the index intact using enumerate()

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title('Movie Recommendation System')

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)


selected_movie_name = st.selectbox(
    'Suggest movies similar to?', movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    # st.write(selected_movie_name)
    for i in recommendations:
        st.write(i)
