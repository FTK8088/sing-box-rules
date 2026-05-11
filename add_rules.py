# import os
import json

def bbc_rules():
    with open('bbc.json', 'r') as f:
        data = json.load(f)

    data["rules"][0]["domain_suffix"].extend([
        "piano.io",
        "tinypass.com",
        "cxense.com"
    ])

    with open('bbc.json', 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    bbc_rules()