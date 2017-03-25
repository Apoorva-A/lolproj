from RIOTAPI import RIOTAPI
def main():
    api = RIOTAPI('RGAPI-DEBB1A9C-F681-400B-ABB1-EA9D98C88AE4')
    r = api.get_summoner_by_name('wat up7',1)
    #.replace(" ", "")

    id = r["watup7"]["id"]

    print(id)
    s = api.get_summoner_by_name(str(id),2)
    print(s)
if __name__ == "__main__":
    main()