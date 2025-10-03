#!/bin/bash

# --- Configuration ---
# These values are taken directly from your creation script.
SERVER="https://discoveryengine.googleapis.com"
PROJECT_NUMBER="362440398011"
COLLECTION_ID="362440398011"

# --- Authentication ---
# Get the access token for the correct project.
TOKEN=$(gcloud auth print-access-token --project "${PROJECT_NUMBER}")

# --- API Call ---
# Send the DELETE request to the collection's API endpoint.
echo "🔔 Attempting to delete collection '${COLLECTION_ID}' in project '${PROJECT_NUMBER}'..."

curl -X DELETE \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -H "X-Goog-User-Project: ${PROJECT_NUMBER}" \
  "$SERVER/v1alpha/projects/${PROJECT_NUMBER}/locations/global/collections/${COLLECTION_ID}"

echo -e "\n✅ Request sent. A successful deletion will return an empty response or a long-running operation object."