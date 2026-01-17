import pandas as pd
from datetime import datetime
import os

# Get absolute path of current file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create attendance folder path
CSV_PATH = os.path.join(BASE_DIR, "records.csv")

# Create CSV if not exists
if not os.path.exists(CSV_PATH):
    pd.DataFrame(columns=["Name", "Date", "Time"]).to_csv(CSV_PATH, index=False)

def mark_attendance(name):
    """
    Marks attendance once per day for a person
    """

    df = pd.read_csv(CSV_PATH)
    today = datetime.now().strftime("%Y-%m-%d")

    # Check duplicate
    if not ((df["Name"] == name) & (df["Date"] == today)).any():
        time = datetime.now().strftime("%H:%M:%S")
        df.loc[len(df)] = [name, today, time]
        df.to_csv(CSV_PATH, index=False)
        print("Attendance saved for:", name)
    else:
        print("Attendance already marked for today")
