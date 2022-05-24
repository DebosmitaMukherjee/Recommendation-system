import streamlit as st
import pickle
import requests

st.set_page_config(page_title="Movie Recommendation System",layout="wide",initial_sidebar_state="collapsed")
st.markdown(
    """
    <style>
    .main {
    background-color: #d5b9f0;
    }
    </style>
    """, unsafe_allow_html=True
)

def fetch_posters(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=539d2d5bdfab55d9f5636de376fa0c21&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    if poster_path is False:
        poster_path = "/m73KqOLXf9ZvPVCWS5dz5Hv7yQF.jpg"
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    # st.text("hello2")
    movie_ind=movies[movies['title']==movie].index[0]
    # st.text("hello3")
    distance = similarity[movie_ind]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        # now fetch posters to display form TMDB API
        recommended_movies_poster.append(fetch_posters(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies, recommended_movies_poster

def show_details(selected_movie_tit):
    movie_ind = movies[movies['title'] == selected_movie_tit].index[0]
    st.write("Details of the movie:")
    l1 = "Movie name: "
    st.caption(l1)
    # st.
    st.write(selected_movie_tit)
    ind1 = movies_fin[movies_fin['title'] == selected_movie_tit].index[0]
    l2 = movies_fin.iloc[ind1].overview
    p = ""
    for i1 in l2:
        p = p + i1 + " "
    st.write("Overview of the Movie:")
    st.caption(p)
    cast = movies_fin.iloc[ind1].cast
    st.write("Top 3 casts of the movie:")
    cnt = 0
    for i1 in cast:
        pri = ""
        if cnt == 0:
            pri += "i) "
        elif cnt == 1:
            pri += "ii) "
        else:
            pri += "iii) "
        pri += i1
        st.caption(pri)
        cnt += 1
    dir = movies_fin.iloc[ind1].director_name
    st.write("Director name:")
    for i1 in dir:
        st.caption(i1)

def show_recommendations(selected_movie_tit):
    movie_ind=movies[movies['title']==selected_movie_tit].index[0]
    st.header("*Details of the movie*:")
    pos = fetch_posters(movies.iloc[movie_ind].id)
    col1, col2 = st.columns(2)
    with col1:
        st.image(pos, width=400)
        st.caption(selected_movie_tit)
    with col2:
        l1 = "*Movie name*: "
        st.subheader(l1)
        # st.
        st.write(selected_movie_tit)
        ind1=movies_fin[movies_fin['title']==selected_movie_tit].index[0]
        l2=movies_fin.iloc[ind1].overview
        p=""
        for i1 in l2:
            p=p+i1+" "
        st.subheader("*Overview of the Movie*:")
        st.write(p)
        cast=movies_fin.iloc[ind1].cast_name
        st.subheader("*Top 3 casts of the movie*:")
        cnt=0
        for i1 in cast:
            pri=""
            if cnt==0:
                pri+="i) "
            elif cnt==1:
                pri+="ii) "
            else:
                pri+="iii) "
            pri+=i1
            st.write(pri)
            cnt+=1
        dir=movies_fin.iloc[ind1].director_name
        st.subheader("*Director name*:")
        for i1 in dir:
            st.write(i1)
    # st.text("hello1")
    st.subheader("*Here are 5 recommendations for you !!* ")

    name, poster = recommend(selected_movie_tit)
    col = st.columns(5)
    cnt = 0
    for i in col:
        with i:
            img = st.image(poster[cnt])
            st.write(name[cnt])
            cnt+=1



movies_list = pickle.load(open('movies.pkl', 'rb'))
movies=movies_list
movies_list=movies_list['title'].values
movies_fin = pickle.load(open('movies_final.pkl', 'rb'))
# movies_fin_
similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title("*Movie Recommendation System*")
selected_movie_title = st.selectbox('Choose your favourite movie', movies_list)
st.caption("*Choose your favourite movie and click on 'Recommend' button to see recommendations* ")
if st.button('Recommend'):
    show_recommendations(selected_movie_title)
    st.success("Successfully recommended!!")
    st.caption("*Copy and paste movie name to the selectbox to see recommendations for that movie!!*")
# st.markdown(
#     """
#     <style>
#     color:blue;
#     </style>
#     """,
#     unsafe_allow_html=True
# )

st.subheader("*Comment  Section:*")
st.text_input("Please write your comments here!!")
if st.button("Submit Response"):
    # show_recommendations(selected_movie_title)
    st.success("Thanks for your valuable comments!!")


