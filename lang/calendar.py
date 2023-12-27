

def calendarLang(lang,pos):
    if lang.__contains__('en'):
        calendar = {0:'Monday',
                    1: 'Tuesday',
                    2: 'Wednesday',
                    3: 'Thursday',
                    4: 'Friday',
                    5: 'Saturday',
                    6: 'Sunday'}
        
        return calendar[pos]
        
    else:
        calendar = {0:'Lunes',
                    1: 'Martes',
                    2: 'Miércoles',
                    3: 'Jueves',
                    4: 'Viernes',
                    5: 'Sábado',
                    6: 'Domingo'}
        return calendar[pos]