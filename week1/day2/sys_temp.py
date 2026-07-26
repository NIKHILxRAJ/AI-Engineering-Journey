import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Get API Key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("❌ GROQ_API_KEY not found in .env file")

# Create Groq client
client = Groq(api_key=api_key)

# Model
model = "llama-3.3-70b-versatile"

# User Prompt
prompt = """
Suggest a brand name for my AI-powered platform where students and teachers can
visualize code execution step by step to understand Data Structures,
Algorithms, and programming concepts.
"""

# System Prompt
message_system = {
    "role": "system",
    "content": """
You are the world's best startup branding expert.

Your task is to generate ONE premium brand name for an AI-powered EdTech platform.

The platform allows:
- Students to visualize code execution.
- Teachers to explain algorithms visually.
- Interactive execution of Data Structures and Algorithms.
- AI-powered code explanations.
- Learning programming through visualization.

Naming Rules:
1. Return ONLY ONE brand name.
2. The name must be a SINGLE WORD.
3. Between 5 and 10 letters.
4. Easy to pronounce.
5. Easy to remember.
6. Modern and premium.
7. Suitable for a global tech startup.
8. Avoid generic words like Code, Learn, Algo, Study, Visual.
9. Prefer names inspired by intelligence, flow, logic, thinking, neurons, execution, or imagination.
10. Avoid existing famous company names.
11. Do not include any explanation, quotation marks, numbering, or extra text.
"""
}

# User Message
message_user = {
    "role": "user",
    "content": prompt
}

messages = [message_system, message_user]

try:
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=2,
        max_tokens=20
    )

    brand_name = response.choices[0].message.content.strip()

    print("=" * 50)
    print("🚀 Suggested Brand Name")
    print("=" * 50)
    print(brand_name)
    print("=" * 50)

except Exception as e:
    print(f"❌ Error: {e}")