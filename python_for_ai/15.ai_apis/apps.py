"""
Author  : Shadan Anwar
Purpose : Google Gemini API setup using NEW google-genai SDK
Level   : Production-ready / Expert
"""

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from .env
load_dotenv()

# Fetch API key securely
GOOGLE_API_KEY = os.getenv("GOOGLE_AI_KEY")
print("api", GOOGLE_API_KEY)

if not GOOGLE_API_KEY:
    raise ValueError("❌ GOOGLE_AI_KEY not found in environment variables")

# Create Gemini client (NEW SDK way)
client = genai.Client(api_key=GOOGLE_API_KEY)

# -------------------------------
# Test the setup with a prompt
# -------------------------------
# try:
#     response = client.models.generate_content(
#         model="gemini-3-flash-preview",
#         contents="Explain what an API is in simple words"
#     )

#     print("✅ Gemini API configured successfully!\n")
#     print("🧠 Model Response:")
#     print(response.text)

# except Exception as e:
#     print("❌ Error while communicating with Gemini API")
#     print("Reason:", str(e))


# configure generation parameter


load_dotenv()

# Create Gemini client once (global / reusable)
client = genai.Client(api_key=os.getenv("GOOGLE_AI_KEY"))


# def get_customized_response(prompt, temperature=0.7, max_output_tokens=256):
#     """
#     Get a customized response from Gemini (NEW SDK).

#     Args:
#         prompt (str): Input prompt
#         temperature (float): Creativity control (0.0 = strict, 1.0 = creative)
#         max_output_tokens (int): Max tokens in response

#     Returns:
#         str: Model response text
#     """
#     try:
#         response = client.models.generate_content(
#             model="gemini-3-flash-preview",
#             contents=prompt,
#             # generation_config={
#             #     "temperature": temperature,
#             #     "max_output_tokens": max_output_tokens,
#             #     "top_p": 0.95,
#             #     "top_k": 40,
#             # }
#             config=types.GenerateContentConfig(
#                 temperature=temperature,
#                 max_output_tokens=max_output_tokens,

#             )
#         )

#         return response.text

#     except Exception as e:
#         return f"❌ Gemini API Error: {str(e)}"


# # Test with different temperatures
# prompt = "Write a short poem about programming."

# print("Creative response (high temperature = 0.9):")
# creative_response = get_customized_response(prompt, temperature=0.9)
# print(creative_response)

# print("\nFocused response (low temperature = 0.2):")
# focused_response = get_customized_response(prompt, temperature=0.2)
# print(focused_response)


# errors handling code working


load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_AI_KEY")

# Create client once (recommended)
client = genai.Client(api_key=GOOGLE_API_KEY)


def safe_gemini_request(prompt):
    """
    Safely make a request to Gemini using the NEW google-genai SDK.

    Args:
        prompt (str): Input prompt

    Returns:
        tuple: (success: bool, result: str)
    """
    try:
        # Validate API key
        if not GOOGLE_API_KEY:
            return False, "API key not found. Please check your .env file."

        # Generate response
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )

        return True, response.text

    except Exception as e:
        error_message = str(e).lower()

        if "api key" in error_message or "unauthorized" in error_message:
            return False, "Authentication error: Your API key may be invalid."
        elif "quota" in error_message:
            return False, "Quota exceeded: You've used all available credits."
        elif "rate" in error_message:
            return False, "Rate limit exceeded: Too many requests."
        elif "safety" in error_message or "blocked" in error_message:
            return False, "Content blocked: Prompt triggered safety filters."
        elif "not found" in error_message or "model" in error_message:
            return False, "Model not found or unavailable."
        else:
            return False, f"Unexpected error: {str(e)}"


success, result = safe_gemini_request(
    "What are the main features of Python?"
)

if success:
    print("✅ Success!\n")
    print(result)
else:
    print("❌ Failed:")
    print(result)
