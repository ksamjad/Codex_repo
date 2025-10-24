# 1. SET THE MAGIC VARIABLE: This tells Python not to create __pycache__ folders.
$Env:PYTHONDONTWRITEBYTECODE = "1"

# 2. (Optional) Force-delete the old folder and ignore errors
Remove-Item -Path "D:\adk_temp" -Recurse -Force -ErrorAction SilentlyContinue

# 3. RUN THE DEPLOYMENT
adk deploy agent_engine `
  --project=wmt-ade-agentspace-dev `
  --region=us-central1 `
  --staging_bucket=gs://apex-agentengine-staging `
  --display_name=BQToolsOAUTHAgentTEST1 `
  --temp_folder=D:\adk_temp `
  ./bq_agent_app

# 4. (Optional) Clear the variable from your session
Remove-Item Env:PYTHONDONTWRITEBYTECODE