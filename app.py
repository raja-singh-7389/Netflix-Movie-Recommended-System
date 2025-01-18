import streamlit as st
import pickle

# Set up the title for the app
st.title('Netflix Recommender System')

# Load the movie list from the pickle file
movie_list = pickle.load(open('movie_list', 'rb'))

# Extract movie names from the dataframe
movie_list = movie_list['Movie Name'].values

# Select a movie from the list
option = st.selectbox(
    'Type movie to find recommended movies', 
    movie_list  # The list of movies for the selectbox options
)

# Display the selected movie
st.write(f'You selected: {option}')

# Implement your recommendation logic here
# Example: assuming you have a recommendation function `recommend()` that uses the selected movie
# recommendation = recommend(option)  # You would call the function that returns recommended movies

# Display the recommendations
# st.write(recommendation)  # Display the recommended movies
