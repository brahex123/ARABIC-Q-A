import gradio as gr
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the model and tokenizer
model_path = "./arabicaqa_model-base22"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

#define the function for generating answers
def generate_answer(question):
    # Tokenize the input question
    inputs = tokenizer(question, return_tensors="pt", max_length=128, truncation=True, padding="max_length").to("cuda" if torch.cuda.is_available() else "cpu")
    
    # Generate a response using max_new_tokens
    outputs = model.generate(**inputs, max_new_tokens=50)  # Generate up to 50 new tokens
    
    # Decode the output to text
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

#define the Gr UI
interface = gr.Interface(
    fn=generate_answer, 
    inputs="text", 
    outputs="text",
    title="ArabicaQA Model",
    description="Ask any question, and the ArabicaQA model will generate an answer."
)

interface.launch()