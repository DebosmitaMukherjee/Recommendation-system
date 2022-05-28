# Movie Recommendation System
Hello everyone I have created a website to recommend user movies based on their movie choice using content based recommendation engine.
Here is the link for video demo of this project:
https://youtu.be/IdS42lESeVQ

## Datasets:
Here is the link to the kaggel data sets for this project,please download this dataset from there to run the project in your local computer:
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
(*Please download both tmdb_5000_credits.csv and tmdb_5000_movies.csv both ans make sure to keep them in the same directory where you have cloned the project*)

## Requirements:
I have used python 3.7 for this project 
I have also used some python libraries- *numpy, pandas,ast, nltk, sklearn, pickle , streamlit , requests*. **Please before running the project , install these libraries.**
Also I have used tmdb api for fetching movie posters from tmdb api , my api key is used in the file 'app.py' and the api key is : 539d2d5bdfab55d9f5636de376fa0c21, otherwise you can run the app.py file as it is 
I used cosine similarity approach for this purpose to generate recommendations, so there are big files getting used in this project, so if you want to push this project in your repo then use git lfs

## Functionality of the webiste:
This site will take user inputs that is the favourite movie name from the list (selectbox) in the site, then it shows swome deatils of that movie and top 5 similar movies for choosen movie. There is also a comment section for taking user reviews on the site.

## How to run the site in your local computer:
- First of all clone the repo using https key , it may take time due to long files uploaded in this repo. 
- After that install all python libraries that is not already installed in your computer according to the version of python
- Then it is completely fine to run only the app.py file from your terminal(*in the floder where all cloned files are*) with the command -
``` python -m streamlit run app.py ``` (*this is the command for windows , find appropreate command according to your operating system*) , if you want to only see the app working , as all the data preprocessing generated files are uploaded in this repo, and when you clone it all the files gets downloaded, other wise you can also run the .ipynb checkpoint file .
- That's it!!! Now if there is no problem in installation in your computer , the app should run fine.

## Future scope of this site:
In future this site can be connected to other real time advanced api realted to current or recent movies to do this same.
We can also stream realtime movies in this site. Also this idea of recommendation system can be used to make recommendations for other topics also such as- books , songs, recommendations system in e-commerce websites , recommendation engine for videos based on title, content , subtitles, popularity e.t.c.
