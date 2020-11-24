# Sentiment-Analysis-API-using-Pyramid

# Overview:
The objective of this project is to create an API endpoint that can accept a text and return associated sentiment with it Using Python Pyramid Framework. 

> To see a Sample demo of this model play "demo.mp4" file.

# Installation
  Firist you need to clone this repo and follow The below specified steps.




In this Project an Sentiment analysis binary model has been created using core concepts of Natural language processing. and the model is trained on the `airline_sentiment_analysis.csv` file. You can see how the model is trained in `Train.ipynb` which is present in the model Directory.

After training we will take the weights presnt in model named `model.pkl` and copy that to nlp folder where an Pyramid API is present.(hear you may have to dlt old `model.pkl` to use new weights)

Pyramid api is present in the folder nlp.
Now we need to activate the virtual environment where your Pyramid api is installed. after that follow the below steps,
  * `cd "inside your pyrimd_environment"`
  * `source bin/activate`

After initializing the environment successfully, we need to install some dependencies in that environment. you can copy code from requirements.txt file and paste on the terminal to install required libraries.

before starting the server we need to setup the environment,  
  * `cd nlp/`
  * run `python setup.py develop`
  * after that run `pserve development.ini` to start Server
it will give an url. copy and paste the Url on any browser
  
# Details and Screenshots.

* Below given image will show an input field where we can enter the text, for which we need to identify sentiment. after typing a text click on submit Button.
![alt text](https://github.com/NikhilG50/Sentiment-Analysis-API-using-Pyramid/blob/main/images/input.png)


* After inputting the text it will redirect to another page where output of our model in Returned in json format. format details is specified below.
    * if model predicted sentiment is Positive it will return {Success:true,Sentiment:1}
    * else if the model predicted sentiment is Negative it will return {Success:true,Sentiment:0}
  
Below is the image which showes the output Window on browser. 
![alt text](https://github.com/NikhilG50/Sentiment-Analysis-API-using-Pyramid/blob/main/images/output.png)

### Note: This project only focuses on Backend part. you can easily edit this using front end web technologies.

# Other Requirements

* Python 3.7
* Numpy
* Matplotlib
* Pyramid

### Thank You.

