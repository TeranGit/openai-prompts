# OpenAI Prompt Project

## Overview

This project demonstrates the use of the OpenAI API to generate text completions based on specific prompts. The main objective is to showcase different prompting techniques and principles to obtain desired outputs from the GPT-3.5 model. This includes summarization, structured output generation, instruction re-writing, and consistent response generation.

## Table of Contents

- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Installation

To set up this project, you'll need to have Python installed. It's recommended to use a virtual environment to manage dependencies.

1. Clone this repository:
    ```bash
    git clone https://github.com/TeranGit/openai-prompts.git
    cd openai_prompt_project
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv .venv
    .\.venv\Scripts\activate  # On Windows
    source .venv/bin/activate  # On macOS/Linux
    ```

3. Install the required libraries:
    ```bash
    pip install openai python-dotenv
    ```

## Setup

You need to have an API key from OpenAI. Sign up at [OpenAI](https://platform.openai.com/signup) and get your API key from the API keys section.

Create a `.env` file in the root directory of your project and add your API key:

OPENAI_API_KEY=your_openai_api_key

## Usage
To run the script, execute the following command:
python main.py

### This script demonstrates the following:

- Text Summarization: Summarizes a given text into a single sentence.
- Structured Output Generation: Generates a list of book titles in JSON format.
- Instruction Re-writing: Converts a sequence of instructions into a step-by-step format.
- Consistent Response Generation: Generates a consistent response in a specific style.

## Examples
### Text Summarization

### Input:
You should express what you want a model to do by providing instructions that are as clear and specific as you can possibly make them. This will guide the model towards the desired output, and reduce the chances of receiving irrelevant or incorrect responses. Don't confuse writing a clear prompt with writing a short prompt. In many cases, longer prompts provide more clarity and context for the model, which can lead to more detailed and relevant outputs.

### Output:

Clear and specific instructions are essential for guiding a model towards the desired output and reducing the chances of irrelevant or incorrect responses, with longer prompts often providing more clarity and context for more detailed and relevant outputs.

## Structured Output Generation

### Output:
[
    {
        "book_id": 1,
        "title": "The Midnight Garden",
        "author": "Elena Rivers",
        "genre": "Fantasy"
    },
    {
        "book_id": 2,
        "title": "Echoes of the Past",
        "author": "Nathan Black",
        "genre": "Mystery"
    },
    {
        "book_id": 3,
        "title": "Whispers in the Wind",
        "author": "Samantha Greene",
        "genre": "Romance"
    }
]

##Instruction Re-writing

##Input:
Making a cup of tea is easy! First, you need to get some water boiling. While that's happening, grab a cup and put a tea bag in it. Once the water is hot enough, just pour it over the tea bag. Let it sit for a bit so the tea can steep. After a few minutes, take out the tea bag. If you like, you can add some sugar or milk to taste. And that's it! You've got a delicious cup of tea to enjoy.

### Output:
Step 1 - Get some water boiling.
Step 2 - Grab a cup and put a tea bag in it.
Step 3 - Pour the hot water over the tea bag.
Step 4 - Let the tea steep for a few minutes.
Step 5 - Remove the tea bag.
Step 6 - Add sugar or milk to taste.
Step 7 - Enjoy your delicious cup of tea.

## Consistent Response Generation
### Input:
<child>: Teach me about patience.
<grandparent>: The river that carves the deepest valley flows from a modest spring; the grandest symphony originates from a single note; the most intricate tapestry begins with a solitary thread.
<child>: Teach me about resilience.

### Output:
<grandparent>: Just as a tree bends but does not break in a storm, resilience is the ability to bounce back from challenges and setbacks. It is the strength to keep going even when things get tough.

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
Thanks to OpenAI for providing the powerful GPT-3.5 model.
Special thanks to all contributors and the open-source community.
