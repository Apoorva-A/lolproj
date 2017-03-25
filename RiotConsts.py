URL = {
    #/api/lol/{region}/v1.4/summoner/by-name/{summonerNames}

    'base1': 'https://{proxy}.api.pvp.net/api/lol/{region}/{url}',
    'summoner_by_name1': 'v{version}/summoner/by-name/{names}',


    # /api/lol/{region}/v1.3/stats/by-summoner/{summonerId}/ranked
    'base2': 'https://{proxy}.api.pvp.net/api/lol/{region}/{url}',
    'summoner_by_name2': 'v{version}/stats/by-summoner/{names}/ranked'
}

API_VERSIONS = {
    'summoner1': '1.4',
    'summoner2': '1.3'
}

REGIONS = {
    'here': 'NA'
}