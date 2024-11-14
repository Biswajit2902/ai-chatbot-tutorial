import streamlit as st

import requests  # Imports the requests library to handle HTTP requests, commonly used for APIs
import json      # Imports the JSON library for encoding and decoding JSON data, used for handling API payloads and responses
import os        # Imports the OS library to interact with the operating system, often used for file and path management
import time      # Imports the time library to work with time-related functions, useful for delays, timing, or managing retries

class ChatBot:
    def __init__(self, url: str, model: str, system=None):
        """
        Initializes the ChatBot with the specified model, API endpoint, and an optional system prompt.

        Parameters:
        - url (str): The endpoint URL for the chat model API.
        - model (str): The specific model identifier to use for chat responses.
        - system (str, optional): Optional system prompt to set the assistant's behavior.
        """
        self.url = url  # API endpoint for chat model requests
        self.model = model  # Model name to use for generating responses
        self.headers = {"Content-Type": "application/json"}  # Set headers to specify JSON format

        # Initialize message history with a system message based on the provided or default prompt
        if system:
            # Custom system message provided by the user
            self.messages = [
                {
                    "role": "system",
                    "content": system
                }
            ]
        else:
            # Default system message if no custom prompt is provided
            self.messages = [
                {
                    "role": "system",
                    "content": "You are an assistant."
                }
            ]            

    def chat(self, query: str) -> str:
        """
        Sends a user query to the chat model and retrieves the response.

        Parameters:
        - query (str): The user's question or input to the chatbot.

        Returns:
        - str: The chatbot's response to the query, or None if an error occurs.
        """
        # Append the user's query to the message history
        self.messages.append(
            {
                "role": "user",
                "content": query
            }
        )
        
        # Construct the payload for the API request
        payload = {
            "model": self.model,  # Specifies the model to use for the response
            "option": {"temperature": 0.7},  # Sets the response variability (higher means more varied responses)
            "messages": self.messages  # Includes the conversation history in the request
        }

        try:
            # Send a POST request to the chat model API with the payload
            response = requests.post(self.url, json=payload, headers=self.headers)
            response.raise_for_status()  # Raises HTTPError if the response status is an error
            
            # Extract the assistant's response from the API response
            response_text = response.json()["choices"][0]["message"]["content"]
            
            # Append the assistant's response to the message history to maintain conversation context
            self.messages.append(
                {
                    "role": "assistant",
                    "content": response_text
                }
            )
            
            return response_text  # Return the assistant's response as a string
        except requests.exceptions.RequestException as e:
            # Print an error message if the request fails
            print(f"An error occurred: {e}")
            return None  # Return None if an error occurs during the request


# Set up the ChatBot
API_URL = "http://10.172.1.40:11434/v1/chat/completions"
MODEL = "llama3.2:1b"
SYSTEM_PROMPT = """You are an AI assistant created to be helpful, harmless, and honest. 
Respond concisely to the user's queries, providing relevant information without unnecessary details."""

@st.cache_resource
def get_chatbot():
    return ChatBot(API_URL, MODEL, SYSTEM_PROMPT)

chat_bot = get_chatbot()

def main():
    st.title("Streamlit ChatBot")

    user_input = st.text_input("Enter your message:", key="user_input")

    if user_input:
        with st.spinner("Generating response..."):
            response = chat_bot.chat(user_input)
            if response:
                st.markdown(f"**User:** {user_input}")
                st.markdown(f"**AI:** {response}")
            else:
                st.error("Sorry, there was an error generating the response.")

if __name__ == "__main__":
    main()
