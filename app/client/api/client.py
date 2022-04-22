import requests 
from requests.structures import CaseInsensitiveDict

class RestAPI:
    
    def __init__(self):
        self.endpoint = ''
        self.token = ''
        self.headers = CaseInsensitiveDict()

    def getToken(self, path=str(), form=dict()):
        urlAuth = self.endpoint + path
        self.headers["Accept"] = "application/json"
        res = requests.post(url=urlAuth, data=form, headers=self.headers)
        return res.json()

    def methodGet(self, path=str()):
        url_get = self.endpoint + path
        self.headers["Accept"] = "application/json"
        #self.headers["Authorization"] = "Bearer %s" % self.token
        #res = requests.get(url=url_get, headers=self.headers)
        res = requests.get(url=url_get, headers=self.headers)
        return res.json()

    def methodPost(self, path=str(), form=dict()):
        url_post = self.endpoint + path
        self.headers["Accept"] = "application/json"
        #self.headers["Authorization"] = "Bearer %s" % self.token
        res = requests.post(url=url_post, data=form, headers=self.headers)
        return res.json()
    
    def existsConnection(self):
        try:
            requests.get("https://www.google.com", timeout = 5)
        except (requests.ConnectionError, requests.Timeout):
            return False
        else:
            return True