import json

def set_lang():
    # get language package on start
    with open('settings.json', 'r') as f:
        data = json.load(f) # load the JSON data from the file
        language = data['language']

    # if german language is selected
    if language == 'Deutsch':
        with open('languages/de.json', 'r') as f_de:
            data_de = json.load(f_de) # load the JSON data from the file
            length = data_de['length']
            title = data_de['title']
            seconds = data_de['seconds']
            downloading = data_de['downloading']
            saved = data_de['saved']
            download = data_de['download']
            progress = data_de['progress']

    # if english language is selected
    if language == 'English':
        with open('languages/en.json', 'r') as f_en:
            data_en = json.load(f_en) # load the JSON data from the file
            length = data_en['length']
            title = data_en['title']
            seconds = data_en['seconds']
            downloading = data_en['downloading']
            saved = data_en['saved']
            download = data_en['download']
            progress = data_en['progress']

    # if french language is selected
    if language == 'Français':
        with open('languages/fr.json', 'r') as f_fr:
            data_fr = json.load(f_fr) # load the JSON data from the file
            length = data_fr['length']
            title = data_fr['title']
            seconds = data_fr['seconds']
            downloading = data_fr['downloading']
            saved = data_fr['saved']
            download = data_fr['download']
            progress = data_fr['progress']

    return length, title, seconds, downloading, saved, download, progress
