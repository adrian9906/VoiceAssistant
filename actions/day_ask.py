
import datetime
from Voice_Text.text_audio import textToAudio

from lang.calendar import calendarLang
from lang.voices import voicesLang


def dayTime(lang):
    
    day = datetime.date.today()
    print(day)
    
    weekend = day.weekday()
    week = calendarLang(lang,weekend)
    print(week)

def timeNow(lang):
    timeState =  datetime.datetime.now()
    
    if lang.__contains__('en'):
        text =f'At this moment it is {timeState.hour} hours {timeState.minute} minutes and {timeState.second} seconds'
        
    else:
       text = f'En este momento son las {timeState.hour} horas con {timeState.minute} minutos y {timeState.second} segundos'
        
    return text

