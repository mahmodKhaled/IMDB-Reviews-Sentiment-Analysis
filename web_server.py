import tensorflow as tf
import re
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from fastapi import FastAPI
from typing import Union

def clean_imdb(text):
    """
    Cleans a string of text by performing the following steps:
    1. Removes HTML tags from the text using BeautifulSoup.
    2. Removes non-alphanumeric characters (including punctuation) from the text using regular expressions and
    converts the text to lowercase.
    3. Tokenizes the text into a list of words using the `nltk.word_tokenize()` function.
    4. Removes stop words from the list of words using the `nltk.corpus.stopwords()` module.
    5. Lemmatizes the list of words using the `nltk.stem.WordNetLemmatizer()` class.
    6. Joins the lemmatized list of words back into a single string.

    Args:
        text (str): A string of text to be cleaned.

    Returns:
        str: A cleaned version of the input text.
    """
    # Remove HTML tags and special characters
    text = BeautifulSoup(text, "html.parser").get_text()  # remove HTML tags
    text = text.lower() # convert to lowercase
    text = re.sub(r"[^a-zA-Z0-9 ]", "", text)  # remove non-alphanumeric characters

    # Tokenize the text
    tokens = nltk.word_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in stop_words]

    # Initialize the Porter Stemmer
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]

    # Join the tokens back into a single string
    cleaned_text = " ".join(tokens)

    return cleaned_text

def predictions(model, X_test):
  """
    Makes predictions using a model.
    Parameters:
    - model: A model object.
    - X_test: A NumPy array containing the input data to use for predictions.
    Returns:
    - A String represent the predicted label
  """
  # perform predictions
  pred = model.predict([X_test])
  correct_pred = 'Negative' if pred[0,0] > pred[0,1] else 'Positive'
  return correct_pred

app = FastAPI()
model = tf.keras.models.load_model('model_weights')

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/Inference")
def Inference(input: str):
  X_test = clean_imdb(input)
  y_pred = predictions(model, X_test)
  output = f'The Movie Review is: {y_pred}'
  return output