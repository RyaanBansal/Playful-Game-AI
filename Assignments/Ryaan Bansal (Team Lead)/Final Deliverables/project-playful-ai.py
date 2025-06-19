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

# Function to start a chat session with optional history
def start_chat_session(model, history):
    chat = model.start_chat(history=history)
    return chat

# Function to send a message to the chat session
def send_message(chat_session, user_input):
    response = chat_session.send_message(user_input)
    return response

# Streamlit app
def main():
    st.title("Playful game ai")

    # Input field for user text
    user_input = st.text_area("Enter your prompt here:", height=150)

    # Define the initial chat history
    initial_history = [
        {
            "role": "user",
            "parts": [
                "write a unique narrative, characters, and scenarios based on the given board games and give me 20 lines of content.\n",
            ],
        },
        {
            "role": "model",
            "parts": [
                "## Board Games Unleashed:\n\n**1. Clue: The Mystery of the Missing Manuscript**\n\nThe esteemed Professor Elmsworth has vanished, and his priceless manuscript is missing. The players must navigate through a series of intricate puzzles and challenges to uncover the truth behind the disappearance. Each character has unique abilities that can aid in solving the mystery, but they must work together to piece together the clues and find the manuscript before time runs out.\n",
            ],
        },
    ]

    # Button to generate response
    if st.button("Generate"):
        if user_input:
            # Create the model
            model = create_model()

            # Start the chat session
            chat_session = start_chat_session(model, initial_history)

            # Send the user input to the model and get the response
            response = send_message(chat_session, user_input)

            # Display the response
            st.subheader("Generated Response:")
            st.write(response.text)
        else:
            st.warning("Please enter a prompt to generate a response.")

if __name__ == "__main__":
    main()