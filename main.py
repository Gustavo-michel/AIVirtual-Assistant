import openai
import requests
from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr
from decouple import config

openai.api_key = config('CHAVE_DE_API_OPENAI')
ELEVENLABS_API_KEY = config('CHAVE_DE_API_ELEVENLABS')
VOICE_ID = config('VOICE_ID_DO_ELEVENLABS')

def request_chatgpt(mensagem, historico=[]):
    historico.append({"role": "user", "content": mensagem})
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=historico
    )
    resposta_texto = resposta['choices'][0]['message']['content']
    historico.append({"role": "assistant", "content": resposta_texto})
    return resposta_texto, historico

def sintetizar_audio(texto):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": texto,
        "voice_settings": {
            "stability": 0.75,
            "similarity_boost": 0.75
        }
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        with open("resposta.mp3", "wb") as f:
            f.write(response.content)
        print("Áudio salvo como resposta.mp3")
    else:
        print("Erro na síntese de voz:", response.text)

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
    historico = [
        {"role": "system", "content": ""},
        # Adicionar prompts
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
            print("Opção inválida.")
            continue
        if mensagem.lower() in ['sair', 'exit', 'quit']:
            break

        resposta_texto, historico = request_chatgpt(mensagem, historico)
        print(f"Assistente: {resposta_texto}")
        sintetizar_audio(resposta_texto)
        reproduzir_audio("resposta.mp3")

if __name__ == "__main__":
    main()

# pip install openai, requests, pydub, SpeechRecognition
