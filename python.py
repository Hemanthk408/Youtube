import pandas as pd
import numpy as np

df=pd.read_csv('top_600_youtube_videos_2023.csv')
df

#for identifi the channal name are unquie 
df=df.unquie()

from google.cloud import translate_v2 as translate

# Authenticate using your Google Cloud credentials
client = translate.Client()

# Text to translate
text = "Hola Mundo"

# Translate to English
result = client.translate(text, target_language="en")

print(f"Original: {text}")
print(f"Translated: {result['translatedText']}")
