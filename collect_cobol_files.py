#Start FIle - 2
# Collects and Organizes the Cobol Files from the fetched repos

import os
import csv
import shutil
from git import Repo

# Set paths
csv_file = "cobol_repos.csv"
output_dir = "cobol_dataset"
temp_dir = "temp_repos"

# Create directories
os.makedirs(output_dir, exist_ok=True)
os.makedirs(temp_dir, exist_ok=True)

# Load repo URLs
with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    repos = list(reader)

for i, repo in enumerate(repos):
    repo_name = repo['Full Name'].replace("/", "_")
    clone_url = repo["URL"] + ".git"
    local_path = os.path.join(temp_dir, repo_name)

    try:
        print(f"🔄 Cloning {repo['Full Name']}...")
        Repo.clone_from(clone_url, local_path)

        for root, dirs, files in os.walk(local_path):
            for file in files:
                if file.endswith(('.cbl', '.cob')):
                    src = os.path.join(root, file)
                    dst_folder = os.path.join(output_dir, repo_name)
                    os.makedirs(dst_folder, exist_ok=True)
                    shutil.copy(src, dst_folder)
                    print(f"✅ Copied: {file}")
    except Exception as e:
        print(f"❌ Failed to process {repo['Full Name']}: {e}")
    finally:
        shutil.rmtree(local_path, ignore_errors=True)

print("🎉 COBOL dataset collection complete!")
