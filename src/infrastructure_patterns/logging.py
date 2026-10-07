import json

def event(name,**fields):
    return json.dumps({"event":name,**fields},sort_keys=True)
