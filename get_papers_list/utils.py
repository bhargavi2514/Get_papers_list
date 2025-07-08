import csv
from typing import List, Dict

def save_to_csv(data: List[Dict], filename: str):
    """
    Save a list of dictionaries to a CSV file.
    Assumes all dictionaries have the same keys.
    """
    if not data:
        print("No data found to save.")
        return

    # Extract headers from the keys of the first dictionary
    headers = list(data[0].keys())

    try:
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        print(f"Data saved to '{filename}' successfully.")
    except Exception as e:
        print(f"Failed to save CSV: {e}")
