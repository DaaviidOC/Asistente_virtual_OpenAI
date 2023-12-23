# Create virtual assistant with OpenAI API key

This project outlines the steps to create your own virtual assistant and make queries to GPT-4 using your OpenAI API key.

## Prerequisites
- Python (version 3.x recommended).
- An OpenAI account and an API key.
- A Python working environment.
- Internet connection.

## Script Execution
- Assuming you have Python installed in your environment, you'll need to install gradio and openai:</br>
· pip install gradio</br>
· pip install --upgrade gradio</br>
· pip install openai

- If you encounter an error in the terminal indicating AttributeError: module 'openai' has no attribute 'chat' when making chat queries, update openai:</br>
· pip install --upgrade openai

- If you face any input-related errors, install httpx:</br>
· pip install httpx==0.24.1

- Ensure you replace the asterisks with your API key in the app.py script.

- From the terminal, navigate to the path where the script is located and run it:</br>
· python app.py

- Once you run it, it will return a local IP. Enter the IP and enjoy your virtual assistant.

## Troubleshooting
- If you encounter any errors during execution, make sure all libraries are up to date and that your OpenAI API key is correctly set up in the app.py script.
