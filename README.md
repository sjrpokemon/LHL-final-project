# Capstone Project LHL
## Movie Recommendation Engine
## Abstract
This project introduces an efficient movie recommendation system. Users can input a favorite movie and receive personalized recommendations. The system utilizes CountVectorizer and NLTK to analyze user preferences based on their movie selection, enhancing the recommendation accuracy.

## Method:
### Dataset
The project uses the "TMDB 5000 Movie Dataset" from Kaggle, featuring details of approximately 4800 movies, including cast, crew, keywords, and user ratings. The dataset includes two key files: 'tmdb_5000_credits.csv' and 'tmdb_5000_movies.csv'.
### Download dataset: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata/data

## Natural Language Processing (NLP)

![Method2](https://github.com/sjrpokemon/LHL-final-project/assets/128329266/2ffa827c-7554-4791-8476-4848f67faf11)

1. Keyword Extraction: Extracting significant keywords from movie overviews, tags, cast, and crew.

2. Word Tokenization with NLTK: Using NLTK to break down keywords into individual tokens.

3. CountVectorizer: Applying CountVectorizer to transform word tokens into a uniform feature vector for analysis.

## Result
The system processes the data using NLP techniques, resulting in a structured dataframe. This data is then serialized into a pickle file and integrated into a Streamlit web application for user interaction.

Streamlit App Integration: The Streamlit application allows users to input a favorite movie and receive five personalized recommendations. This demonstrates the recommendation engine's effective operation in an engaging and user-friendly platform.

![streamlit](https://github.com/sjrpokemon/LHL-final-project/assets/128329266/75b20b87-7347-467f-8da0-bf643c15e9d1)

## Future Development

![Movie-flowchart](https://github.com/sjrpokemon/LHL-final-project/assets/128329266/0c6c662d-0a95-42e9-8a13-000e8ea72050)


![Method](https://github.com/sjrpokemon/LHL-final-project/assets/128329266/7f4ba9c2-a4ad-41ae-81f0-e15283cedc74)

Applying Apriori Algorithm & K-means Clustering:

- Conversion of ratings to a binary format in a utility matrix.
- Implementation of Apriori for frequent itemset detection and K-means for clustering.
- 
The project is poised to incorporate Apriori and K-means clustering to further refine the recommendation accuracy. The integration of these advanced algorithms aims to enhance the system's ability to deliver more precise movie suggestions.

## Challenges
While progressing with the integration of the recommendation system into the Streamlit app, a few challenges have been encountered. Incorporating the Apriori algorithm's output into K-means clustering presented a significant challenge. The Apriori algorithm, used for identifying frequent itemsets in our dataset, outputs combinations of items (movies) and their support values. The main task was to transform this output into a suitable format for K-means clustering. This involved creating a binary matrix representing the presence or absence of movies in each itemset. The K-means algorithm then used this matrix to cluster movies based on their similarities in itemset appearances. Determining the optimal number of clusters and ensuring a correct flow of data from Apriori to K-means required careful attention. Moreover, validating the clusters formed by K-means to ensure their relevance to the recommendation system added another layer of complexity to the project.

## Project Structure
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
│   ├── streamlit.png                    <-  streamlit app
├── pickle(file too big to upload) <- pickle data
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
