from django.shortcuts import render

# index view
def index(request):
    '''
    This view will be responsible for dislaying the home page once the url is called
    '''
    return render(request,'smartfarm/index.html')