import streamlit as st
import requests

st.header('Movie Recommender System')

# Fetch movie list from pickle file
import pickle
movies_df = pickle.load(open('movie_list.pkl', 'rb'))
movie_list = movies_df['title'].values

selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button('Show Recommendation'):
    response = requests.get(f"http://127.0.0.1:5000/recommend?movie={selected_movie}")
    
    if response.status_code == 200:
        data = response.json()
        
        if data:
            cols = st.columns(5)
            for i, col in enumerate(cols):
                with col:
                    st.text(data[i]['title'])
                    st.image(data[i]['poster'])  # Poster key matches backend response
        else:
            st.warning("No recommendations found!")
    else:
        st.error("Error fetching recommendations!")
