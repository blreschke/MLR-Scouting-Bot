import urllib.request
import json

def stringFromSource(source):
    with urllib.request.urlopen(source) as url:
        data = url.read().decode()
    return data

def dictFromSource(source):
    with urllib.request.urlopen(source) as url:
        data = json.loads(url.read())
    return data