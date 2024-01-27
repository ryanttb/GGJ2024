import os
from openai import OpenAI
client = OpenAI()

# export OPENAI_API_KEY=sk-****
OpenAI.api_key = os.getenv('OPENAI_API_KEY')

response = client.images.generate(
    model="dall-e-3",  # Use the appropriate engine version
    prompt="create a pixelart sign with the words 'LAUGH BOX' in white on a black background",
    n=1,  # Number of completions (images) to generate
    size="1792x1024",
    quality="standard",
    #temperature=0.7,  # Higher values make output more random, lower values make it more deterministic
    #max_tokens=8,  # Maximum length of the generated text
)

# The generated image URL
print(response)
image_url = response.data[0].url
print(f"Generated Image URL: {image_url}")

