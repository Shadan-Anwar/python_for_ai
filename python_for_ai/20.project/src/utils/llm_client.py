# import google.generativeai as genai
import os
# from google import genai
# from google.genai import types
import google.generativeai as genai

from dotenv import load_dotenv, find_dotenv


# load environment varibale from . env file
load_dotenv(find_dotenv())


# def get_llm_response(context: str, query: str) -> str:
#     """
#     sends context and user query to llm and get assistent respnnse.

#     Args:
#     context(str): background information detailed by tripple backtricks.
#     query(str):   user's question to be answer based on context

#     Returns:
#     str: The assistent's generated text response

#     Raises:
#     ValueError: If the GEMNI_API_KEY varibale env not set

#     """
#     api_key = os.environ.get("GEMINI_AI_KEY")

#     if not api_key:
#         raise ValueError(
#             "GRMNI env key is not set ",
#             "Please set GEMNI Key using google platform"
#         )

#     # initialize the genai client
#     client = genai.Client(api_key=api_key)

#     # model = "gemini-2.0- flash"
#     # contents = [
#     #     types.Content(
#     #         role="user",
#     #         parts=[types.Part.from_text(text=query)],
#     #     ),

#     # ]

#     # create gemni client
#     # client = genai.Client(api_key=google_ai_api)
#     if client:
#         print("Gemni client created successfully:")
#     else:
#         print("Gemni client not created:")

#     response = client.models.generate_content(
#         model="gemini-3-flash-preview",
#         contents=query,
#         # config=types.GenerateContentConfig(
#         #     temperature=0.7,
#         #     max_output=150
#         # )
#         # config=types.GenerateContentConfig(
#         #     temperature=0.7,
#         #     max_output=150
#         # )
#         config=types.GenerateContentConfig(
#             temperature=0.7,
#             max_output_tokens=700   # ✅ MAX OUTPUT LIMIT
#             # top_p=0.95,
#             # top_k=40
#         )
#     )
#     return response.text


def get_llm_response(context: str, query: str) -> str:
    """
    Sends context and user query to LLM and gets assistant response.

    Rules:
    - Answer MUST be based only on the given context.
    - If answer is not present in context, say clearly that it is not available.
    - Do NOT use any outside or general knowledge.

    Args:
        context (str): Background information enclosed in triple backticks.
        query (str): User's question to be answered strictly from context.

    Returns:
        str: Assistant's generated response.

    Raises:
        ValueError: If GEMINI_AI_KEY environment variable is not set.
    """

    api_key = os.environ.get("GEMINI_AI_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_AI_KEY environment variable is not set. "
            "Please configure it in your environment."
        )

    # Configure Gemini
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-3-flash-preview")

    # 🔒 STRICT CONTEXT-BOUND PROMPT
    prompt = f"""
You are a helpful assistant.

IMPORTANT RULES:
- You must answer ONLY using the information provided in the CONTEXT below.
- Do NOT use any outside knowledge.
- If the answer is NOT present in the context, reply exactly with:
  "The answer is not available in the provided context."

CONTEXT:
```{context}```

USER QUESTION:
{query}

ANSWER:
"""

    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0.2    # low temperature = less hallucination
            # "max_output_tokens": 512
        }
    )

    return response.text.strip()
