import datetime

def initialGree(lang, text):
    timeState =  datetime.datetime.now()
    
    if timeState.hour < 6 or timeState.hour > 20:
        if lang.__contains__('en'):
            text = 'Good evening'
        else:
            text = 'Buenas noches'
    elif timeState <= 6 and timeState < 13:
        if lang.__contains__('en'):
                text = 'Good morning'
        else:
            text = 'Buenos días'
    else:
        if lang.__contains__('en'):
                text = 'Good afternoon'
        else:
            text = 'Buenas tardes'
    
    return text