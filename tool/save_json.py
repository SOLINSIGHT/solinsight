import json


def new_json(i,filepath):
    new_json = []
    new_json.append(i)

    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(new_json, file, ensure_ascii=False)
        # Finally, write the above list into the file according to the json dump to get the final json file
    file.close()

