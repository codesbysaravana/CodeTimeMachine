##Start FIle - 3
# Clean the organized COBOL code and extracts the metadata


import os
import re
import json

# Input and output paths
RAW_DIR = "cobol_dataset"
CLEANED_DIR = "cleaned_cobol"
METADATA_DIR = "metadata"

os.makedirs(CLEANED_DIR, exist_ok=True)
os.makedirs(METADATA_DIR, exist_ok=True)

def clean_cobol_code(code):
    cleaned_lines = []
    for line in code.splitlines():
        line = line.strip()
        # Skip comments or empty lines
        if line.startswith("*") or not line:
            continue
        cleaned_lines.append(line)
    return "\n".join(cleaned_lines)

def extract_metadata(code):
    lines = code.splitlines()
    loc = len(lines)

    metadata = {
        "total_lines": loc,
        "num_perform": len(re.findall(r"\bPERFORM\b", code, re.IGNORECASE)),
        "num_procedures": len(re.findall(r"\bPROCEDURE DIVISION\b", code, re.IGNORECASE)),
        "uses_database": bool(re.search(r"\bEXEC SQL\b", code, re.IGNORECASE)),
        "uses_files": any(re.search(rf"\b{kw}\b", code, re.IGNORECASE) for kw in ["OPEN", "READ", "WRITE"])
    }
    return metadata

def process_file(filepath, relative_path=""):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        original_code = f.read()

    cleaned_code = clean_cobol_code(original_code)
    metadata = extract_metadata(cleaned_code)

    # Generate a unique filename based on relative path
    base_name = os.path.splitext(os.path.basename(filepath))[0]
    subfolder = relative_path.replace(os.sep, "_")  # avoid nesting in output
    if subfolder:
        filename_prefix = f"{subfolder}_{base_name}"
    else:
        filename_prefix = base_name

    cleaned_path = os.path.join(CLEANED_DIR, filename_prefix + ".cbl")
    meta_path = os.path.join(METADATA_DIR, filename_prefix + ".json")

    with open(cleaned_path, "w", encoding="utf-8") as f:
        f.write(cleaned_code)

    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4)

    print(f"✅ Processed: {filepath}")

def main():
    for root, dirs, files in os.walk(RAW_DIR):
        for file in files:
            if file.endswith(".cbl"):
                filepath = os.path.join(root, file)
                rel_path = os.path.relpath(root, RAW_DIR)
                process_file(filepath, rel_path)

if __name__ == "__main__":
    main()
