import requests 
from requests.structures import CaseInsensitiveDict

class RestAPI:
    
    def __init__(self, domain, prefix):
        self.domain = domain
        self.prefix = prefix
        self.endpoint = self.domain + self.prefix
        self.token = ''
        self.headers = CaseInsensitiveDict()
    
    def __init__(self):
        self.domain = ''
        self.prefix = ''
        self.endpoint = self.domain + self.prefix
        self.token = ''
        self.headers = CaseInsensitiveDict()

    def getToken(self, path=str(), form=dict()):
        urlAuth = self.enviroment + path
        self.headers["Accept"] = "application/json"
        res = requests.post(url=urlAuth, data=form, headers=self.headers)
        return res.json()

    def methodGet(self, path=str()):
        url_post = self.enviroment + path
        self.headers["Accept"] = "application/json"
        self.headers["Authorization"] = "Bearer %s" % self.token
        res = requests.get(url=url_post, headers=self.headers)
        return res.json()

    def methodPost(self, path=str(), form=dict()):
        url_post = self.enviroment + path
        self.headers["Accept"] = "application/json"
        self.headers["Authorization"] = "Bearer %s" % self.token
        res = requests.post(url=url_post, data=form, headers=self.headers)
        return res.json()
    
    def existsConnection(self):
        try:
            requests.get("https://www.google.com", timeout = 5)
        except (requests.ConnectionError, requests.Timeout):
            return False
        else:
            return True