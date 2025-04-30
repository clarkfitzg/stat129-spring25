import requests
import os

# Path to API key file in home directory
key_path = os.path.expanduser("/stat129/llm_api_key")

# Read the key
try:
    with open(key_path, "r") as f:
        api_key = f.read().strip()
except FileNotFoundError:
    raise Exception(f"API key file not found at {key_path}. Please create it and add your key.")

# Base URL and endpoint
LITE_LLM_API_URL = "https://llm.nrp-nautilus.io/v1/chat/completions"

# Request payload
payload = {
    "model": "llama3-sdsc",  # Other options: gemma3
    "messages": [
        {"role": "user", "content": """
Who's the cat who won't cop out, when there's danger all about?
        """},
    ],
    "temperature": 0.5, 
    "max_tokens": 30
}


# Headers with your API key
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Send the request
response = requests.post(LITE_LLM_API_URL, json=payload, headers=headers)

# Handle response
if response.ok:
    data = response.json()
    answer = data["choices"][0]["message"]["content"]
    print("Response:", answer)
else:
    print(f"Error {response.status_code}: {response.text}")
