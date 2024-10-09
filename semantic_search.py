from wordllama import WordLlama
import json

# Load the default WordLlama model
wl = WordLlama.load()

# Function to match queries to image descriptions using WordLlama for similarity
def match_query_to_image_with_wordllama(queries, images):
    updated_images = []
    
    # Loop over each query
    for query in queries:
        image_descriptions = [image["desc"] for image in images]
        
        # Rank image descriptions based on their similarity to the query
        ranked_docs = wl.rank(query, image_descriptions)
        
        if ranked_docs:
            # Get the most similar description (first in ranked list)
            best_match_desc = ranked_docs[0][0]
            
            # Find the corresponding image with that description
            matched_image = next(image for image in images if image["desc"] == best_match_desc)
            updated_images.append({"query": query, "matched_image": matched_image["path"], "similarity_score": ranked_docs[0][1]})
        else:
            updated_images.append({"query": query, "matched_image": None, "similarity_score": 0.0})
    
    return updated_images

# Example input
input_data = {
    "queries": ["sunset", "beach", "mountains"],
    "images": [
        {"desc": "a beautiful sunset over the ocean", "path": "/images/sunset.jpg"},
        {"desc": "a sandy beach with palm trees", "path": "/images/beach.jpg"},
        {"desc": "snowy mountains in the winter", "path": "/images/mountains.jpg"}
    ]
}

# Get the queries and images from the input data
# queries = input_data["queries"]
# images = input_data["images"]

# # Call the function to match queries to images using WordLlama
# result = match_query_to_image_with_wordllama(queries, images)

# # Output the updated JSON with matched image paths
# output_json = json.dumps(result, indent=4)
# print(output_json)
