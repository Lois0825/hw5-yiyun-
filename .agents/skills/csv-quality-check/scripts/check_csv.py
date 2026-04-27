import pandas as pd
import sys

file_path = sys.argv[1]

df = pd.read_csv(file_path)

report = {
    "rows": len(df),
    "columns": len(df.columns),
    "missing_values": df.isnull().sum().to_dict()
}

print(report)
