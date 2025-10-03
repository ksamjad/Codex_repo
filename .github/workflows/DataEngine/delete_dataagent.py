import requests
import json
import os
import sys
import subprocess

# Replace with your actual values
PROJECT_NUMBER = '362440398011'
LOCATION = 'global'
ENGINE_ID = 'agentspace-test-bot1_1744872480618'
AGENT_ID = '10521090652494292424'
AGENT_RESOURCE_NAME = 'projects/362440398011/locations/global/collections/default_collection/engines/agentspace-test-bot1_1744872480618/assistants/default_assistant/agents/6806780255366687791'

#PROJECT_NUMBER = "994041294907"
#LOCATION = "global"
#ENGINE_ID = "agentspace-demo_1753289817401"
#AGENT_ID = "18272621115287692047"
#AGENT_RESOURCE_NAME = "projects/994041294907/locations/global/collections/default_collection/engines/agentspace-demo_1753289817401/assistants/default_assistant/agents/7585199406368048969"

def get_access_token():
    """
    Retrieves a Google Cloud access token using the gcloud CLI.
    """
    try:
        # Check if gcloud is installed
        subprocess.run(["gcloud", "--version"], check=True, capture_output=True, shell=True)
    except FileNotFoundError:
        print("Error: The 'gcloud' command-line tool is not found.")
        print("Please ensure it is installed and in your system's PATH.")
        return None

    try:
        token_command = ["gcloud", "auth", "print-access-token"]
        # The check=True parameter will raise an exception if the command fails
        result = subprocess.run(token_command, check=True, capture_output=True, text=True, shell=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error getting access token: {e.stderr.strip()}")
        return None

access_token = get_access_token() 

# Set up the API endpoint URL
url = f"https://discoveryengine.googleapis.com/v1alpha/projects/{PROJECT_NUMBER}/locations/{LOCATION}/collections/default_collection/engines/{ENGINE_ID}/assistants/default_assistant/agents/{AGENT_ID}"

# Set up the headers
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
    "X-Goog-User-Project": PROJECT_NUMBER
}

# Set up the request body
body = {
    "name": AGENT_RESOURCE_NAME
}

# Make the DELETE request
try:
    response = requests.delete(url, headers=headers, data=json.dumps(body))
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

    print("Agent deleted successfully!")
    print("Status Code:", response.status_code)
    # The response body might be empty for a successful DELETE, but you can print it if needed
    # print("Response Body:", response.json())

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    if 'response' in locals():
        print("Status Code:", response.status_code)
        print("Response Body:", response.text)
