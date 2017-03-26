# importing required packages
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from RIOTAPI import RIOTAPI
import time


# disabling csrf (cross site request forgery)
@csrf_exempt
def index(request):
    
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


@csrf_exempt
def calculate(request):
    if request.method == 'GET':
        template = loader.get_template('results.html')

        #Get Summoner Names
        summoner_one = request.GET.get('summoner_one', None).replace(" ", "").lower()
        summoner_two = request.GET.get('summoner_two', None).replace(" ", "").lower()
        summoner_three = request.GET.get('summoner_three', None).replace(" ", "").lower()
        summoner_four = request.GET.get('summoner_four', None).replace(" ", "").lower()
        summoner_five = request.GET.get('summoner_five', None).replace(" ", "").lower()
        summoner_six = request.GET.get('summoner_six', None).replace(" ", "").lower()
        summoner_seven = request.GET.get('summoner_seven', None).replace(" ", "").lower()
        summoner_eight = request.GET.get('summoner_eight', None).replace(" ", "").lower()
        summoner_nine = request.GET.get('summoner_nine', None).replace(" ", "").lower()
        summoner_ten = request.GET.get('summoner_ten', None).replace(" ", "").lower()

        #Get Summoner ID's
        api = RIOTAPI('RGAPI-DEBB1A9C-F681-400B-ABB1-EA9D98C88AE4')
        sum_one = api.get_summoner_by_name(summoner_one,1)
        time.sleep(5)

        sum_two = api.get_summoner_by_name(summoner_two,1)
        time.sleep(5)
        sum_three = api.get_summoner_by_name(summoner_three,1)
        sum_four = api.get_summoner_by_name(summoner_four,1)
        sum_five = api.get_summoner_by_name(summoner_five,1)
        time.sleep(10)
        sum_six = api.get_summoner_by_name(summoner_six,1)
        sum_seven = api.get_summoner_by_name(summoner_seven,1)
        sum_eight = api.get_summoner_by_name(summoner_eight,1)
        time.sleep(10)
        sum_nine = api.get_summoner_by_name(summoner_nine,1)
        sum_ten = api.get_summoner_by_name(summoner_ten,1)
        time.sleep(10)


        id1 = sum_one[summoner_one]["id"]
        id2 = sum_two[summoner_two]["id"]
        id3 = sum_three[summoner_three]["id"]
        id4 = sum_four[summoner_four]["id"]
        id5 = sum_five[summoner_five]["id"]
        id6 = sum_six[summoner_six]["id"]
        id7 = sum_seven[summoner_seven]["id"]
        id8 = sum_eight[summoner_eight]["id"]
        id9 = sum_nine[summoner_nine]["id"]
        id10 = sum_ten[summoner_ten]["id"]

        ##Average Creep Score

        info = api.get_summoner_by_name(str(id1),2)
        sum_one_cs = info["champions"][len(info["champions"])-1]["stats"]["totalMinionKills"] / info["champions"][len(info["champions"])-1]["stats"]["totalSessionsPlayed"]
        time.sleep(5)

        info2 = api.get_summoner_by_name(str(id2),2)
        sum_two_cs = info2["champions"][len(info2["champions"])-1]["stats"]["totalMinionKills"] / info2["champions"][len(info2["champions"])-1]["stats"]["totalSessionsPlayed"]
        
        info3 = api.get_summoner_by_name(str(id3),2)
        sum_three_cs = info3["champions"][len(info3["champions"])-1]["stats"]["totalMinionKills"] / info3["champions"][len(info3["champions"])-1]["stats"]["totalSessionsPlayed"]
        time.sleep(10)
        info4 = api.get_summoner_by_name(str(id4),2)
        sum_four_cs = info4["champions"][len(info4["champions"])-1]["stats"]["totalMinionKills"] / info4["champions"][len(info4["champions"])-1]["stats"]["totalSessionsPlayed"]
        
        info5 = api.get_summoner_by_name(str(id5),2)
        sum_five_cs = info5["champions"][len(info5["champions"])-1]["stats"]["totalMinionKills"] / info5["champions"][len(info5["champions"])-1]["stats"]["totalSessionsPlayed"]
        time.sleep(5)
        info6 = api.get_summoner_by_name(str(id6),2)
        sum_six_cs = info6["champions"][len(info6["champions"])-1]["stats"]["totalMinionKills"] / info6["champions"][len(info6["champions"])-1]["stats"]["totalSessionsPlayed"]
        
        info7 = api.get_summoner_by_name(str(id7),2)
        sum_seven_cs = info7["champions"][len(info7["champions"])-1]["stats"]["totalMinionKills"] / info7["champions"][len(info7["champions"])-1]["stats"]["totalSessionsPlayed"]
        time.sleep(10)
        info8 = api.get_summoner_by_name(str(id8),2)
        sum_eight_cs = info8["champions"][len(info8["champions"])-1]["stats"]["totalMinionKills"] / info8["champions"][len(info8["champions"])-1]["stats"]["totalSessionsPlayed"]
        
        info9 = api.get_summoner_by_name(str(id9),2)
        sum_nine_cs = info9["champions"][len(info9["champions"])-1]["stats"]["totalMinionKills"] / info9["champions"][len(info9["champions"])-1]["stats"]["totalSessionsPlayed"]
        time.sleep(10)

        info10 = api.get_summoner_by_name(str(id10),2)
        sum_ten_cs = info10["champions"][len(info10["champions"])-1]["stats"]["totalMinionKills"] / info10["champions"][len(info10["champions"])-1]["stats"]["totalSessionsPlayed"]
        

        return HttpResponse(template.render(request=request, context={'summoner_one': summoner_one, 'summoner_two': summoner_two,
                                                                        'summoner_three': summoner_three, 'summoner_four': summoner_four,
                                                                        'summoner_five': summoner_five, 'summoner_six': summoner_six,
                                                                        'summoner_seven': summoner_seven, 'summoner_eight': summoner_eight,
                                                                        'summoner_nine': summoner_nine, 'summoner_ten': summoner_ten,
                                                                        'info': info, 'sum_one_cs': sum_one_cs, 'sum_two_cs': sum_two_cs,
                                                                        'sum_three_cs': sum_three_cs, 'sum_four_cs':sum_four_cs,
                                                                        'sum_five_cs':sum_five_cs, 'sum_six_cs':sum_six_cs,
                                                                        'sum_seven_cs':sum_seven_cs, 'sum_eight_cs':sum_eight_cs,
                                                                        'sum_nine_cs':sum_nine_cs, 'sum_ten_cs':sum_ten_cs}))

