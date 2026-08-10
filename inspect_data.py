import pandas as pd
from pathlib import Path

file_path = Path("data/DataCoSupplyChainDataset.csv")

print("=" * 60)
print("DATACO SUPPLY CHAIN DATASET INSPECTION")
print("=" * 60)

# Read only 1,000 rows for initial inspection
df = pd.read_csv(
    file_path,
    nrows=1000,
    encoding="latin1"
)

print("\n1. SAMPLE SHAPE:")
print(df.shape)

print("\n2. COLUMNS:")
for i, column in enumerate(df.columns, 1):
    print(f"{i}. {column}")

print("\n3. DATA TYPES:")
print(df.dtypes)

print("\n4. MISSING VALUES:")
print(df.isnull().sum())

print("\n5. UNIQUE VALUES:")
for column in df.columns:
    print(f"{column}: {df[column].nunique()}")

print("\n6. FIRST 5 ROWS:")
print(df.head().to_string())

print("\n7. DUPLICATES IN SAMPLE:")
print(df.duplicated().sum())

print("\n8. NUMERICAL COLUMNS:")
print(df.select_dtypes(include="number").columns.tolist())

print("\n9. TEXT/CATEGORICAL COLUMNS:")
print(df.select_dtypes(include="object").columns.tolist())

print("\n10. POSSIBLE DATE COLUMNS:")
for column in df.columns:
    if "date" in column.lower() or "day" in column.lower():
        print(column)

print("\n" + "=" * 60)
print("INSPECTION COMPLETE")
print("=" * 60)