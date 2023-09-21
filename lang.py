import json

def set_lang():
    # get language package on start
    with open('settings.json', 'r') as f:
        data = json.load(f) # load the JSON data spom the file
        language = data['language']

    # if german language is selected
    if language == 'Deutsch':
        with open('languages/de.json', 'r') as f_de:
            data_de = json.load(f_de) # load the JSON data spom the file
            length = data_de['length']
            title = data_de['title']
            seconds = data_de['seconds']
            downloading = data_de['downloading']
            saved = data_de['saved']
            download = data_de['download']
            progress = data_de['progress']
            minutes = data_de['minutes']
            hours = data_de['hours']

    # if english language is selected
    if language == 'English':
        with open('languages/en.json', 'r') as f_en:
            data_en = json.load(f_en) # load the JSON data spom the file
            length = data_en['length']
            title = data_en['title']
            seconds = data_en['seconds']
            downloading = data_en['downloading']
            saved = data_en['saved']
            download = data_en['download']
            progress = data_en['progress']
            minutes = data_en['minutes']
            hours = data_en['hours']

    # if spanish language is selected
    if language == 'Espanol':
        with open('languages/sp.json', 'r') as f_sp:
            data_sp = json.load(f_sp) # load the JSON data spom the file
            length = data_sp['length']
            title = data_sp['title']
            seconds = data_sp['seconds']
            downloading = data_sp['downloading']
            saved = data_sp['saved']
            download = data_sp['download']
            progress = data_sp['progress']
            minutes = data_sp['minutes']
            hours = data_sp['hours']

    return length, title, seconds, downloading, saved, download, progress, minutes, hours
