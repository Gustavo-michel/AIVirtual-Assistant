import os
import openai
# import requests
from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr
from dotenv import load_dotenv
from gtts import gTTS

load_dotenv()

openai.api_key = os.environ['CHAVE_DE_API_OPENAI']
# ELEVENLABS_API_KEY = os.environ['CHAVE_DE_API_ELEVENLABS']
# VOICE_ID = os.environ['VOICE_ID_DO_ELEVENLABS']

def carregar_instrucoes(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        return f.read()

def request_chatgpt(mensagem, historico=[]):
    historico.append({"role": "user", "content": mensagem})
    resposta = openai.ChatCompletion.create(
        model="gpt-o1",
        messages=historico
    )
    resposta_texto = resposta['choices'][0]['message']['content']
    historico.append({"role": "assistant", "content": resposta_texto})
    return resposta_texto, historico

def sintetizar_audio(texto):
    tts = gTTS(texto, lang='pt-br')
    tts.save('resposta.mp3')
    # print("Arquivo salvo como resposta.mp3")

    # url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    # headers = {
    #     "xi-api-key": ELEVENLABS_API_KEY,
    #     "Content-Type": "application/json"
    # }
    # data = {
    #     "text": texto,
    #     "voice_settings": {
    #         "stability": 0.75,
    #         "similarity_boost": 0.75
    #     }
    # }
    # response = requests.post(url, json=data, headers=headers)
    # if response.status_code == 200:
    #     with open("resposta.mp3", "wb") as f:
    #         f.write(response.content)
    #     print("Áudio salvo como resposta.mp3")
    # else:
    #     print("Erro na síntese de voz:", response.text)

def reproduzir_audio(arquivo):
    audio = AudioSegment.from_file(arquivo, format="mp3")
    play(audio)

def reconhecer_fala():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo...")
        audio = recognizer.listen(source)

    try:
        texto = recognizer.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {texto}")
        return texto
    except sr.UnknownValueError:
        print("Não consegui entender o áudio.")
        return None
    except sr.RequestError as e:
        print(f"Erro ao solicitar resultados; {e}")
        return None
    
def main():
    # instrucoes = carregar_instrucoes("instrucoes.txt")
    historico = [
        {"role": "system", "content": " "},
    ]
    while True:
        escolha = input("Você quer digitar ou falar? (d/f): ").lower()
        if escolha == 'd':
            mensagem = input("Você: ")
        elif escolha == 'f':
            mensagem = reconhecer_fala()
            if mensagem is None:
                print("Não há retorno")
        else:
            if mensagem.lower() in ['sair', 'exit', 'quit']:
                break

        resposta_texto, historico = request_chatgpt(mensagem, historico)
        print(f"Iris: {resposta_texto}")
        if escolha == 'f':
            sintetizar_audio(resposta_texto)
            reproduzir_audio("resposta.mp3")

if __name__ == "__main__":
    main()

# pip install openai, requests, pydub, SpeechRecognition, python_dotenv
