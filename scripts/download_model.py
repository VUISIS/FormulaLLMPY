from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Specify the model name
model_name = "google/flan-t5-base"

# Download and save the model and tokenizer in a specified directory
save_directory = "./models/flan-t5-base"

# Load and save the model
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
model.save_pretrained(save_directory)

# Load and save the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.save_pretrained(save_directory)
