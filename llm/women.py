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
        key = api_key,
        model = "llama3-sdsc",  # Other options: gemma3
        max_tokens = 10,
        temperature = 0.5,  # Turn this up for more unpredictability ;)
        kwargs = {},
        ):
    """
    Submit the query to the LLM

    There are other arguments as well:
    https://docs.litellm.ai/docs/completion/input#optional-fields
    """
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt + textdata},
                    ],
        "max_tokens": max_tokens,
        "temperature": temperature,
        **kwargs
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
women = pd.read_csv("/stat129/class/llm/women.csv")
mission = women["mission"]

prompt = """Is the following nonprofit most related to health, education, civil rights, sports, or other?
Just one or two words please, no explanation.

         Mission:
         """

category = [llm(x, prompt, temperature=2) for x in mission]

# Add this as a column to our data frame
women["category"] = category
