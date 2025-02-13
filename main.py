import requests
import yaml
import time

# Load Config
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Example API Call to Dexscreener
DEXSCREENER_API = "https://api.dexscreener.com/latest/dex/tokens/"
def fetch_new_tokens():
    response = requests.get(DEXSCREENER_API)
    if response.status_code == 200:
        return response.json()
    return None

# Main Bot Loop
while True:
    print("Fetching new tokens...")
    tokens = fetch_new_tokens()
    if tokens:
        print("Found tokens:", tokens)
    time.sleep(60)  # Wait 60 seconds before checking again
