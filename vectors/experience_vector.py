def experience_vector(nlp):
    from experience.load_experience import load_experience_json
    from utils.similarity import precompute_vectors

    try:
        # LOAD JSON
        json = load_experience_json()

        # CREATE VECTOR
        vector_data = precompute_vectors(
            list_words=json, 
            nlp=nlp
        )

        return vector_data
    
    except Exception as e:
        error_msg = "Exception occured in experience_vector:" + str(e)
        # raise Exception(error_msg)
        print(error_msg)
        return None