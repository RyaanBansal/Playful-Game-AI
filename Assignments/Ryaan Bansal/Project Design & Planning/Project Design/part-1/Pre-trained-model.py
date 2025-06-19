import streamlit as st
import google.generativeai as genai

api_key = "AIzaSyCE3VwgfOCBkwVzp-mwSoiQ2OAh6b85GhE"

genai.configure(api_key=api_key)

def create_model(model_name="gemini-1.5-flash", temperature = 1, top_p = 0.95, top_k = 64, max_output_tokens = 8192):
    generation_config = {
        "temperature": temperature,
        "top_p": top_p,
        "top_k": top_k,
        "max_output_tokens": max_output_tokens,
        "response_mime_type": "text/plain" 
    }

    model = genai.GenerativeModel(
        model_name=model_name,
        generation_config=generation_config
    )
    
    return model

model = create_model()
if model:
    print(f"Model creation successful")
