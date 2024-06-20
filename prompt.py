import requests

# Define the API endpoint
#API_URL = "https://api-inference.huggingface.co/models/gpt2"
API_URL = "https://api-inference.huggingface.co/models/bert-base-uncased"

# Your Hugging Face API token
headers = {"Authorization": f"Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# The prompt you want to send
#prompt = "Hello, how are you?"
prompt = "I love using Hugging Face's transformers! They are [MASK]."
# Sending the prompt to the API
output = query({"inputs": prompt})

# Print the output from the API
print(output)
