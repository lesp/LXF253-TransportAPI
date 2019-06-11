import json

with open('boxout.json') as f:
    data = json.load(f)
    #print(data)
    print(json.dumps(data, indent=4))