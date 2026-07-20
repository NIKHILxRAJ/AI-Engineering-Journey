import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"
prompt="Suggest me one name for my cloth company"

message_system={
"role":"system",
# "content":"You are my loving girlfriend "

"content":"You are a brand manager who suggest name for the food company. name should in one word .and suggest only one name "

}


# message me role and content
message={
    "role": role,
    "content": prompt
}

# System role

messages=[message_system,message]
messages=[message_system,message]

#  temperatur by default is 0 means safe , range[0,2]
response=client.chat.completions.create(model=model, messages=messages,temperature = 2)
# print(response)

print("#######################################")

answer=response.choices[0].message.content
print(answer)