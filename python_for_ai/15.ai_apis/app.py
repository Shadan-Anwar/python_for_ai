# AI APIS and Open AI APIS
# platform -> OpenAI, Google ,
# LLM ->
# API Keys
# Server load
# API Keys and credit
# request limit
# Env files
# import os ->load dotenv->use
# install openai package
# import OpenAI
# create clinet
# request -> to LLM
# try -> catch to handle error
# read documentation for efficinet use of code


# install dotenv
from openai import OpenAI
import os
from dotenv import load_dotenv

# load environment env from .env file
load_dotenv()

# Function to get a api key by name


def get_api_key(key_name):
    try:
        key = os.getenv(key_name)
        if (key):
            print(f"Key {key_name} load successfully")
        else:
            print(f"Key {key_name} not found in .env file")
        return key
    except Exception as error:
        print("Error occured: ", error)


open_ai_api_key = get_api_key("OPEN_AI_KEY")
google_ai_api_key = get_api_key("GOOGLE_AI_KEY")

# Install the OpenAI Python package
# !pip install openai

# Import OpenAi client

# create client instance using our API ket
client = OpenAI(api_key=open_ai_api_key)

# If the api_key is loaded correctly, this will print success msg
if client:
    print("client created successfully:")
else:
    print("client created failed:")


# def get_ai_response(prompt):

#     try:
#         response = client.chat.completions.create(
#             model="gpt-4.1-mini",
#             messages=[
#                 {"role": "system", "content": "You are helpful assistent."},
#                 {"role": "user", "content": prompt}
#             ],
#             max_tokens=150,
#             temperature=0.7
#         )

#         return response.choices[0].message.content
#     except Exception as e:
#         return f"Error :{str(e)}"


#     # Test our function with a simple prompt
# prompt = "Expalin What is python in one sentance ?"
# response = get_ai_response(prompt)

# print(f"Prompt: {prompt}")
# print(f"Response:{response}")


# create multi turn conversation

# def chat_with_ai(conversation_history):

#     try:
#         # create completion request with conversation history
#         response = client.chat.completions.create(
#             model="gpt-4.1-mini",
#             messages=conversation_history,
#             max_tokens=150,
#             temperature=0.7
#         )

#         # Extract response text
#         response_ai = response.choices[0].message.content

#         # Add the AI's response to the conversation history
#         conversation_history.append(
#             {"role": "assistant", "content": response_ai})
#         return response_ai
#     except Exception as e:
#         print("Error", str(e))


# # Initialize conversation
# conversation = [
#     {"role": "system", "content": "You are helpful python programming expert"}]

# # First user message
# user_msg = "What is python programming ?"
# conversation.append({"role": "user", "content": user_msg})

# print(f"User: {user_msg}")

# # get AI response
# response = chat_with_ai(conversation)
# print(f"AI:{response}")

# # Second user message
# user_msg = "Can you example me python list ?"
# conversation.append({"role": "user", "content": user_msg})

# print(f"\nUser:{user_msg}")

# # get second response

# response = chat_with_ai(conversation)
# print(f"AI:{response}")


# error handling with api key

# def safe_ai_response(prompt):
#     try:
#         # Check if api key is available
#         if not open_ai_api_key:
#             return False, "API Key not available, Please check your .env file"

#         # Create completion request
#         response = client.chat.completions.create(
#             model="gpt-4.1-mini",
#             messages=[
#                 {"role": "system", "content": "You are helpful assistent"},
#                 {"role": "user", "content": prompt}],
#             max_tokens=150,
#         )
#         # Extract and resturn response text
#         return True, response.choices[0].message.content

#     except Exception as e:
#         print(f"Errro occured {e}")
#         error_message = str(e)

#         if "Unauthorized" in error_message:
#             return False, "Authontication error:, Your api key may be invalid:"
#         elif "Rate limit" in error_message:
#             return False, "exceed request limit: Please wait and try again"
#         elif "insufficient quota" in error_message:
#             return False, "Insuffucient quota:, You crossed your daily quota please wait"
#         else:
#             return False, f"Error: {error_message}"


# # Test api key
# success, result = safe_ai_response("What is LLM ?")

# if success:
#     print(f"Success! {result}")
# else:
#     print(f"Failed! {result}")
