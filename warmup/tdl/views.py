from models import To_do
from django.shortcuts import render_to_response
import os

STATIC_URL = os.path.dirname(os.path.dirname('__init__'))
 
def index(request): #Define our function, accept a request
 
    items = To_do.objects.all() #ORM queries the database for all of the to-do entries.
 
    return render_to_response('index.html', {'items': items, 'STATIC_URL': os.path.join(STATIC_URL,'/static/')}) #Responds with passing the object items (contains info from the DB) to the template index.html

