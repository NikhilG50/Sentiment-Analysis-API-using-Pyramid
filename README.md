# Sentiment-Analysis-API-using-Pyramid

# Overview:
The objective of this project is to create an API endpoint that can accept a text and return associated sentiment with it Using Python Pyramid Framework. 

# Installation
  Firist you need to clone this repo and follow The below specified steps.




In this Project an Sentiment analysis binary model has been created using core concepts of Natural language processing. and the model is trained on the `airline_sentiment_analysis.csv` file. You can see how the model is trained in `Train.ipynb` which is present in the model Directory.

After training we will take the weights presnt in model named `model.pkl` and copy that to nlp folder where an Pyramid API is present.(hear you may have to dlt old `model.pkl` to use new weights)

Pyramid api is present in the folder nlp.
Now we need to activate the virtual environment where your Pyramid api is installed. after that follow the below steps,
  * `cd inside your pyrimd_"environment name"`
  * `source bin/activate`

After initializing the environment successfully, we need to install some dependencies in that environment. you can copy code from requirements.txt file and paste on the terminal to install required libraries.

before starting the server we need to setup the environment,  
  * `cd nlp/`
  * run `python setup.py develop`
it will give an url. copy and paste the Url on any browser
  
# Details and Screenshots.

This will show an input field where we can enter the text, for which we need to identify sentiment. 
################### add screenshots of the model.

after inputting the text it will redirect to another page where output of our model in Returned in json format. format details is specified below.
  * if model predicted sentiment is Positive it will return {Success:true,Sentiment:1}
  * else if the model predicted sentiment is Negative it will return {Success:true,Sentiment:0}
#####################screen shot




# Other Requirements

* Python 3.7
* Numpy
* Matplotlib
* Pyramid


