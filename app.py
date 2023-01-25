import streamlit as st
import pickle
import pandas as pd


allmovie_dict=pickle.load(open('allmovie_dict.pkl','rb'))
cm=pickle.load(open('cm.pkl','rb'))
x=allmovie_dict.values()

def get_similar(movie_name,rating):
    similar_ratings = cm[movie_name]*(rating-2.5)
    similar_ratings = similar_ratings.sort_values(ascending=False)
    return similar_ratings



st.title('C.F based Movie Recomender System')

movieone=st.selectbox("Choose Movie ",x,key=1)
ratingone=st.selectbox("Rate movie",(1,2,3,4,5),key=2)
movietwo=st.selectbox("Choose Movie ",x,key=3)
ratingtwo=st.selectbox("Rate movie",(1,2,3,4,5),key=4)
moviethree=st.selectbox("Choose Movie ",x,key=5)
ratingthree=st.selectbox("Rate movie",(1,2,3,4,5),key=6)

if st.button('Recommend'):
    st.header('Reviews provided are... ')
    st.write(movieone)
    st.write(ratingone)
    st.write(movietwo)
    st.write(ratingtwo)
    st.write(moviethree)
    st.write(ratingthree)
    pickle.dump((movieone, ratingone,movietwo,ratingtwo,moviethree,ratingthree), open('q.pkl', 'wb'))


    personality = [(movieone, ratingone), (movietwo, ratingtwo), (moviethree, ratingthree)]
    similar_movies = pd.DataFrame()
    for movie, rating in personality:
        similar_movies = similar_movies.append(get_similar(movie, rating), ignore_index=True)

    similar_movies.head(10)
    similar_movies.sum().sort_values(ascending=False).head(20)
    newlist = list(similar_movies.columns.values)
    newdict = {stu: "Passed" for stu in newlist}
    xar = newdict.keys()
    st.header('Recommended movies are')
    for i in xar:
        st.write(i, "\n");