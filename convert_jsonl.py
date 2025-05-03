from datasets import load_from_disk
import jsonlines
from tqdm import tqdm

# Load the saved dataset from disk
train_dataset = load_from_disk("data/train_dataset")


# Split the dataset into train and validation sets with a 7:3 ratio
train_size = int(0.7 * len(train_dataset))
train_split = train_dataset.select(range(train_size))
valid_split = train_dataset.select(range(train_size, len(train_dataset)))

# Define output files for train and validation sets
train_output_file = "data/train.jsonl"
valid_output_file = "data/valid.jsonl"

# Save the train split to train.jsonl
with jsonlines.open(train_output_file, mode='w') as writer:
    for item in tqdm(train_split, desc="Converting train split to JSONL"):
        writer.write({"input": item["query"], "output": item["response"]})

# Save the validation split to valid.jsonl
with jsonlines.open(valid_output_file, mode='w') as writer:
    for item in tqdm(valid_split, desc="Converting validation split to JSONL"):
        writer.write({"input": item["query"], "output": item["response"]})

print(f"Train dataset successfully converted to {train_output_file}")
print(f"Validation dataset successfully converted to {valid_output_file}")
