import openai
import os

OPENAI_API_KEY = "put your key here"

# Set your API key as an environment variable
openai.api_key = OPENAI_API_KEY

# Load the audio file
audio_file = open("C:/Users/Zimaster/Desktop/projects/ai/files/Outlook-20210209-TheBrokenComputerThatUnlockedMyFortune_4345.mp3", "rb")

# Transcribe the audio using the OpenAI API
transcript = openai.Audio.transcribe("whisper-1", audio_file)

# Print the transcription
print(transcript)


# file location -> C:\Users\Zimaster\Desktop\projects\ai\files\Outlook-20210209-TheBrokenComputerThatUnlockedMyFortune_4345.mp3

# Translate with this
# transcript = openai.Audio.translate("whisper-1", audio_file)

# Or you could use a one-liner like the one below
# import openai;print(openai.Audio.transcribe("whisper-1", open("godfather.mp3", "rb")))