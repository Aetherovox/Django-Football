import requests
import json
import io
from rest_framework.parsers import JSONParser


# NOTE:
#   - Django handles request from multiple users via multithreading
#   - I won't need to use async libraries providing the user is making one request at a time

class LeagueData:
    def __init__(self,league_id):
        self.base_url = "https://football-web-pages1.p.rapidapi.com"
        self.headers = {
        'x-rapidapi-host': "football-web-pages1.p.rapidapi.com",
        'x-rapidapi-key': "af7822929emshdd2aef6b991faf0p1a1627jsn882dc1fc0738"
        }
        self.league_id = league_id
        self.querystring = {"comp":f"{self.league_id}"}

    def get_league_fixtures(self):
        """:return list of python dictionaries"""
        url = "/".join((self.base_url,"/fixtures-results.json"))
        response = requests.request("GET", url, headers=self.headers, params=self.querystring).json()
        response_data = response["fixtures-results"]["matches"]
        renames = {'home-team':'home_team','away-team':'away_team'}
        res = list(map(lambda x: Cleaner.clean(dict(x),rename=renames,remove=('attendance',)),response_data))
        # print(res)
        return res

    def get_teams(self):
        url = "/".join((self.base_url, "/teams.json"))
        response = requests.request("GET", url, headers=self.headers, params=self.querystring).json()
        renames = {'short-name':'short_name','full-name':'full_name'}
        res = list(map(lambda x: Cleaner.clean(dict(x),rename=renames),response["teams"]))
        print(res)
        return res




class Cleaner:
    def __init__(self,data,rename = None,remove = None,make_id=None):
        self.data = data
        self.__renames = rename
        self.__removes = remove
        self.__ids = make_id

    def __rename_keys(self):
        if self.__renames is None:
            return
        for _from, _to in self.__renames.items():
            self.data[_to] = self.data.pop(_from)
        return

    def __remove_keys(self):
        if self.__removes is None:
            return
        for key in self.__removes:
            del self.data[key]

    def __id_keys(self):
        if self.__ids is None:
            return
        for key in self.__ids:
            self.data[f'{key}_id'] = self.data.pop(key)

    @classmethod
    def clean(cls,data,rename = None,remove = None,make_id=None):
        c = cls(data,rename,remove,make_id)
        c.__rename_keys()
        c.__remove_keys()
        c.__id_keys()
        return c.data


