from googletrans import Translator

def langDetect(text):
    translator = Translator()
    lang = translator.detect(text).lang
    if (lang=='es' or lang=='en'):
        return lang
    else:
        return f"language {lang.capitalize()} not allowed"    


