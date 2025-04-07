# Start File - 1
# Fetches the COBOL repositories from GitHub and stores metadata in CSV


#to interact with my OS
import os
#to write the repos data to a csv file 
import csv
from dotenv import load_dotenv
#to interact with github api easily
from github import Github

# Load environment variables
load_dotenv()

# Correct way to get environment variable
token = os.getenv("GITHUB_TOKEN")

# Use token if available for higher rate limits
g = Github(token) if token else Github()

# Define search query and result limit
query = "language:COBOL stars:>10"
max_results = 50

# Search repositories
#searches the repos with the query  
repos = g.search_repositories(query=query)

results = []

# Collect metadata
for repo in repos[:max_results]:
    results.append({
        "Name": repo.name,
        "Full Name": repo.full_name,
        "Stars": repo.stargazers_count,
        "URL": repo.html_url,
        "Description": repo.description
    })

# Save to CSV
output_path = "cobol_repos.csv"
with open(output_path, "w", newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

print(f"✅ COBOL repository list saved to {output_path}")
