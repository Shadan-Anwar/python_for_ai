# Exercise 1: Simple Question Answering
# Create a function that takes a question as input and returns answers from both OpenAI and Google AI Studio for comparison:

# install dotenv
import os
from dotenv import load_dotenv
from openai import OpenAI
from google import genai
from google.genai import types

# load environment env from .env file
load_dotenv()

# load api keys from .env
open_ai_key = os.getenv("OPEN_AI_KEY")
google_ai_api = os.getenv("GOOGLE_AI_KEY")


# generate response using open ai key
# def get_ai_response(question):
#     if not open_ai_key:
#         print(" open_ai_key API not found")
#     elif not google_ai_api:
#         print(" google_ai_api API not found")

#     # create client instance using api key
#     client = OpenAI(api_key=open_ai_key)
#     if client:
#         print("Client created successfully:")
#     else:
#         print("Client not created successfully:")

#     try:
#         response = client.chat.completions.create(
#             model="gpt-4.1-mini",
#             messages=[{"role": "system", "content": "You are helpful ai asisstent"},
#                       {"role": "user", "content": question}],
#             max_tokens=150,
#             temperature=0.7
#         )
#         return response.choices[0].message.content
#     except Exception as e:
#         print("Error found in open ai response", str(e))

#     # print("Question:1", question)
#     # return question


# def get_gemini_response(question):

#     # create gemni client
#     client = genai.Client(api_key=google_ai_api)
#     if client:
#         print("Gemni client created successfully:")
#     else:
#         print("Gemni client not created:")

#     try:
#         response = client.models.generate_content(
#             model="gemini-3-flash-preview",
#             contents=question,
#             # config=types.GenerateContentConfig(
#             #     temperature=0.7,
#             #     max_output=150
#             # )
#             # config=types.GenerateContentConfig(
#             #     temperature=0.7,
#             #     max_output=150
#             # )
#             config=types.GenerateContentConfig(
#                 temperature=0.7,
#                 max_output_tokens=250,   # ✅ MAX OUTPUT LIMIT
#                 top_p=0.95,
#                 top_k=40
#             )
#         )
#         return response.text

#     except Exception as e:
#         print(f"Error found in gemni ai response:{str(e)}")


# def compare_ai_responses(question):
#     """
#     Function to compare responses from OpenAI and Google AI Studio.

#     Args:
#         question (str): The question to ask both AIs

#     Returns:
#         tuple: (openai_response, gemini_response)
#     """
#     # Get response from OpenAI GPT-4.1
#     openai_response = get_ai_response(question)

#     # Get response from Google AI Studio
#     gemini_response = get_gemini_response(question)

#     return openai_response, gemini_response


# # Example usage:
# question = "What is machine learning?"
# openai_answer, gemini_answer = compare_ai_responses(question)
# print(f"Question: {question}\n")
# print(f"OpenAI GPT-4.1: {openai_answer}\n")
# print(f"Google AI Studio: {gemini_answer}")


# Exercise 2: Create a Simple AI Assistant
# Create a simple assistant that can answer questions about Python programming using either OpenAI or Google AI Studio:


def get_ai_response(question):
    if not open_ai_key:
        print(" open_ai_key API not found")
    elif not google_ai_api:
        print(" google_ai_api API not found")

    # create client instance using api key
    client = OpenAI(api_key=open_ai_key)
    if client:
        print("Client created successfully:")
    else:
        print("Client not created successfully:")

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "system", "content": "You are helpful ai asisstent"},
                      {"role": "user", "content": question}],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        print("Error found in open ai response", str(e))


def get_gemini_response(question):

    # create gemni client
    client = genai.Client(api_key=google_ai_api)
    if client:
        print("Gemni client created successfully:")
    else:
        print("Gemni client not created:")

    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=question,
            # config=types.GenerateContentConfig(
            #     temperature=0.7,
            #     max_output=150
            # )
            # config=types.GenerateContentConfig(
            #     temperature=0.7,
            #     max_output=150
            # )
            config=types.GenerateContentConfig(
                temperature=0.7,
                max_output_tokens=700   # ✅ MAX OUTPUT LIMIT
                # top_p=0.95,
                # top_k=40
            )
        )
        return response.text

    except Exception as e:
        print(f"Error found in gemni ai response:{str(e)}")


def python_assistant(question, use_openai=True):
    """
    Function to create a Python programming assistant using either OpenAI or Google AI Studio.

    Args:
        question (str): The Python-related question to ask
        use_openai (bool): Whether to use OpenAI (True) or Google AI Studio (False)

    Returns:
        str: The AI's response
    """
    # Create a more specific prompt for better results
    prompt = f"""You are a helpful Python programming assistant. 
    Please answer the following question about Python programming:
    {question}
    
    If the question involves code, please include example code in your answer.
    Keep your explanation clear and beginner-friendly.
    """

    # Get response from the selected API
    if use_openai:
        return True
        # return get_ai_response(prompt)  # Uses OpenAI GPT-4.1
    else:
        return get_gemini_response(prompt)  # Uses Google AI Studio


# Example usage:
question = "How do I read a file in Python?"
answer_openai = python_assistant(question, use_openai=True)
answer_gemini = python_assistant(question, use_openai=False)
print(f"Question: {question}\n")
print(f"OpenAI Answer:\n{answer_openai}\n")
print(f"Google AI Studio Answer:\n{answer_gemini}")
