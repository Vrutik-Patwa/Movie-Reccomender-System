import streamlit as st
import pickle
import pandas as pd
st.title('Movie Recommender System')

movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)
similarity=pickle.load(open('Similarity.pkl','rb'))
def recommend_movie(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommend_movies=[]
    for i in movie_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies



Selcted_Movie_Name= st.selectbox(
    'Select a movie',
movies['title'].values)
if(st.button('Recommend')):
    recommend=recommend_movie(Selcted_Movie_Name)
    for i in recommend:
        st.write(i)
# st.write('You selected:', option)