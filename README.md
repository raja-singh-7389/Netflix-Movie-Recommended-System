# Netflix-Movie-Recommended-System-App

This project is a movie recommendation system designed to suggest movies similar to a user-provided movie based on genres. It uses cosine similarity on the genres of movies to find and recommend similar ones.

How It Works
	1.	The dataset contains information about movies, including:
	•	Movie Name
	•	Rating
	•	Genre
	2.	The genres are vectorized using the Bag of Words (BoW) model.
	3.	Cosine similarity is applied to compute similarity between movies.
	4.	The system recommends the top 5 most similar movies to the one you input.

Prerequisites
	•	Python 3.8 or later
	•	Libraries required:
	•	pandas
	•	scikit-learn
	•	joblib

How to Use
	1.	Prepare the dataset (Netflix-title.csv) with columns: ID, Movie Name, Rating, Genre.
	2.	Run the script to generate the required files:
	•	movie_list.joblib (contains preprocessed movie data)
	•	similarity.joblib (contains the similarity matrix)
	3.	Use the recommend() function to get movie recommendations:

recommend('Movie Name')

Example

recommend('Ganglands')

Output:

Top 5 movies similar to 'Ganglands':
1. Blood & Water
2. Kota Factory
3. Jailbirds New Orleans
4. Dick Johnson Is Dead
5. Ganglands
