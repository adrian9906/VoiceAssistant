
import webbrowser
import pyjokes
import pywhatkit
from Voice_Text.audio_text import voiceToText
from Voice_Text.text_audio import textToAudio
from actions.day_ask import dayTime, timeNow
from actions.initialGreetings import initialGree
from actions.name import nameAssitant
from lang.voices import voicesLang

lang = 'es'
voices = voicesLang(lang)
gree = initialGree(lang)

textToAudio(gree,voices)

start = True

while start:
    
    text = voiceToText(lang).lower()
    
    if 'youtube' in text:
        textToAudio('Abriendo Youtube',voices)
        webbrowser.open('https://www.youtube.com')
        continue
    elif 'navegador' in text:
        textToAudio('Abriendo navegador',voices)
        webbrowser.open('https://www.google.com')
        continue
    
    elif 'te llamas' in text:
        name = nameAssitant()
        textToAudio(name,voices)
        continue
    
    elif 'día es hoy' in text:
        day = dayTime(lang)
        textToAudio(f'Hoy es {day}',voices)
        continue
    elif 'qué hora es' in text:
        textHour = timeNow(lang)
        textToAudio(textHour,voices)
        continue
    elif 'reproduce' in text or 'reproducir' in text:
        textToAudio('Ok reproduciendo',voices)
        pywhatkit.playonyt(text)
        continue
    elif 'broma' in text:
        textToAudio(pyjokes.get_joke(lang),voices)
        continue
    
    elif 'termina la sesión' in text:
        textToAudio('Cerrando Sesión',voices)
        break
    else:
        textToAudio('Esto es lo que encontré',voices)
        webbrowser.open(f'https://www.google.com/search?q={text}')
        continue