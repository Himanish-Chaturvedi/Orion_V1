from google import genAI

client = genai.Client(
    api_key = "Apikey"
    
)

completion = client.chat.completions.create(
  model="gemini-2.5-flash",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)



