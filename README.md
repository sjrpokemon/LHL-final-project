# Capstone Project LHL
## Movie Recommendation Engine
## Abstract
This project introduces a streamlined movie recommendation system designed for users to input a single preferred movie and receive tailored recommendations. 
I have synergized CountVectorizer and NLTK for personalized recommendations. By combining CountVectorizer and NLTK, the recommendation algorithm in my app gains a deeper understanding of user preferences from textual inputs.

## Method:
### Dataset
The dataset employed in this project is Kaggle's "TMDB 5000 Movie Dataset," comprising approximately 4800 movies with details such as cast, crew, keywords, and user ratings. Two primary files, 'tmdb_5000_credits.csv' for cast and crew and 'tmdb_5000_movies.csv' for user ratings and overviews, were utilized.
### Download dataset: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata/data

## Natural Language Processing (NLP)

![Method2](https://github.com/sjrpokemon/LHL-final-project/assets/128329266/2ffa827c-7554-4791-8476-4848f67faf11)

1. Keyword Extraction: Extracting meaningful keywords from movie overviews, tags, cast, and crew.

2. Word Tokenization with NLTK: Breaking down extracted keywords into individual variables using the nltk library.

3. CountVectorizer: Utilizing the CountVectorizer to convert the variable-length word sequences into a fixed-length feature vector for analysis.

## Result
The processed data, enriched with meaningful keywords from natural language processing techniques, was structured into a dataframe. For enhanced user interaction, the resulting dataframe was serialized into a pickle file and seamlessly integrated into a sophisticated Streamlit web application.

Streamlit App Integration: The Streamlit app has been successfully developed and deployed, allowing users to input a single preferred movie and receive five personalized recommendations. This marks a significant achievement, showcasing the operationalization of the recommendation engine in an interactive and user-friendly manner.

![streamlit](https://github.com/sjrpokemon/LHL-final-project/assets/128329266/75b20b87-7347-467f-8da0-bf643c15e9d1)

## Future Development

![Movie-flowchart](https://github.com/sjrpokemon/LHL-final-project/assets/128329266/0c6c662d-0a95-42e9-8a13-000e8ea72050)


![Method](https://github.com/sjrpokemon/LHL-final-project/assets/128329266/7f4ba9c2-a4ad-41ae-81f0-e15283cedc74)

Apply Apriori Algorithm & K-means Clustering:
  - Utilized utility matrix with ratings converted to binary.
  -  Applied Apriori for frequent itemsets and K-means for clustering.

The data processing phase for implementing machine learning techniques, specifically Apriori and K-means clustering, has been successfully completed. The output of the Apriori algorithm serves as a crucial input for the subsequent application of K-means clustering. This multi-layered approach aims to refine and enhance the recommendation engine, providing users with even more accurate and personalized movie suggestions. The seamless integration of these advanced techniques sets the foundation for continuous improvement and future feature expansion within the recommendation system.

## Challenges
While progressing with the integration of the recommendation system into the Streamlit app, a few challenges have been encountered. The complexities lie in seamlessly connecting the processed data with the app's interface, ensuring a user-friendly and efficient experience. Debugging and refining this integration process may require careful attention to ensure optimal functionality and a smooth recommendation flow within the app.

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
