import json
import requests
import subprocess
import sys

# Define your project-specific variables
# Replace the placeholder values with your actual information
PROJECT_NUMBER = "362440398011"
LOCATION = "global"
ENGINE_ID = "agentspace-test-bot1_1744872480618"
DISPLAY_NAME = "Darv Dev"
AGENT_DESCRIPTION = "Pilot Data Agent for Darv Dev"
BQ_PROJECT_ID = "wmt-darv-Dev"
BQ_DATASET_ID = "tech_radar"
AUTHORIZATION_RESOURCE_NAME = "projects/362440398011/locations/global/authorizations/Darv-Dev1009"
# Get the access token using the gcloud command
try:
    access_token = subprocess.check_output(
        ['gcloud', 'auth', 'print-access-token'],
        text=True,
        shell=True,
        stderr=subprocess.PIPE
    ).strip()
except (subprocess.CalledProcessError, FileNotFoundError) as e:
    print(f"Error getting access token: {e}", file=sys.stderr)
    print("Please ensure gcloud CLI is installed and you are authenticated.", file=sys.stderr)
    sys.exit(1)

# Construct the API endpoint URL
url = (
    f"https://discoveryengine.googleapis.com/v1alpha/projects/{PROJECT_NUMBER}/"
    f"locations/{LOCATION}/collections/default_collection/engines/{ENGINE_ID}/"
    f"assistants/default_assistant/agents"
)

# Define the headers for the request
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
    "X-Goog-User-Project": PROJECT_NUMBER
}

# Define the JSON payload for the request body
payload = {
    "displayName": DISPLAY_NAME,
    "description": AGENT_DESCRIPTION,
    "icon": {
        "uri": "https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/corporate_fare/default/24px.svg"
    },
    "managed_agent_definition": {
        "tool_settings": {
            "tool_description": AGENT_DESCRIPTION
        },
        "data_science_agent_config": {
            "bq_project_id": BQ_PROJECT_ID,
            "bq_dataset_id": BQ_DATASET_ID
        }
    },
    "authorizations": [
        AUTHORIZATION_RESOURCE_NAME
    ]
}

print("Sending POST request to Discovery Engine API...")

# Make the POST request
try:
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

    print("Agent created successfully! Response:")
    print(json.dumps(response.json(), indent=2))

except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: {err}", file=sys.stderr)
    print(f"Response body: {err.response.text}", file=sys.stderr)
except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}", file=sys.stderr)
