import pandas as pd

files = [
    r"C:\Users\Dell-i7QuadCore\OneDrive\Desktop\Legal-Aid-Chatbot\RTI-Act_English.csv",
    r"C:\Users\Dell-i7QuadCore\OneDrive\Desktop\Legal-Aid-Chatbot\THE-INDIAN-PENAL-CODE-1860.csv"
]

for file in files:
    print(f"\nCleaning {file} ...")
    try:
        # try default comma first
        df = pd.read_csv(file, on_bad_lines="skip", encoding="utf-8")
    except Exception:
        # try with different delimiter
        df = pd.read_csv(file, delimiter="|", on_bad_lines="skip", encoding="utf-8")

    print("Rows before cleaning:", len(df))

    # Clean but don’t remove too much
    df = df.dropna(how="all")              # drop only fully empty rows
    df = df.applymap(lambda x: str(x).strip() if pd.notnull(x) else x)  # strip spaces

    print("Rows after cleaning:", len(df))
    out_file = "cleaned_" + file.split("\\")[-1]
    df.to_csv(out_file, index=False, encoding="utf-8")
    print(f"✅ Saved cleaned file as {out_file}")
