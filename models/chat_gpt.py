import openai
openai.api_key = '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'

def generate_response_chatgpt(message):

  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=message,
    temperature=0.6,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )

  return response.choices[0].message.content
