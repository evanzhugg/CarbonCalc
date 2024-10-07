import json
def dump(data):
    json_object = json.dumps(data, indent = 4)

    with open("data.json", "w") as outfile:
        outfile.write(json_object)

