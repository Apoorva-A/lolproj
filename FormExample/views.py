# importing required packages
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


# disabling csrf (cross site request forgery)
@csrf_exempt
def index(request):
    
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


@csrf_exempt
def summoner_one(request):
    if request.method == 'GET':
        template = loader.get_template('results.html')
        summoner_one = request.GET.get('summoner_one', None)
        summoner_two = request.GET.get('summoner_two', None)


        return HttpResponse(template.render(request=request, context={'summoner_one': summoner_one, 'summoner_two': summoner_two}))
