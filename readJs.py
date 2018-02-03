import json
json_data = '{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}'

print(json.loads(json_data))

loaded_json = json.loads(json_data)
for x in loaded_json:
    print("%s: %d" % (x, loaded_json[x]))

class Test(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)
        
test1 = Test(json_data)
print(test1.a)

with open('./testJsons/json1.json', 'r') as f:
    myJson_dict = json.load(f)
#    print(myJson_dict)

for things in myJson_dict:
    if(things == 'faceAnnotations'):
        print('************')
        print(things)
        print('************')
        for thing in myJson_dict['faceAnnotations']:
            print (thing)
    """
    for thing in things:
        print(thing)
"""