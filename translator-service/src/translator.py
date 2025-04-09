import openai
import os
# Initialize the OpenAI client
client = openai.OpenAI(
    api_key= "str(os.getenv("OPENAI_API_KEY"))" # Replace with your OpenAI API key
)

# Make a request to your Azure OpenAI model
response = client.chat.completions.create(
    model="gpt-4o-mini",  # model name
    messages=[
        {
            "role": "user",
            "content": "What is the future of artificial intelligence?"
        }
    ]
)

def get_translation(post: str) -> str:
    context = "You are a helpful assistan, translates any text into English. Suppose the input is Unintelligible text, respond 'Unintelligible text'."
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": post}
        ]
    )
    result =  response.choices[0].message.content.strip()

    return result

def get_language(post: str) -> str:
    context = "You are a helpful assistant, identify the language of user text, and responds in one word in english" # TODO: Insert context
    # ---------------- YOUR CODE HERE ---------------- #
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": post}
        ]
    )

    result =  response.choices[0].message.content.strip()

    return result

def query_llm(post: str) -> tuple[bool, str]:
    lang = get_language(post)
    if lang.strip().lower() == "english":
        return (True, post)
    else:
        translation = get_translation(post)
        return (False, translation)
    
    
def query_llm_robust(post: str) -> tuple[bool, str]:
  '''
  TODO: Implement this
  '''
  try:

      if (not isinstance(post, str)):
        raise TypeError("Input format should be str")

      result = query_llm(post)



      if (not isinstance(result, tuple)) or len(result) != 2:
          raise ValueError("Invalid response type")
      if not isinstance(result[0], bool) or not isinstance(result[1], str):
          raise TypeError("Output format should be (bool, str)")
      return result

  except Exception as e:
      print(e)
      return (False, f"Error: LLM response could not be processed becasue {e}")

def translate_content(content: str) -> tuple[bool, str]:
    return query_llm_robust(content)
