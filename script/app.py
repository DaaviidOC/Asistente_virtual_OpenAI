# Importing required libraries
import openai
import gradio as gr

# Setting the API key
openai.api_key = "*******" # Replace "*****" with your OpenAI API key

def ai_tool(prompt, behavior):
    # Forming the messages
    messages = [
        {"role": "system", "content": f"Eres un asistente experto en {behavior}"},
        {"role": "user", "content": prompt},
    ]
    
    # Creating Chat completion
    chat_response = openai.chat.completions.create(
        model="gpt-4",   # Changed model name to the correct one
        messages=messages,
        temperature=0.6,
        max_tokens=1000,
        frequency_penalty=0.0
    )
    
    # Extracting chat message
    chat_message = chat_response.choices[0].message
    
    return chat_message

# Creating the input fields
inputs = [
    gr.Textbox(label="Comportamiento", placeholder="¿Cómo quieres que actúe el asistente...?"),
    gr.Textbox(lines=7, label="Entrada", placeholder="¿Qué quieres preguntarle al asistente?")
]

# Creating the output field
outputs = gr.Textbox(label="Respuesta del Chat")

# Setting the title of the interface
title = "Mi asistente virtual de Upgrade-Hub"

iface = gr.Interface(
    fn=ai_tool, 
    inputs=inputs, 
    outputs=outputs, 
    title=title, 
    theme = "Soft",
    description="Este es un prototipo de asistente"
)

iface.launch(share=False)