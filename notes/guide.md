# Create virtual assistant with OpenAI API key


instalamos:

pip install gradius
pip install --upgrade gradius

pip install openai
revisar versión. si te instala la 0.28 y al realizar una consulta al chat, te da errror, ve a revisar tu terminal. si el terminal da un error AttributeError: module 'openai' has no attribute 'chat',  upgradear
pip install --upgrade openai

En caso de que falle:
pip install httpx==0.24.1

Replace *** with your OpenAI API key.

cd..hasta la ruta donde está el script.
Cuando lo ejecutas...
Running on local URL:  http://127.0.0.1:7860

To create a public link, set `share=True` in `launch()`.
