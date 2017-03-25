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
        summoner_three = request.GET.get('summoner_three', None)
        summoner_four = request.GET.get('summoner_four', None)
        summoner_five = request.GET.get('summoner_five', None)
        summoner_six = request.GET.get('summoner_six', None)
        summoner_seven = request.GET.get('summoner_seven', None)
        summoner_eight = request.GET.get('summoner_eight', None)
        summoner_nine = request.GET.get('summoner_nine', None)
        summoner_ten = request.GET.get('summoner_ten', None)

        return HttpResponse(template.render(request=request, context={'summoner_one': summoner_one, 'summoner_two': summoner_two,
                                                                        'summoner_three': summoner_three, 'summoner_four': summoner_four,
                                                                        'summoner_five': summoner_five, 'summoner_six': summoner_six,
                                                                        'summoner_seven': summoner_seven, 'summoner_eight': summoner_eight,
                                                                        'summoner_nine': summoner_nine, 'summoner_ten': summoner_ten }))

