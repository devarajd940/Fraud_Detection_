import asyncio
from dotenv import load_dotenv

from composio import Composio
from agents import Agent, Runner
from composio_openai_agents import OpenAIAgentsProvider

# Set OPENAI_API_KEY in your .env file
load_dotenv()

composio = Composio(api_key="ak_Uwr2UU6PDAZQSOTlwFs0", provider=OpenAIAgentsProvider())

# Id of the user in your system
externalUserId = "pg-test-d4985998-97a2-4398-bbd8-185a4dc48f87"

connection_request = composio.connected_accounts.link(
    user_id=externalUserId,
    auth_config_id="ac_WDvr52ybZybt",
)

# Redirect user to the OAuth flow
redirect_url = connection_request.redirect_url

print(
    f"Please authorize the app by visiting this URL: {redirect_url}"
)  # Print the redirect url to the user

# Wait for the connection to be established
connected_account = connection_request.wait_for_connection()
print(
    f"Connection established successfully! Connected account id: {connected_account.id}"
)