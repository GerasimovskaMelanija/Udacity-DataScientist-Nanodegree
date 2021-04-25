# Disaster Response Pipeline Project

### Instructions: (If you want to try it on your local machine)
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

Also, there is a model trained with KNN and can be found [here](https://drive.google.com/drive/folders/16oSTqkjX1KL7I3SXTcGkfWRUWMY_mdlx?usp=sharing). This file is too large to be uploaded on Github.<br/>
You can choose to use the model on the Github repository (RandomForestClassifier), or the other model with KNN.

## File Description
1. Folder model (This folder contains the train_classifier.py python file, that contains the Machine Learning Pipeline for training the model and classifier.pkl, that is trained model with Random Forest Classifier).<br/>
2. Folder data (Contains the data used for training and testing the model, python file for data preprocessing and saving the data into database).<br/>
3. Folder app (Contains all files that we need for the web application).<br/>
4. README file.



