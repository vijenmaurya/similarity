import json

def load_and_transform_data(json_file):
    with open(json_file, 'r') as file:
        records = json.load(file)
    
    return {x['experience']: x['experience_synonyms'] for x in records}

def load_experience_json():
    json_file = 'experience/experiences.json'
    return load_and_transform_data(json_file)