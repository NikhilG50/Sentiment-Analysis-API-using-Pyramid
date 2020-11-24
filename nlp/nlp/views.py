from pyramid.view import view_config;
from .main import main
import joblib
import os


@view_config(route_name='home', renderer='templates/mytemplate.jinja2')#templates/mytemplate.jinja2
def my_view(request):
    """ This Function helps to get input from the Browser
    """
    return {'project': 'nlp'}

@view_config(route_name='content', renderer='json')
def temp(request):
    """ This Function helps to display the output from the model to Browser
        Return's the output in Json Format
    """
    if request.method == 'GET':
        response = {request.GET.get('text', None)}
        # Exception Block t handle errors
        try:
            # Try to get output from our model
            model = joblib.load(os.getcwd()+'/model.pkl')
            output_array = model.predict([main.spacy_cleaner(str(response))])
            return {"Sucess": True ,'Sentiment': output_array[0].item()}

        except (ValueError, TypeError) as e:
            # If any error occurs
            return {"Sucess": False ,'Sentiment':'Null'}