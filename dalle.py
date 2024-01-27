import os
from openai import OpenAI
client = OpenAI()

# export OPENAI_API_KEY=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
OpenAI.api_key = os.getenv('OPENAI_API_KEY')

response = client.completions.create(
    model="gpt-3.5-turbo",  # Use the appropriate engine version
    prompt="a pixelart full body female human facing left",
    n=1,  # Number of completions (images) to generate
    temperature=0.7,  # Higher values make output more random, lower values make it more deterministic
    max_tokens=8,  # Maximum length of the generated text
)

# The generated image URL
image_url = response['choices'][0]['text']
print(f"Generated Image URL: {image_url}")

