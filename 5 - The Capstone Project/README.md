# The Capstone Project: Help navigate the robots!

## File description:<br />
1. Folder Data (contains the data needed for this project, separated into X_train, X_test and Y_train);<br />
2. README file;<br />
3. Main script: navigation_robots.ipynb;<br />
4. Model folder with Trained model: model.pkl;<br />
5. Wrangling scripts.<br />
6. myapp<br/>
7. myapp.py<br/>
8. pdf document: Capstone project, with description for every section of the project.<br/>

## Libraries:
1. Numpy<br />
2. Pandas<br />
3. Matplotlib<br />
4. Seaborn<br />
5. Math<br />
6. Scipy<br />
7. Scikit-learn<br />
8. Pickle<br />

## Descripiton and motivation:
This project is part of the Udacity Nanodegree Program, as a final project. The project is published on [Kaggle](https://www.kaggle.com/c/career-con-2019). I wanted to do something different, so I choosed this project on my own.<br />
The main goal is to build a model that will predict on what type of floor the robot is standing and in that way, we can improve the robots navigation. I used cross-validation and Random Forest Classifier, and the accuracy of the best model is around 95%. There are still improvements that can be made, but for now, this is satisfying.<br/>

## Web application
In order to run the web application, you need to have installed Flask. <br/>
Open your terminal, go into the folder with all this files, enter python myapp.py in your terminal <br/>
Open: http://localhost:3001<br/>
You will see plots of the distribution of the X,Y,Z and W orientations. Enter a number of series_id on which you want to see the distribution.<br/>
![tempsnip](https://user-images.githubusercontent.com/36305738/122585916-4ea5f600-d05c-11eb-8f15-23dab115aa75.png)
![222](https://user-images.githubusercontent.com/36305738/122585954-58c7f480-d05c-11eb-906d-0c4acfcef4bf.png)

In this web application, we have only shown the distribution of the orientation, all other details about the data and explanations are in the jupyternotebook.

## Licensing, Authors, Acknowledgements
This project is part of Data Scientist Nanodegree - Udacity.<br/>


