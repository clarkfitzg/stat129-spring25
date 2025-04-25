# /opt/anaconda/bin/ipython
# ^ run with this ^

import requests
import pandas as pd


# Path to API key file 
# You'll need to change this path if you run this on your local machine.
key_path = "/stat129/llm_api_key"

# Read the key
try:
    with open(key_path, "r") as f:
        api_key = f.read().strip()
except FileNotFoundError:
    raise Exception(f"API key file not found at {key_path}. Please create it and add your key.")


def llm(textdata,
        prompt = "summarize the following: ",
        API_URL = "https://llm.nrp-nautilus.io/v1/chat/completions",
        key = api_key):
    """
    Submit the query to the LLM
    TODO: make this function more flexible by allowing user to modify the payload
    """
    payload = {
        "model": "llama3-sdsc",  # Other options: gemma3
        "messages": [
            {"role": "user", "content": prompt + textdata},
                    ],
        #"temperature": 0.5, # Try turning this up to see creative/crazy results :)
        "max_tokens": 10,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }

    # Send the request
    response = requests.post(API_URL, json=payload, headers=headers)
    if response.ok:
        data = response.json()
        return data["choices"][0]["message"]["content"]
    else:
        return "" # Empty string indicates failure


# Read in data
christmas = pd.read_csv("/stat129/class/llm/christmas.csv")
mission = christmas["mission"]

prompt = """Give me a percentage summarizing how much the
            following nonprofit mission relates to spreading the Christian
            religion, with 0 being not at all, and 100 being the sole
            mission. Just one single number, no justification, please.

         Mission:
         """

christianity = [llm(x, prompt) for x in mission]

# Add this as an integer column to our data frame
christmas["christianity"] = [int(x) for x in christianity]

