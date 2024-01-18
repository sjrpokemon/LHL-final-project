# Capstone Project LHL
## Movie Recommendation Engine
## Abstract
##### This project introduces a streamlined movie recommendation system designed for users to input a single preferred movie and receive tailored recommendations. 
##### I have Synergized CountVectorizer and NLTK for Personalized Recommendations. By combining CountVectorizer and NLTK, the recommendation algorithm in my app gains a deeper understanding of user preferences from textual inputs.

## Method:
### Dataset
##### The dataset used in this proejct is Kaggle's "TMDB 5000 Movie Dataset", containing around 4800 movies, including details such as cast, crew, keywords, and user ratings.
##### For the project, two files were primarily used: 'tmdb_5000_credits.csv' for cast and crew and tmdb_5000_movies.csv' for user ratings and overviews.

### Natural Language Processing (NLP)

1. Keyword Extraction: Extracting meaningful keywords from movie overviews, tags, cast, and crew.

2. Word Tokenization with NLTK: Breaking down extracted keywords into individual variables using the nltk library.

3. CountVectorizer: Utilizing the CountVectorizer to convert the variable-length word sequences into a fixed-length feature vector for analysis.

## Result
##### The processed data, containing the meaningful keywords extracted through natural language processing techniques, was integrated into a structured dataframe. To enhance user interaction, the resulting dataframe was serialized into a pickle file and seamlessly integrated into a Streamlit web application.

## Future Development
![Movie-flowchart](https://github.com/sjrpokemon/LHL-final-project/assets/128329266/0c6c662d-0a95-42e9-8a13-000e8ea72050)


![Method](https://github.com/sjrpokemon/LHL-final-project/assets/128329266/7f4ba9c2-a4ad-41ae-81f0-e15283cedc74)

Apply Apriori Algorithm & K-means Clustering:
  - Utilized utility matrix with ratings converted to binary.
  -  Applied Apriori for frequent itemsets and K-means for clustering.

##Project Structure
```
├── app                       <- Folder For All The Streamlit App Code  
│   ├── app.py                            <- my streamlit app 
│   ├── .env                              <- api_key
│
├── datasets                  <- Data Folder 
│   ├── tmdb_5000_credits.csv            <- data source
│   ├── tmdb_5000_movies.csv             <- data source
├── figures                   <- Images Used in the Project 
│   ├── Method1.png                      <-  Apriori and K-means Clustering   
│   ├── Method2.png                      <-  Item-based Collaborative Filtering
│   ├── Movie-flowchart.png              <-  Flowchart of the project
├── pickle                    <- pickle data
│   ├── movies_list.py                   <- list of movies
│   ├── similarity.pkl                   <- cosine_similarity applied
│   ├── overview.pkl                     <- data of overview
│   ├── apriori.pkl                      <- apriori for future use
│   ├── df_numeric.pkl                   <- K-means clustering for future use
│   ├── lift_list.pkl                    <- Apriori for future use
├── data_processing_and_ML    <- Jupyter notebook of data preprocessing and applying Machine Learning
│   ├── Collaborative-filtering.ipynb    <- K-means clustering for future use
│   ├── future_work.ipynb                <- Apriori and K-means clustering for future use      
└── README.md                 <- Project Documentation
```
## The Streamlit App
#### To run the Streamlit App, run the following command: 
```
streamlit run app/app.py
```
