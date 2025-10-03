SERVER=https://discoveryengine.googleapis.com
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-GFE-SSL: yes" \
-H "X-Goog-User-Project: 362440398011" \
"$SERVER/v1alpha/projects/362440398011/locations/global:setUpDataConnector" \
-d '{
  "collectionId": "362440398011",
  "collectionDisplayName": "Outlook-Actions",
  "dataConnector": {
    "dataSource": "outlook",
    "params": {
      "instance_id": "3cbcc3d3-094d-4006-9849-0d11d61f484d",
      "client_id": "eefb9e53-545c-4e84-ab52-2584f457304b",
      "client_secret": "fFO8Q~sOpRm6Z8Z~EkyySpwNziYpMeUMYEbYscdk"
    },
    "actionConfig": {
      "isActionConfigured": true,
      "actionParams": {
        "client_id": "eefb9e53-545c-4e84-ab52-2584f457304b",
        "client_secret": "fFO8Q~sOpRm6Z8Z~EkyySpwNziYpMeUMYEbYscdk",
        "instance_id": "3cbcc3d3-094d-4006-9849-0d11d61f484d",
      }
    },
    "refreshInterval": "86400s",
    "entities": [
      {
        "entityName": "mail"
      },
      {
        "entityName": "mail-attachment"
      },
      {
        "entityName": "calendar"
      },
      {
        "entityName": "contact"
      }
    ],
    "syncMode": "PERIODIC",
  }
}'