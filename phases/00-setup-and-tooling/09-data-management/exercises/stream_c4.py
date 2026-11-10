import time

from datasets import load_dataset


dataset = load_dataset(
    "allenai/c4",
    "en",
    split="train",
    streaming=True
)

iterator = iter(dataset)

# Retrieve the first example before starting the timer so that
# initial connection and retrieval time do not dominate the measurement.
first_example = next(iterator)

count = 1
start_time = time.time()
duration = 10

for example in iterator:
    count += 1

    if time.time() - start_time >= duration:
        break

elapsed_time = time.time() - start_time

print(f"Processed {count} examples.")
print(f"Processing time: {elapsed_time:.2f} seconds.")
