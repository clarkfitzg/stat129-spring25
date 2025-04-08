import requests
import os

# Path to API key file in home directory
key_path = os.path.expanduser("~/.llm_api_key")

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
    "model": "llama3-sdsc",
    "messages": [
        {"role": "user", "content": "What's the capital of Japan?"}
    ],
    "temperature": 0.7,
    "max_tokens": 100
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
    print("Response:", data["choices"][0]["message"]["content"])
else:
    print(f"Error {response.status_code}: {response.text}")
