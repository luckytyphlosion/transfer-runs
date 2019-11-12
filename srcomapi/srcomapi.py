import requests
from http.client import responses
from os.path import dirname
from os import environ
import inspect
import time

import srcomapi
import srcomapi.datatypes as datatypes
from .exceptions import APIRequestException, APINotProvidedException

# libraries for mocking
import json
import gzip

with open(dirname(srcomapi.__file__) + "/.version") as f:
    __version__ = f.read().strip()
API_URL = "https://www.speedrun.com/api/v1/"
TEST_DATA = dirname(srcomapi.__file__) + "/test_data/"

class SpeedrunCom(object):
    def __init__(self, api_key=None, user_agent="blha303:srcomapi/"+__version__, mock=False):
        self._datatypes = {v.endpoint:v for k,v in inspect.getmembers(datatypes, inspect.isclass) if hasattr(v, "endpoint")}
        self.api_key = api_key
        self.user_agent = user_agent
        self.mock = mock
        self.debug = 0
        self.start_time = time.time()
        self.use_count = 0

    def get(self, endpoint, keep_pagination=False, full_request=False, **kwargs):
        self.wait_rate_limit()

        headers = {"User-Agent": self.user_agent}
        if self.api_key:
            headers["X-API-Key"] = self.api_key
        kwargs.update({"headers": headers})
        if full_request:
            uri = endpoint
        else:
            uri = API_URL + endpoint

        if self.debug >= 1: print(uri)
        if self.mock:
            mock_endpoint = ".".join(endpoint.split("/")[0::2])
            try:
                with gzip.open(TEST_DATA + mock_endpoint + ".json.gz") as f:
                    data = json.loads(f.read().decode("utf-8"))["data"]
            except FileNotFoundError:
                response = requests.get(uri, **kwargs)
                if response.status_code != 404:
                    with gzip.open(TEST_DATA + mock_endpoint + ".json.gz", "wb") as f:
                        f.write(json.dumps(response.json()).encode("utf-8"))
                    data = response.json()["data"]
                else:
                    raise APIRequestException((response.status_code, responses[response.status_code], uri[len(API_URL):]), response)
        else:
            response = requests.get(uri, **kwargs)
            if response.status_code == 404:
                raise APIRequestException((response.status_code, responses[response.status_code], uri[len(API_URL):]), response)
            if keep_pagination:
                data = response.json()
            else:
                data = response.json()["data"]

        return data

    def post(self, endpoint, data, **kwargs):
        self.wait_rate_limit()
        headers = {"User-Agent": self.user_agent}
        if self.api_key:
            headers["X-API-Key"] = self.api_key
        kwargs.update({"headers": headers})
        uri = API_URL + endpoint

        response = requests.post(uri, json=data, **kwargs)
        if response.status_code == 404 or response.status_code == 500:
            raise APIRequestException((response.status_code, responses[response.status_code], uri[len(API_URL):]), response)
        
        out_data = response.json()

        return out_data

    def wait_rate_limit(self):
        if self.use_count == 100:
            print("Waiting to pass rate limit")
            while time.time() - self.start_time < 60:
                time.sleep(1)
            self.start_time = time.time()
            self.use_count = 0
        else:
            self.use_count += 1

    def get_game(self, id, **kwargs):
        self.wait_rate_limit()
        return datatypes.Game(self, data=self.get("games/" + id))

    def get_request(self, req, **kwargs):
        self.wait_rate_limit()
        return self.get(req)
