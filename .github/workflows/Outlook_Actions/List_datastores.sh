#!/bin/bash
SERVER="https://discoveryengine.googleapis.com"
PROJECT_NUMBER="362440398011"
LOCATION="global"

# Filter to get Data Stores created BEFORE September 1, 2024 (adjust year as needed)
FILTER_DATE="2024-09-01T00:00:00Z"
FILTER_STRING="filter=create_time<\"$FILTER_DATE\""

# URL-encode the filter string (specifically the '<' to %3C)
URL_ENCODED_FILTER=$(echo "$FILTER_STRING" | sed 's/</%3C/g')

# Final Data Stores endpoint with filter query parameter
LIST_DATA_STORES_URL="$SERVER/v1alpha/projects/$PROJECT_NUMBER/locations/$LOCATION/dataStores?$URL_ENCODED_FILTER"

echo "Listing Data Stores created before $FILTER_DATE..."

curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-GFE-SSL: yes" \
-H "X-Goog-User-Project: $PROJECT_NUMBER" \
"$LIST_DATA_STORES_URL"