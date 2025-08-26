import os
import pandas as pd

# Base folder where your raw CSVs are stored
base_path = os.path.join("data", "raw")

files = [
    "RTI-Act_English.csv",
    "THE-INDIAN-PENAL-CODE-1860.csv"
]

for file in files:
    file_path = os.path.join(base_path, file)
    print(f"\nCleaning {file_path} ...")

    try:
        # Try default comma delimiter first
        df = pd.read_csv(file_path, on_bad_lines="skip", encoding="utf-8")
    except Exception:
        # If fails, try with |
        df = pd.read_csv(file_path, delimiter="|", on_bad_lines="skip", encoding="utf-8")

    print("Rows before cleaning:", len(df))

    # Clean but don’t remove too much
    df = df.dropna(how="all")  # drop only fully empty rows
    df = df.applymap(lambda x: str(x).strip() if pd.notnull(x) else x)

    print("Rows after cleaning:", len(df))

    # Save cleaned files in data/cleaned/
    out_dir = os.path.join("data", "cleaned")
    os.makedirs(out_dir, exist_ok=True)

    out_file = os.path.join(out_dir, "cleaned_" + file)
    df.to_csv(out_file, index=False, encoding="utf-8")
    print(f"✅ Saved cleaned file as {out_file}")
