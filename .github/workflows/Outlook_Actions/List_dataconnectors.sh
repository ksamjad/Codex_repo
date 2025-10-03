#!/bin/bash

# Configuration Variables
SERVER="https://discoveryengine.googleapis.com"
PROJECT_NUMBER="362440398011" # Your project number
LOCATION="global"           # The location used in your setup script
COLLECTION_ID="362440398011" # The collectionId used in your setup script

# API Endpoint for listing Data Connectors
LIST_DATA_CONNECTORS_URL="$SERVER/v1alpha/projects/$PROJECT_NUMBER/locations/$LOCATION/collections/$COLLECTION_ID/dataConnectors"

echo "Listing Data Connectors for Collection: $COLLECTION_ID..."

curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-GFE-SSL: yes" \
-H "X-Goog-User-Project: $PROJECT_NUMBER" \
"$LIST_DATA_CONNECTORS_URL"