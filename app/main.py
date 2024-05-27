from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer, util
import json
import os
import openai
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from a .env file
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to load JSON files
def load_data():
    data = []
    data_dir = 'data'
    for file_name in os.listdir(data_dir):
        if file_name.endswith('.json'):
            with open(os.path.join(data_dir, file_name)) as f:
                data.extend(json.load(f))
    return data

# Load all data
business_data = load_data()

# Initialize the model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Precompute embeddings for the business data
data_embeddings = model.encode([json.dumps(item) for item in business_data], convert_to_tensor=True)

@app.route('/api/query', methods=['POST'])
def query():
    user_query = request.json.get('query')
    answer = generate_answer(user_query)
    return jsonify({'answer': answer})

def generate_answer(query):
    # Encode the user query
    query_embedding = model.encode(query, convert_to_tensor=True)
    # Retrieve the most similar data
    results = util.semantic_search(query_embedding, data_embeddings, top_k=1)
    relevant_data_index = results[0][0]['corpus_id']
    relevant_data = business_data[relevant_data_index]

    # Generate response using OpenAI's GPT-4
    response = openai.Completion.create(
        engine="text-davinci-004",
        prompt=f"Based on the following information, answer the question:\n\n{json.dumps(relevant_data)}\n\nQuestion: {query}\nAnswer:",
        max_tokens=150
    )

    return response.choices[0].text.strip()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)