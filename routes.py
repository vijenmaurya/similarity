from flask import Blueprint, request, jsonify
import spacy

from experience.load_experience import load_experience_json
from vectors.experience_vector import experience_vector
from job_type.load_job_type import load_job_type_json
from industry.load_industry import load_industry_json
from vectors.job_type_vector import job_type_vector
from vectors.industry_vector import industry_vector
from utils.similarity import find_best_match

# API Blueprint
api = Blueprint('api', __name__)

# LOAD NLP
nlp = spacy.load('en_core_web_md')

# INDUSTRY VECTOR
industry_vector_data = industry_vector(nlp=nlp)

# EXPERIENCE VECTOR
experience_vector_data = experience_vector(nlp=nlp)

# JOB TYPE VECTOR
job_type_vector_data = job_type_vector(nlp=nlp)

# ROUTE TO CHECK INDUSTRY SIMILARITY
@api.route('/api/industry/similarity', methods=['POST'])
def check_industry_similarity():
    data = request.get_json()
    
    if not isinstance(data, list):
        return jsonify({"error": "Request body should be a list of words"}), 400
    
    # LOAD INDUSTRY JSON
    industry_json = load_industry_json()

    result = {}

    # FIND SIMILAR DATA
    for word in data:
        result[word] = find_best_match(
            list_words=industry_json,
            vector_data=industry_vector_data, 
            word=word, 
            nlp=nlp, 
        )
    
    return jsonify(result)

# ROUTE TO CHECK EXPERIENCE SIMILARITY
@api.route('/api/experience/similarity', methods=['POST'])
def check_education_similarity():
    data = request.get_json()
    
    if not isinstance(data, list):
        return jsonify({"error": "Request body should be a list of words"}), 400
    
    # LOAD EXPERIENCE JSON
    experience_json = load_experience_json()

    result = {}

    # FIND SIMILAR DATA
    for word in data:
        result[word] = find_best_match(
            list_words=experience_json,
            vector_data=experience_vector_data, 
            word=word,
            nlp=nlp
        )
    
    return jsonify(result)

# ROUTE TO CHECK JOB TYPE SIMILARITY
@api.route('/api/job-type/similarity', methods=['POST'])
def check_job_type_similarity():
    data = request.get_json()
    
    if not isinstance(data, list):
        return jsonify({"error": "Request body should be a list of words"}), 400
    
    # LOAD JOB TYPE JSON
    job_type_json = load_job_type_json()

    result = {}

    # FIND SIMILAR DATA
    for word in data:
        result[word] = find_best_match(
            list_words=job_type_json,
            vector_data=job_type_vector_data, 
            word=word,
            nlp=nlp
        )
    
    return jsonify(result)

# ROUTE TO CHECK SERVER STATUS
@api.route('/api/status', methods=['GET'])
def status():
    return jsonify({"status": "API is running"})
