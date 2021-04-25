# Disaster Response Pipeline Project

### Description
In this project we are using dataset from Figure Eight in order to create disaster response pipeline. We created two pipelines: ETL and Machine Learning Pipeline. We have trained two different models, one with KNN and the other with RandomForestClassifier. The model with KNN gives us great results and can be found on this link [here](https://drive.google.com/drive/folders/16oSTqkjX1KL7I3SXTcGkfWRUWMY_mdlx?usp=sharing). This model is very large and can not be uploaded on Github. The other model with RandomForestClassifier does not give us very good results, and this model can be found in the folder model.<br/>

### Libraries
Numpy<br/>
Pandas<br/>
Plotly<br/>
Flask<br/>
Scikit-learn<br/>
SQLAlchemy<br/>
Gunicorn<br/>
Scipy<br>
Nltk<br/>

### File Description
1. Folder model (This folder contains the train_classifier.py python file, that contains the Machine Learning Pipeline for training the model and classifier.pkl, a trained model with Random Forest Classifier).<br/>
2. Folder data (Contains the dataset used for training and testing the model, and contains a python file, used for data preprocessing and saving the data into database).<br/>
3. Folder app (Contains all files that we need for the web application).<br/>
4. README file.<br/>
5. Application.py, Requirements.txt, Procfile and nltk.txt are for Flask and you do not need them if you want to run this app locally.

### Instructions: (If you want to try it on your local machine)
You should have all this folders if you want to run in locally. If you want to try it from the beggining, then you should start from step 1, but if you want to use my model, then you should skip step 1.<br/>

1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://localhost:3001/

### Application
Here are screenshots of the web application:<br/>

This pictures are from the model with KNN.<br/>

![app1](https://user-images.githubusercontent.com/36305738/116004900-1c9c8880-a605-11eb-8980-ffeee403dbd6.png)
![app2](https://user-images.githubusercontent.com/36305738/116004921-2f16c200-a605-11eb-8bcb-d9a0c40d031d.png)
![app3](https://user-images.githubusercontent.com/36305738/116004937-3ccc4780-a605-11eb-9359-06524155a4be.png)
![app4](https://user-images.githubusercontent.com/36305738/116004944-405fce80-a605-11eb-9b5a-d4f055132760.png)
![app5](https://user-images.githubusercontent.com/36305738/116004950-43f35580-a605-11eb-85f7-8a2564121796.png)
![app6](https://user-images.githubusercontent.com/36305738/116004953-4655af80-a605-11eb-93e2-28d3e30f04a5.png)
![app7](https://user-images.githubusercontent.com/36305738/116004954-4950a000-a605-11eb-92e7-c4ff8e67ae2e.png)
![app8](https://user-images.githubusercontent.com/36305738/116004959-4d7cbd80-a605-11eb-86f9-b57b86bb0c09.png)

### Licensing, Authors, Acknowledgements
This project was completed as part of the Udacity Data Scientist Nanodegree Program.

