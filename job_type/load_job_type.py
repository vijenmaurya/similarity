import json

def load_and_transform_data(json_file):
    with open(json_file, 'r') as file:
        records = json.load(file)
    
    return {x['job_type']: x['job_type_synonyms'] for x in records}

def load_job_type_json():
    json_file = 'job_type/job_types.json'
    return load_and_transform_data(json_file)