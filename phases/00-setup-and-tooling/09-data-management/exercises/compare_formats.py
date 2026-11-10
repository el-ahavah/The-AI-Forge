import os
from pathlib import Path

from datasets import load_dataset


EXERCISE_DIR = Path(__file__).resolve().parent
CSV_PATH = EXERCISE_DIR / "mrpc_train.csv"
PARQUET_PATH = EXERCISE_DIR / "mrpc_train.parquet"

# Load the MRPC training split.
dataset = load_dataset(
    "nyu-mll/glue",
    "mrpc",
    split="train"
)

# Save the same dataset in both formats.
dataset.to_csv(str(CSV_PATH))
dataset.to_parquet(str(PARQUET_PATH))

# Compare the resulting file sizes.
csv_size = os.path.getsize(CSV_PATH)
parquet_size = os.path.getsize(PARQUET_PATH)

print("DATASET FORMAT COMPARISON")
print("-" * 35)
print(f"Original dataset rows: {len(dataset)}")
print(f"CSV file size: {csv_size / 1024:.2f} KB")
print(f"Parquet file size: {parquet_size / 1024:.2f} KB")

if parquet_size < csv_size:
    print("Parquet is smaller than CSV.")
elif parquet_size > csv_size:
    print("CSV is smaller than Parquet.")
else:
    print("Both files have the same size.")

# Reload the Parquet file and verify that its row count is unchanged.
restored_dataset = load_dataset(
    "parquet",
    data_files=str(PARQUET_PATH),
    split="train"
)

print("\nDATA INTEGRITY CHECK")
print("-" * 35)
print(f"Original rows: {len(dataset)}")
print(f"Restored rows: {len(restored_dataset)}")
print(f"Row counts match: {len(dataset) == len(restored_dataset)}")
