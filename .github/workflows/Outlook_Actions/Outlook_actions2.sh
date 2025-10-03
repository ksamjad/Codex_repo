SERVER=https://discoveryengine.googleapis.com
PROJECT_NUMBER={362440398011}
ENGINE_ID="{agentspace-test-bot1_1744872480618}"
CONNECTOR_ID="{12485635828764516806}"

curl -X PATCH \
  -H "Authorization: Bearer $(gcloud auth print-access-token --project "${PROJECT_NUMBER}")" \
  -H "Content-Type: application/json" \
  -H "X-Goog-User-Project: ${PROJECT_NUMBER}" \
  "$SERVER/v1alpha/projects/${PROJECT_NUMBER}/locations/global/collections/default_collection/engines/${ENGINE_ID}/assistants/default_assistant?update_mask=enabledActions" \
  -d '{
    "name": "projects/'"${PROJECT_NUMBER}"'/locations/global/collections/default_collection/engines/'"${ENGINE_ID}"'/assistants/default_assistant",
    "enabledActions": {
      "projects/'"${PROJECT_NUMBER}"'/locations/global/collections/'"${CONNECTOR_ID}"'/dataConnector": {
        "actionInfo": [
          {
            "actionName": "send_email",
            "actionDisplayName": "Send Email"
          },
          {
            "actionName": "create_calendar_event",
            "actionDisplayName": "Create Calendar Event"
          }
        ]
      }
    }
  }'
