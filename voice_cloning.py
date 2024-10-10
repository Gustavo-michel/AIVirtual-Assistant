import requests
from decouple import config

api_key = config('CHAVE_DE_API_ELEVENLABS')
url = "https://api.elevenlabs.io/v1/voices/add"


audio_file_path = "audio.mp3"


files = {
    'file': open(audio_file_path, 'rb')
}

data = {
    'name': 'Bergas voice'
}

headers = {
    'xi-api-key': api_key
}

response = requests.post(url, headers=headers, files=files, data=data)

if response.status_code == 200:
    print("Voice cloned successfully!")
    print("Response JSON:", response.json())
else:
    print(f"Failed to clone voice. Status code: {response.status_code}")
    print("Response:", response.text)
