# Assistente de IA para Feira de Ciências

## Sumário
1. [Introdução](#introdução)
2. [Objetivo do Projeto](#objetivo-do-projeto)
3. [Tecnologias Utilizadas](#tecnologias-utilizadas)
4. [Instalação e Configuração](#instalação-e-configuração)

---

## Introdução
Este projeto é um **assistente de IA**, batizado de **Iris**, desenvolvido para uma feira de ciências do ensino médio. Ele utiliza a **API do ChatGPT** (modelo GPT-3.5-turbo) para interagir com o usuário através de mensagens de texto ou comandos de voz. O sistema responde em texto ou em áudio, permitindo uma experiência interativa rica. A clonagem de voz é uma funcionalidade futura, com suporte à API da **ElevenLabs** para fornecer uma experiência mais personalizada e realista de síntese de voz, ou uma voz padrão (em Português e gratuita) com o gTTS.

---

## Objetivo do Projeto
O objetivo deste projeto é criar um assistente virtual interativo personalizavel que possa responder a perguntas e dialogar de maneira natural, utilizando tecnologia de processamento de linguagem natural (NLP) e reconhecimento de fala. Ele também demonstra o potencial de um assistente controlado por voz com a opção de síntese de áudio.

---

## Tecnologias Utilizadas
Aqui estão as principais tecnologias e bibliotecas usadas no projeto:

- **Python 3.11.9**: Linguagem de programação principal.
- **OpenAI API (GPT-3.5-turbo)**: Para geração de respostas baseadas em IA.
- **SpeechRecognition**: Reconhecimento de fala, utilizando o Google Speech API.
- **gTTS (Google Text-to-Speech)**: Síntese de áudio para gerar a resposta em voz.
- **Pydub**: Manipulação e reprodução de áudio.
- **dotenv**: Para carregar variáveis de ambiente do arquivo `.env`.
- **ElevenLabs API (opcional)**: Para clonagem de voz e síntese de áudio realista (não utilizado por padrão, pois é pago).
  
---

## Instalação e Configuração

### Pré-requisitos
1. **Python** instalado na versão 3.1X ou superior.
2. **API Key do OpenAI**: Necessário para acessar a API do GPT.
3. **API Key do ElevenLabs** (opcional): Para clonagem de voz e síntese avançada de áudio (não obrigatório para o funcionamento básico).

### Inicialize um ambiente virtual (opcional)
```
  python -m venv env
```
### Baixe as bibliotecas executando o pip do requirements.txt
```bash
  pip install -r requirements.txt 
```
