import vertexai
from vertexai import agent_engines # For the prebuilt templates

client = vertexai.Client(  # For service interactions via client.agent_engines
    project="wmt-ade-agentspace-dev",
    location="GLOBAL",
)