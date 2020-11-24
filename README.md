# Sentiment-Analysis-API-using-Pyramid
The objective of this project is to create an API endpoint that can accept a text and return associated sentiment with it. 


Trained on airline_sentiment_analysis.csv file

Train the model using Train.ipynb

after training take the model.pkl file add to the nlp folder to use that weights.


activete the virtual environment where your Pyramid api is installed. 
cd inside your pyrimd_"environment name"
source bin/activate

Install all the dependinces
install all the required libraries present in requirements.txt file.


this api whould return output from our model in json format.
* if model predicted sentiment is Positive it will return {Success:true,Sentemnt:1}
* else if the model predicted sentiment is Negetive it will return {Success:true,Sentemnt:0}


python setup.py develop

Python 3.7
Pyramid

