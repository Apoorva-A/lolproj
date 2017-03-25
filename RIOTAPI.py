import RiotConsts as Consts
import requests
class RIOTAPI(object):

    def __init__(self, api_key, region = Consts.REGIONS['here']):
        self.api_key = api_key
        self.region = region

    def request(self, choice, api_url, params={},):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key]=value
        if(choice==1):
            response = requests.get(
                Consts.URL['base1'].format(
                    proxy=self.region,
                    region=self.region,
                    url=api_url
                    ),
                params=args
                )
        else:
            response = requests.get(
                Consts.URL['base2'].format(
                    proxy=self.region,
                    region=self.region,
                    url=api_url
                ),
                params=args
            )
        print (response.url)
        return response.json()

    def get_summoner_by_name(self, name, choice):
        if choice == 1:
            api_url = Consts.URL['summoner_by_name1'].format(
                version=Consts.API_VERSIONS['summoner1'],
                names=name
                )
        else:
            api_url = Consts.URL['summoner_by_name2'].format(
                version=Consts.API_VERSIONS['summoner2'],
                names=name
                )
        return self.request(choice, api_url)