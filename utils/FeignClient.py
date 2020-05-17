# coding=utf-8

import requests
import json
import random
import logging
from urllib.parse import urlparse,urlunparse

def get(url, params=None, **kwargs):
    return requests.get(get_real_url(url), params, **kwargs)


def post(url, data=None, json=None, **kwargs):
    return requests.post(get_real_url(url), data, json, **kwargs)


def put(url, data=None, **kwargs):
    return requests.put(get_real_url(url), data, **kwargs)


def delete(url, **kwargs):
    return requests.delete(get_real_url(url), **kwargs)


def get_real_url(url):
    try:
        parse_result = urlparse(url)
        host = parse_result.netloc
        response = requests.get("http://localhost:8030/hosts/"+host)
        if response.status_code != 200:
            return url
        json_result = json.loads(response.text)
        if len(json_result) == 0:
            return url

        def get_url(result):
            return f'{result["host"]}:{result["port"]}'

        url_list = list(map(get_url,json_result))
        real_url = choose_url(url_list)
        return url.replace(host,real_url,1)

    except Exception as e:
        logging.exception(e)
        return url


def choose_url(url_list):
    index = random.randint(0, len(url_list)-1)
    return url_list[index]