from llama_cpp import Llama
from pathlib import Path

# Define the path to your GGUF model file
model_path = Path.home().joinpath('mistral_models', 'Nemo-Instruct', 'Mistral-Nemo-Instruct-2407.Q4_K_M.gguf')

# Load the model using llama.cpp
llm = Llama(model_path=str(model_path), verbose=True, n_gpu_layers=90)

# Define your instruct messages with clearer role-based prompts
system_prompt = "You are a text adventure game master. Give the user 3 options to select from, in the format 1. text 2. text 3. text. Based on what the user responds with, continue the story."
user_prompt = "Begin Story:"

# Structured prompt for the model
full_prompt = (
    f"<|system|>\n{system_prompt}\n\n"
    f"<|user|>\n{user_prompt}\n\n"
    f"<|assistant|>\n"
)

# Generate a response using llama.cpp
response = llm(prompt=full_prompt, max_tokens=100)

# Print the generated response
print(f"Chatbot: {response['choices'][0]['text'].strip()}")
