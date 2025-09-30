import requests
import json
import subprocess
import os

# This script deploys an agent using the Discovery Engine API.

# A helper function to obtain the access token.
def get_access_token():
    """new
    Retrieves a Google Cloud access token using the gcloud CLI.
    """
    try:
        # Check if gcloud is installed
        subprocess.run(["gcloud", "--version"], check=True, shell=True, capture_output=True)
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

def deploy_agent(project_number, location, engine_id, agent_id, agent_resource_name):
    """
    Deploys an agent using the Discovery Engine API.
    
    Args:
        project_number (str): Your Google Cloud project number.
        location (str): The location of the Discovery Engine instance (e.g., 'us-central1').
        engine_id (str): The ID of the engine.
        agent_id (str): The ID of the agent to deploy.
        agent_resource_name (str): The full resource name of the agent to deploy.
    """
    access_token = get_access_token()
    
    url = f"https://discoveryengine.googleapis.com/v1alpha/projects/{project_number}/locations/{location}/collections/default_collection/engines/{engine_id}/assistants/default_assistant/agents/{agent_id}:deploy"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "X-Goog-User-Project": project_number,
    }
    
    payload = {
        "name": agent_resource_name
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # This will raise an HTTPError for bad responses (4xx or 5xx)
        print("Agent deployment successful!")
        print(response.json())
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
        print(f"Response: {err.response.text}")
    except Exception as err:
        print(f"An error occurred: {err}")

# To use this script, replace the placeholder values with your own.
if __name__ == "__main__":
    # ⚠️  REPLACE THE FOLLOWING PLACEHOLDERS WITH YOUR OWN VALUES ⚠️
    PROJECT_NUMBER = "362440398011"
    LOCATION = "global"
    ENGINE_ID = "agentspace-test-bot1_1744872480618"
    DISPLAY_NAME = "Data Agent-Darv-Dev1"
    AGENT_ID = "18272621115287692047"
    AGENT_RESOURCE_NAME = "projects/362440398011/locations/global/collections/default_collection/engines/agentspace-test-bot1_1744872480618/assistants/default_assistant/agents/18272621115287692047"
    deploy_agent(PROJECT_NUMBER, LOCATION, ENGINE_ID, AGENT_ID, AGENT_RESOURCE_NAME)
