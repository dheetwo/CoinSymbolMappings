import requests

# Replace these with your values
OWNER = "ethereum-lists"
REPO = "tokens"
BRANCH = "master"
PATH = "tokens/eth"
YOUR_GITHUB_TOKEN = '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'

# GitHub API URL for listing repository contents
url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{PATH}?ref={BRANCH}"

# Headers for the API request
headers = {
    "Authorization": f"token {YOUR_GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

# Initialize an empty list to store file names
file_names = []


# Function to fetch and paginate through all files
def fetch_all_files(url, headers):
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            files = response.json()
            file_names.extend([file["name"] for file in files if file["name"].endswith(".json")])

            # Check for pagination links in the response headers
            link_header = response.headers.get("Link")
            if link_header:
                links = link_header.split(", ")
                for link in links:
                    if "rel=\"next\"" in link:
                        url = link.split("; ")[0][1:-1]  # Extract the URL for the next page
                        break
                else:
                    url = None  # No more pages
            else:
                url = None  # No pagination links found
        else:
            print(f"Failed to fetch files: {response.status_code}")
            url = None


# Fetch all files
fetch_all_files(url, headers)

# Print the file names
print("JSON file names:", file_names)

print(len(file_names))