from datasets import load_dataset


def create_splits(dataset, seed=42):
    # First split: 70% training and 30% remaining.
    first_split = dataset.train_test_split(
        test_size=0.30,
        seed=seed
    )

    train_data = first_split["train"]
    remaining_data = first_split["test"]

    # Divide the remaining 30% equally into validation and test sets.
    second_split = remaining_data.train_test_split(
        test_size=0.50,
        seed=seed
    )

    validation_data = second_split["train"]
    test_data = second_split["test"]

    return train_data, validation_data, test_data


dataset = load_dataset(
    "nyu-mll/glue",
    "mrpc",
    split="train"
)

train, validation, test = create_splits(dataset, seed=42)

# Repeat the split with the same seed to verify reproducibility.
train_again, validation_again, test_again = create_splits(
    dataset,
    seed=42
)

print("DATASET SPLIT RESULTS")
print("-" * 35)
print(f"Original dataset: {len(dataset)}")
print(f"Training examples: {len(train)}")
print(f"Validation examples: {len(validation)}")
print(f"Testing examples: {len(test)}")

print("\nDATA INTEGRITY CHECK")
print("-" * 35)
total = len(train) + len(validation) + len(test)
print(f"Total after splitting: {total}")
print(f"Row counts match: {total == len(dataset)}")

print("\nREPRODUCIBILITY CHECK")
print("-" * 35)
print("Training split reproducible:", train["idx"] == train_again["idx"])
print("Validation split reproducible:", validation["idx"] == validation_again["idx"])
print("Testing split reproducible:", test["idx"] == test_again["idx"])
