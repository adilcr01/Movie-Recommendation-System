
# Movie Recommendation using Machine learning

Recommender System is a system that seeks to predict or filter preferences
according to the user’s choices. Recommender systems are utilized in a variety
of areas including movies, music, news, books, research articles, search queries,
social tags, and products in general. 
Recommender systems produce a list of recommendations in any of the two ways – 
 

#### Collaborative filtering: 

    Collaborative filtering approaches build a model from the user’s past behavior
    (i.e. items purchased or searched by the user) as well as similar decisions 
    made by other users. This model is then used to predict items (or ratings for
    items) that users may have an interest in.

#### Content-based filtering:

    Content-based filtering approaches uses a series of discrete characteristics 
    of an item in order to recommend additional items with similar properties. 
    Content-based filtering methods are totally based on a description of the 
    item and a profile of the user’s preferences. It recommends items based on 
    the user’s past preferences.




In this project we are using a Content-based filtering approach.
This type of recommendation systems, takes in a movie that a user currently likes 
as input. Then it analyzes the contents (storyline, genre, cast, director etc.) 
of the movie to find out other movies which have similar content. Then it ranks 
similar movies according to their similarity scores and recommends the most 
relevant movies to the user.



#### CountVectorizer:

The CountVectorizer provides a simple way to both tokenize a collection of text
documents and build a vocabulary of known words, but also to encode new documents 
using that vocabulary.


#### Cosine Similarity:

Cosine similarity is a measure of similarity between two non-zero vectors of an 
inner product space that measures the cosine of the angle between them. The cosine 
of 0° is 1, and it is less than 1 for any angle in the interval (0, π] radians

#### How Cosine Similarity works?

Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.



![image](https://user-images.githubusercontent.com/93968656/141446290-432b187c-93f7-4bcd-978f-272c921893d0.png)


## Screenshot

#### home page
![movie recommender 1](https://user-images.githubusercontent.com/93968656/141446551-d7d77119-aa59-4146-a157-44fb7f244535.png)


![movie recommender 2](https://user-images.githubusercontent.com/93968656/141446592-2de5f670-e03c-43bc-8521-0ace164d0ba0.png)

#### Recomendation page
![movie recommender 3](https://user-images.githubusercontent.com/93968656/141446656-0728ea6e-2d5e-4fbf-8330-d9e5280ce6c8.png)


## Tech Stacks

##### Programming Language : Python
##### WebFramework : Steamlit
##### API : TMDB
##### Machine Learning Libraries: Numpy, Pandas, Sklearn

## Deployement on Heroku
##### Login or signup in order to create virtual app. You can either connect your github profile or download ctl to manually to deploy this project.
![image](https://user-images.githubusercontent.com/93968656/141473709-159ff490-856e-4cab-95b0-504d52b8eaea.png)

##### The next step would be to follow the instruction given in the Heroku Documentation to deploy a web app.


## Link to the application 

Check out the live demo: 
https://moviesrecommender1.herokuapp.com/

#### Loading of app might take some time as the Webframework used is Streamlit


## How to get a API key


1. First create an account on tmdb website   https://www.themoviedb.org/signup

2. Now go to Setting

3. Go to API

4. Go to API Key

![Api key 3](https://user-images.githubusercontent.com/93968656/141447807-b4e90348-695a-4fba-98a6-e710229ad902.png)


## How to run the project on local system?

   ##### 1. Clone this repository in your local system.
   ##### 2. Uncompressed the simmilarity.7z file
   ##### 3. Open your IDE from your project directory and Install all the libraries mentioned in the requirements.txt file with the command pip install -r requirements.txt.
   ##### 4. Replace YOUR_API_KEY in (line no. 6) of app.py file.
   ##### 5. Run the app.py file by clicking the run button.
   ##### 6. Go to your browser and type http://127.0.0.1:5000/ in the address bar.
   ##### Hurray! That's it.


## Dataset used

IMDB Dataset 
https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv
