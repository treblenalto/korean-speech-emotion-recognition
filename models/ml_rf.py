import os
import pandas as pd 

from ml_corpus import make_corpus
from ml_display import display_results
# from ml_display import  display_results, plot_confusion_matrix
from sklearn.ensemble import RandomForestClassifier 
from sklearn.model_selection import train_test_split 
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(path)

    df = pd.read_csv('../data/most_common.csv')
    cat_to_id = {'Angry': 0,
            'Disgust': 1,
            'Fear': 2,
            'Happiness': 3,
            'Neutral': 4,
            'Sadness': 5,
            'Surprise': 6}

    # Tokenize based on morphology analysis
    corpus = make_corpus(df['speech'])
    print(corpus[:3])


if __name__=="__main__":
    main()