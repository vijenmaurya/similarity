def job_type_vector(nlp):
    from job_type.load_job_type import load_job_type_json
    from utils.similarity import precompute_vectors

    try:
        # LOAD JSON
        json = load_job_type_json()

        # CREATE VECTOR
        vector_data = precompute_vectors(
            list_words=json, 
            nlp=nlp
        )

        return vector_data
    
    except Exception as e:
        error_msg = "Exception occured in job_type_vector:" + str(e)
        # raise Exception(error_msg)
        print(error_msg)
        return None