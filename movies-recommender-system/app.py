import streamlit as st
import requests
import pickle

def fetch_poster(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=752d9b76bedf19f3e0eebb818912e57a&language=en-US".format(movie_id))
    # Get the full url by going on "https://developers.themoviedb.org/3/movies/get-movie-details"
    data=response.json()    # Get The API KEY by going to "https://www.themoviedb.org/settings/api"
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']  #type tmdb image path and copy url and second type the url above(request.get(this url)) and add movie id open it in newtab and copy poster_path



def recommend(film):# Function same as we have created in our movies-recommender-system jupyter note book
    f=movies[movies['title']==film].index[0]
    distance=simmilarity[f]
    list_of_movies=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies_list=[]
    recommended_movies_poster = []
    for i in list_of_movies:
        recommended_movies_list.append(movies.loc[i[0],'title'])#i[0] indexes of similar movies and we are appending title of movies
        recommended_movies_poster.append(fetch_poster(movies.loc[i[0],'movie_id']))#i[0] indexes of similar movies and we are fetching poster of it
    return recommended_movies_list,recommended_movies_poster  # Store similar movies name and poster


# open a file, where you stored the pickled data
file = open('movies.pkl', 'rb')

# dump information to that file
movies = pickle.load(file)

movies_list=movies['title'].values #Only contain movie titles

simmilarity=pickle.load(open('simmilarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movies_name = st.selectbox(
'Enter your Favourite Movie',
movies_list) # Create a drop down menu to select movie name

if st.button('Recommend'): # Create a button name recommend
    names,poster=recommend(selected_movies_name)# this function fetch_poster(recommended_movies_poster) already present in recommend
    col1, col2, col3,col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])  #st.text instead of st.header due to large font size of header
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])
