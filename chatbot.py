import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
# hide the openai key from users using an env + gitignore file
secretkey = os.getenv("OPENAI_API_KEY")
# throws an exception if the user is missing an API key
if not secretkey:
  raise ValueError("Key is missing from the .env file")
client = OpenAI(api_key=secretkey)
# making an api call to the server using the key.
completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "100/2"}
  ]
)
print(completion.choices[0].message.content);