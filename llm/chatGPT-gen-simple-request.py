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
Summarize the following description in 5 to 10 words.
Put the words in root/infinitive form with no concern for grammar, explanations, or formatting.

TO PROMOTE AND SUPPORT ALL OF PERKINS STUDENT ATHLETES AND SPORTS PROGRAMS. GAINING SUPPORT THROUGH POSITIVE PARENT AND COMMUNITY INVOLVEMENT TO GIVE EVERY STUDENT ATHLETE A POSITIVE EXPERIENCE IN ATHLETICS. THE PABC RAISES MONEY THROUGH DIFFERENT EVENTS THROUGHOUT THE YEAR TO ASSIST OUR STUDENT ATHLETES AND OUR SPORTS PROGRAMS; TO CONTRIBUTE TO THE SPIRIT AND ENTHUSIASM OF PERKINS ATHLETICS AND THE PERKINS COMMUNITY. MAINTAINING THE RICH TRADITION AND HISTORY OF EXCELLENCE IN BOTH ACADEMICS AND ATHLETICS AT PERKINS SCHOOLS.
        """},
    ],
    "temperature": 0.5, 
    "max_tokens": 10
}

# Three parameters to experiment with:

# 1. prompt
# 2. model
# 3. temperature: 
#   - 0 (predictable) 
#   - 0.7 (good mix)
#   - 2 (random)

# Observations:
# - The two models I tried returned the same output for temperatures 0 and 1. Different for 2.
# - Results appear to be cached, so resending the same request with a high temperature doesn't create a new random result.


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
