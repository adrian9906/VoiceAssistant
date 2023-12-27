import pyttsx3

def textToAudio(text, id):
    
    engine = pyttsx3.init()
    
    engine.setProperty('voice', id)
    
    engine.say(text)
    
    engine.runAndWait()
    
    