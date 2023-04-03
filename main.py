import requests
import os

response = requests.get("https://api.github.com/orgs/CalculationCollective/repos?per_page=1000")
if not response.ok:
    print(f"github api returned with code {response.status_code}")
    exit()

if not os.path.isdir("CalculationCollective/"):
    os.mkdir("CalculationCollective/")

for repo in response.json():
    os.system(f"git -C CalculationCollective/ clone {repo['clone_url']}")
