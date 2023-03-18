# IMDB-Reviews-Sentiment-Analysis

## Dataset Description

The IMDB movie reviews dataset is a widely-used dataset in natural language processing (NLP) research and applications. It consists of a collection of 50,000 movie reviews from the Internet Movie Database (IMDB), labeled as either positive or negative sentiment.

The dataset is commonly used for sentiment analysis tasks, where the goal is to classify the sentiment of a given text as either positive or negative. Each review in the dataset is represented as a sequence of words, and the labels indicate whether the review has a positive or negative sentiment.

The dataset is evenly split between training and testing sets. The reviews in the training set are used to train machine learning models, while the reviews in the testing set are used to evaluate the performance of the models.

The IMDB movie reviews dataset has become a standard benchmark dataset in the NLP community, and has been used to train and evaluate a variety of machine learning models for sentiment analysis and related tasks.

## Instructions

### Test outside the Docker Image

You can test the model on **Fastapi** server by runinng this command only, without the need to build the docker image to test it.

```
uvicorn web_server:app --reload
```
After that go to this link in the web browser
```
http://127.0.0.1:8000
```
Then edit the link and add /docs at the end to be able to go to interactive API docs

### How to build the docker image
To build the Docker Image we should execute the following docker-compose command
```
docker-compose -f docker-compose.yaml up
```

### How to test the solution

There is two ways to test the solution 
1. At this point the app was built and the connection to the  server is active now, so we can head now to the server by opening the browser and type this **URL** in the search bar
```
http://localhost:80/docs
```
2. Another way you can head to the server, is to open the **Docker Desktop Application** if it was installed on your local machine, you can open it then on the left press on **Containers**, then you will see our container expand it, then head to the **PORT(S)** column, and you will see this port **8000:8000**, then press on it and it will get you directly to the server to test
