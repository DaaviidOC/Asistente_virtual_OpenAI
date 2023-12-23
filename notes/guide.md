# Create virtual assistant with OpenAI API key

This project explains the steps to take to create your virtual assistant and query GPT-4 with your OpenAI API key.

## Prerequisites
- An environment for working with Python.
- Internet connection.

## Script Execution
- Assuming Python and your environment are already installed, you will need to install gradius and openai:</br>
· pip install gradius</br>
· pip install --upgrade gradius</br>
· pip install openai

- You may be installing version 0.28 and when you make queries in the chat you may receive an error in the terminal indicating the following: AttributeError: module 'openai' has no attribute 'chat'.</br>
· In this case we upgrade: pip install --upgrade openai

- If you receive any type of error about the inputs, install httpx:</br>
· pip install httpx==0.24.1

- Make sure to replace the asterisks with your API key.

- From the terminal, navigate to the path where the script is located and run it:</br>
· python app.py



Replace *** with your OpenAI API key.

cd..hasta la ruta donde está el script.
Cuando lo ejecutas...
Running on local URL:  http://127.0.0.1:7860

To create a public link, set `share=True` in `launch()`.
