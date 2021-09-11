import os
import pandas as pd 

from corpus import make_corpus
from display import display_results, plot_confusion_matrix

from catboost import CatBoostClassifier                          
from sklearn.model_selection import train_test_split 
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(path)

    df = pd.read_csv('../../data/most_common.csv')
    cat_to_id = {'Angry': 0,
            'Disgust': 1,
            'Fear': 2,
            'Happiness': 3,
            'Neutral': 4,
            'Sadness': 5,
            'Surprise': 6}

    # tokenize based on morphology analysis
    corpus = make_corpus(df['speech'])

    X = corpus                        # tokenized & cleansed data 
    y = df['emotion'].map(cat_to_id)  # change y label to index values

    # train-test-split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

    # tf-idf encoding
    tfidf = TfidfVectorizer(max_features = 1000).fit(X_train)
    X_train = tfidf.fit_transform(X_train).toarray()
    X_test = tfidf.fit_transform(X_test).toarray()

    # Catboost
    cbc = CatBoostClassifier(task_type = "GPU", 
                            verbose = 200) 
    cbc.fit(X_train, y_train)

    # predict 
    cbc_pred = cbc.predict_proba(X_test)

    # result 
    display_results(y_test, cbc_pred)

if __name__=="__main__":
    main()