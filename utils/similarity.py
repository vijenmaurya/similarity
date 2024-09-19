import numpy as np

# FUNCTION TO PRECOMPUTE VECTORS FOR INDUSTRY SYNONYMS
def precompute_vectors(list_words, nlp):
    vector_data = {}
    all_texts = []
    industry_to_index = {}
    
    for industry, synonyms in list_words.items():
        all_texts.append(industry)
        industry_to_index[industry] = len(all_texts) - 1  # SAVE INDEX OF INDUSTRY
        
        for synonym in synonyms:
            all_texts.append(synonym)

    # PROCESS ALL TEXTS IN ONE GO USING NLP.PIPE() FOR EFFICIENCY
    doc_vectors = [doc.vector if doc.has_vector else None for doc in nlp.pipe(all_texts)]
    
    # Reconstruct the vector data structure
    for industry, synonyms in list_words.items():
        industry_idx = industry_to_index[industry]
        industry_vector = doc_vectors[industry_idx]
        
        synonym_vectors = [doc_vectors[industry_idx + 1 + i] for i in range(len(synonyms)) if doc_vectors[industry_idx + 1 + i] is not None]
        
        vector_data[industry] = (industry_vector, synonym_vectors)
    
    return vector_data

# FUNCTION TO CALCULATE COSINE SIMILARITY BETWEEN TWO VECTORS
def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

# FUNCTION TO FIND THE BEST INDUSTRY MATCH FOR A GIVEN WORD
def find_best_match(word, vector_data, nlp, list_words):
    exact_word = word
    word = str(word).lower()
    
    # DIRECT MATCH FIRST
    for industry, synonyms in list_words.items():
        if word == industry or word in synonyms:
            return industry
        
    # COMPUTE THE VECTOR FOR THE INPUT WORD
    word_vector = nlp(word).vector if nlp(word).has_vector else None
    if word_vector is None:
        return exact_word
    
    best_match = None
    best_similarity = -1
    
    for industry, (industry_vector, synonym_vectors) in vector_data.items():
        # CALCULATE SIMILARITY FOR THE INDUSTRY NAME
        if industry_vector is not None:
            industry_similarity = cosine_similarity(word_vector, industry_vector)
            if industry_similarity > best_similarity:
                best_similarity = industry_similarity
                best_match = industry
        
        # CALCULATE SIMILARITY FOR ALL SYNONYMS
        for synonym_vector in synonym_vectors:
            similarity = cosine_similarity(word_vector, synonym_vector)
            if similarity > best_similarity:
                best_similarity = similarity
                best_match = industry
    
    return best_match
