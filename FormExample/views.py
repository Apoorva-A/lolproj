# importing required packages
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from RIOTAPI import RIOTAPI



# disabling csrf (cross site request forgery)
@csrf_exempt
def index(request):
    
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


@csrf_exempt
def summoner_one(request):
    if request.method == 'GET':
        template = loader.get_template('results.html')

        summoner_one = request.GET.get('summoner_one', None).replace(" ", "")
        summoner_two = request.GET.get('summoner_two', None)
        summoner_three = request.GET.get('summoner_three', None)
        summoner_four = request.GET.get('summoner_four', None)
        summoner_five = request.GET.get('summoner_five', None)
        summoner_six = request.GET.get('summoner_six', None)
        summoner_seven = request.GET.get('summoner_seven', None)
        summoner_eight = request.GET.get('summoner_eight', None)
        summoner_nine = request.GET.get('summoner_nine', None)
        summoner_ten = request.GET.get('summoner_ten', None)

        # summoner_one = summoner_one.replace(" ", "")
        summoner_two = summoner_two.replace(" ", "")
        summoner_three = summoner_three.replace(" ", "")
        summoner_four = summoner_four.replace(" ", "")
        summoner_five = summoner_five.replace(" ", "")
        summoner_six = summoner_six.replace(" ", "")
        summoner_seven = summoner_seven.replace(" ", "")
        summoner_eight = summoner_eight.replace(" ", "")
        summoner_nine = summoner_nine.replace(" ", "")
        summoner_ten = summoner_ten.replace(" ", "")



        api = RIOTAPI('RGAPI-DEBB1A9C-F681-400B-ABB1-EA9D98C88AE4')
        sum_one = api.get_summoner_by_name(summoner_one,1)
        sum_two = api.get_summoner_by_name(summoner_two,1)
        sum_three = api.get_summoner_by_name(summoner_three,1)
        sum_four = api.get_summoner_by_name(summoner_four,1)
        sum_five = api.get_summoner_by_name(summoner_five,1)
        sum_six = api.get_summoner_by_name(summoner_six,1)
        sum_seven = api.get_summoner_by_name(summoner_seven,1)
        sum_eight = api.get_summoner_by_name(summoner_eight,1)
        sum_nine = api.get_summoner_by_name(summoner_nine,1)
        sum_ten = api.get_summoner_by_name(summoner_ten,1)


        id1 = sum_one[summoner_one]["id"]
        # id2 = sum_two[summoner_two]["id"]
        # id3 = sum_three[summoner_three]["id"]
        # id4 = sum_four[summoner_four]["id"]
        # id5 = sum_five[summoner_five]["id"]
        # id6 = sum_six[summoner_six]["id"]
        # id7 = sum_seven[summoner_seven]["id"]
        # id8 = sum_eight[summoner_eight]["id"]
        # id9 = sum_nine[summoner_nine]["id"]
        # id10 = sum_ten[summoner_ten]["id"]

        a = 0
        b = 0
        c = 0
        info = api.get_summoner_by_name(str(id1),2)
        # a = info["champions"][len(info["champions"])-1]["stats"]["totalSessionsPlayed"]
        # b = info["champions"][len(info["champions"])-1]["stats"]["totalMinionKills"]

        # c = b/a




        return HttpResponse(template.render(request=request, context={'summoner_one': summoner_one, 'summoner_two': summoner_two,
                                                                        'summoner_three': summoner_three, 'summoner_four': summoner_four,
                                                                        'summoner_five': summoner_five, 'summoner_six': summoner_six,
                                                                        'summoner_seven': summoner_seven, 'summoner_eight': summoner_eight,
                                                                        'summoner_nine': summoner_nine, 'summoner_ten': summoner_ten,
                                                                        'info': info, 'y': c}))

