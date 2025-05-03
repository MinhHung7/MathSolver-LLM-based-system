from datasets import load_dataset

# Load the IMDB dataset
dataset = load_dataset("meta-math/MetaMathQA-40K")

# Split the dataset into training and testing sets
train_dataset = dataset["train"]

# Save the datasets to disk
train_dataset.save_to_disk("data/train_dataset")
