# /opt/anaconda/bin/ipython
# ^ run with this ^

# Definitely should clean this up before giving it to students!

import csv
import os
import random
import sys

import requests
from lxml import etree


def extract(xmlfile):
    tree = etree.parse(xmlfile)
    try:
        ein = str(tree.xpath("//Filer//EIN/text()")[0])
        name = str(tree.xpath("//Filer//BusinessNameLine1Txt/text()")[0])


# Just paste together all text relating to the mission
        mission = tree.xpath("//ActivityOrMissionDesc/text()")
        mission += tree.xpath("//MissionDesc/text()")
        mission += tree.xpath("//IRS990/Desc/text()")
# ChatGPT generated, sweet!
        mission += tree.xpath('//SupplementalInformationDetail[FormAndLineReferenceDesc="FORM 990 - ORGANIZATION\'S MISSION"]/ExplanationTxt/text()')
        mission += tree.xpath("//PrimaryExemptPurposeTxt/text()")
        mission = " ".join(mission)
        mission = mission.replace("\n", " ")

        # Failed to extract
        if mission == "":
            return None
    except:
        return None

    # A dictionary holding all the results
    result = {"ein": ein, "name": name, "file": xmlfile, "mission": mission}
    return result

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

def summarize(mission):
    payload = {
        "model": "llama3-sdsc",  # Other options: gemma3
        "messages": [
            {"role": "user", "content": """
Summarize the following description in 5 to 10 words.
Put the words in root/infinitive form with no concern for grammar, explanations, or formatting.
        """ + mission},
                    ],
        #"temperature": 0.5, 
        "max_tokens": 10,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Send the request
    response = requests.post(LITE_LLM_API_URL, json=payload, headers=headers)
    if response.ok:
        data = response.json()
        return data["choices"][0]["message"]["content"]
    else:
        return None


datadir = "/stat129/tax23/"

all990 = [datadir + p for p in os.listdir(datadir)]

# Working with a small sample is easier
# Setting the seed here guarantees the same random sample
random.seed(286349) 
n = 10
s990 = random.sample(all990, n)

# Develop a function by starting with just one.
xmlfile = s990[1]

if True:
    writer = csv.DictWriter(sys.stdout, fieldnames = "ein name file summary mission".split())
    writer.writeheader()
    #for f in s990: # sample
    for f in all990:
        row = extract(f)
        if row is not None:
            row["summary"] = summarize(row["mission"])
            writer.writerow(row)
