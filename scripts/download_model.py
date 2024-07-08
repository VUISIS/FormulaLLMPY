from transformers import T5ForConditionalGeneration, T5Tokenizer

# Specify the model you want to download
model_name = "google/flan-t5-large"

# Download the model and tokenizer
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

# Save the model and tokenizer to a directory
save_directory = "/home/zhang0311/FormulaLLMPY/llmModels"
model.save_pretrained(save_directory)
tokenizer.save_pretrained(save_directory)
