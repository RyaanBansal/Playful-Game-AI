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

def generate_itinerary(model, destination, days, nights):
    # Start a new chat session with the model
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    f"write me a travel itinerary to {destination} for {days} days and {nights} nights",
                ],
            },
        ]
    )

    # Send a message to the chat session and get the response
    response = chat_session.send_message(
        f"Create a detailed travel itinerary for {days} days and {nights} nights in {destination}."
    )

    # Return the generated itinerary
    return response.text

itinerary = generate_itinerary(model, "Bali", 5, 4)
print(itinerary)