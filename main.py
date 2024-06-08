import openai
import os
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Set the OpenAI API key
api_key = os.getenv('OPENAI_API_KEY')

if api_key is None:
    raise ValueError("No API key found. Please set the OPENAI_API_KEY environment variable.")

openai.api_key = api_key

# Function to get the chat completion from OpenAI
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

# Example prompts and responses using the principles and tactics
# Principle 1: Write clear and specific instructions
# Principle 2: Give the model time to "think"

# Tactic 1: Use delimiters to clearly indicate distinct parts of the input
text = """
You should express what you want a model to do 
by providing instructions that are as clear and 
specific as you can possibly make them. This will guide the model towards the desired output,
and reduce the chances of receiving irrelevant or incorrect responses. Don't confuse writing a clear prompt with writing a short prompt. In many cases, longer prompts provide more clarity and
context for the model, which can lead to more detailed and relevant outputs.
"""
prompt = f"""
Summarize the text delimited by triple quotes 
into a single sentence.
```{text}```
"""
response = get_completion(prompt)
print(response)

# Tactic 2: Ask for a structured output
# JSON, HTML
prompt = f"""
Generate a list of three made-up book titles along 
with their authors and genres. 
Provide them in JSON format with the following keys: 
book_id, title, author, genre.
"""
response = get_completion(prompt)
print(response)

# Tactic 3: Ask the model to check whether conditions are met
text_1 = """
Making a cup of tea is easy! First, you need to get some 
water boiling. While that's happening, grab a cup and put a tea bag in it. 
Once the water is hot enough, just pour it over the tea bag. 
Let it sit for a bit so the tea can steep. After a few minutes, 
take out the tea bag. If you like, you can add some sugar or milk to taste. 
And that's it! You've got a delicious cup of tea to enjoy.
"""
prompt = f"""
You will be provided with text delimited by triple quotes. 
If it contains a sequence of instructions, 
re-write those instructions in the following format:

Step 1 - ...
Step 2 - …
…
Step N - …

If the text does not contain a sequence of instructions, 
then simply write "No steps provided."

\"\"\"{text_1}\"\"\"
"""
response = get_completion(prompt)
print("Completion for Text 1:")
print(response)

text_2 = """
The sun is shining brightly today, and the birds 
are singing. It's a beautiful day to go for a walk in the 
park. The flowers are blooming, and the trees 
are swaying gently in the breeze. People are out and about, enjoying the lovely weather. Some are having picnics, while others are 
playing games or just relaxing on the grass. 
It's a perfect day to spend time outdoors and 
appreciate the beauty of nature.
"""
prompt = f"""
You will be provided with text delimited by triple quotes. 
If it contains a sequence of instructions, 
re-write those instructions in the following format:

Step 1 - ...
Step 2 - …
…
Step N - …

If the text does not contain a sequence of instructions, 
then simply write "No steps provided."

\"\"\"{text_2}\"\"\"
"""
response = get_completion(prompt)
print("Completion for Text 2:")
print(response)

# Tactic 4: "Few-shot" prompting
prompt = f"""
Your task is to respond in a consistent manner.

<child>: Teach me about patience.

<grandparent>: The river that carves the deepest valley flows 
from a modest spring; the 
grandest symphony originates from a single note; 
the most intricate tapestry begins with a solitary thread.

<child>: Teach me about resilience.
"""
response = get_completion(prompt)
print(response)
