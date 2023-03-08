import json

def sort_by_price_ascending(json_string):
    data = json.loads(json_string)

    data.sort(key=lambda x: x["price"])
    
    return json.dumps(data)

print(sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'))