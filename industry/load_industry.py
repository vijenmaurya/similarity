import json

def load_and_transform_data(json_file):
    with open(json_file, 'r') as file:
        records = json.load(file)
    
    return {x['industry']: x['industry_synonyms'] for x in records}

def load_industry_json():
    json_file = 'industry/industries.json'
    return load_and_transform_data(json_file)