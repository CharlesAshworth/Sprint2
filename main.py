# Charles Ashworth
#Professor Santore
# COMP 490
# Sprint 1

import json
import sys
import requests
from requests.auth import HTTPBasicAuth

import secrets




def get_wufoo_data() -> dict:
    # URL Of the wufoo CUBES Project Proposal Submission
    url = "http://charlieashworth23.wufoo.com/api/v3/forms/zv9axo1n8asf9/entries/json"
    response = requests.get(url, auth=HTTPBasicAuth(secrets.wufoo_key, 'pass'))
    print(response.text)

    if response.status_code != 200:  # if we don't get an ok response we have trouble

        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason}")
        sys.exit(-1)
    json_response = response.json()
    return json_response

## This will write the data to the file using the json library.
def write_data_to_file():
    data = get_wufoo_data()['Entries']

    with open("w_data.txt", "w") as outfile:
        for item in data:
            for key, value in item.items():
                outfile.write(f"{key}: {value}\n")

    print_wfile("w_data.txt")

    ## This will print the data from the file "w_data.txt"
def print_wfile(file_name):
    with open(file_name) as wufoo:
        print(wufoo.read())


if __name__ == "__main__":
    write_data_to_file()
