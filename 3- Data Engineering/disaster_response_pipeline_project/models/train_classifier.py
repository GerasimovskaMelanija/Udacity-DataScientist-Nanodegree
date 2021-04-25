import sys
import nltk
import re
import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import GridSearchCV
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.pipeline import Pipeline
from sqlalchemy import create_engine
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report
nltk.download(['punkt', 'wordnet'])
# import libraries


def load_data(database_filepath):
    """This function loads the dataset from database"""
    engine = create_engine('sqlite:///{}'.format(database_filepath))
    df = pd.read_sql_table('Disaster_messages', con=engine)
    print(df.shape)
    X = df['message']
    Y = df.iloc[:, 4:]
    return X, Y


def tokenize(text):
    """This function tokenize the text"""
    # tokenize text
    tokens = word_tokenize(text)

    # initiate lemmatizer
    lemmatizer = WordNetLemmatizer()

    # iterate through each token
    clean_tokens = []
    for tok in tokens:

        # lemmatize, normalize case, and remove leading/trailing white space
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens


def build_model():
    """This function returns machine learning pipeline"""
    pipeline = Pipeline([

            ('text_pipeline', Pipeline([
                ('vect', CountVectorizer(tokenizer=tokenize)),
                ('tfidf', TfidfTransformer())
            ])),

        # We can try and Support Vector Machine Classifier, but it will take longer to train the model
        # ('clf', MultiOutputClassifier(KNeighborsClassifier()))
        ('clf', MultiOutputClassifier(RandomForestClassifier()))
    ])

    # specify parameters for grid search
    parameters = {'clf__estimator__n_estimators'  : [7, 20],
                  'clf__estimator__max_depth' : [10, 17],
                  # 'clf__estimator__weights' : ['uniform', 'distance'],

    }
    """parameters = { 'features__text_pipeline__vect__ngram_range': ((1, 1), (1, 2)),
                  'clf__estimator__n_estimators'  : [10, 50],
                  'clf__estimator__max_depth' : [20, 30],

    }"""

    # create grid search object
    # cv = GridSearchCV(pipeline, param_grid = parameters, cv = 3)
    cv = GridSearchCV(pipeline, param_grid=parameters)
    return cv


def evaluate_model(model, X_test, y_test):
    """This function predicts X_test and display the information about the predicted value and the real value"""
    y_pred = model.predict(X_test)
    for i, col in enumerate(y_test):
        print('For Column: ', col)
        print(classification_report(y_test.values[i], y_pred[i]))


        
    #for i, col in enumerate(y_test):
       #print('F1_score for Column: ', col)
       #print(f1_score(y_test.values[i], y_pred[i]))
    # accuracy = (y_pred == y_test).mean()  
    # print(accuracy)
       


def save_model(model, model_filepath):
    """This function saves the model as pickle file"""
    with open(model_filepath, 'wb') as pickle_file:
        pickle.dump(model, pickle_file)


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

        print('Building model...')
        model = build_model()

        print('Training model...')
        model.fit(X_train, Y_train)

        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()