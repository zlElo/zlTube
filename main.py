import customtkinter
from pytube import YouTube
import threading
from tkinter import filedialog
import os
from settings import settings_window
import pyuac
from lang import set_lang
import customtkinter as tk

def video_meta_datas():
    download_path = filedialog.askdirectory()

    # Get the video URL from the entry widget
    url = url_entry.get()

    # Create a YouTube object
    yt = YouTube(url)

    # Get the video details
    title_yt = yt.title
    length_yt = yt.length

    if len(title_yt) > 25:
        title_yt = f'{title_yt[:25]}...'

    # Print the video details
    print("Title:", title_yt)
    print("Length:", length_yt, seconds)

    title_value = f'"{title_yt}"'
    value_title.configure(text=title_value)

    length_value = f'{length_yt} {seconds}'
    value_length.configure(text=length_value)

    # refresh window
    window.update()
    window.update_idletasks()


    if file_format_box.get() == '.mp4':
        download_thread = threading.Thread(target=lambda: download_as_mp4(yt, download_path))
        download_thread.start()

    elif file_format_box.get() == '.mp3':
        download_thread = threading.Thread(target=lambda: download_as_mp3(yt, download_path))
        download_thread.start()

    


def download_as_mp4(yt, download_path):
    # progress title
    label_done.configure(text=downloading, text_color='red')

    # refresh window
    window.update()
    window.update_idletasks()
    

    # Download the video
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    stream.download(download_path)

    # done title
    label_done.configure(text=saved, text_color='green')

    # refresh window
    window.update()
    window.update_idletasks()

    # console logging
    print('[log] download done!')


def download_as_mp3(yt, download_path):
    # progress title
    label_done.configure(text=downloading, text_color='red')

    # refresh window
    window.update()
    window.update_idletasks()
    

    audio_streams = yt.streams.filter(only_audio=True)

    # Wählen Sie den ersten Audio-Stream
    audio = audio_streams.first()

    # Herunterladen des Audio-Streams
    audio.download(download_path)

    # Konvertieren Sie das heruntergeladene Audio in MP3
    base, ext = os.path.splitext(f'{download_path}/{audio.default_filename}')
    new_file = f'{base}.mp3'
    os.rename(f'{download_path}/{audio.default_filename}', new_file)
    

    # done title
    label_done.configure(text=saved, text_color='green')

    # refresh window
    window.update()
    window.update_idletasks()

    # console logging
    print('[log] download done!')


def admin_prompt():
    if pyuac.isUserAdmin():
        settings_window()
    else:
        window.destroy()
        print("[log] re-launching as admin")
        pyuac.runAsAdmin() 
        
        



# Create a Tkinter window
window = customtkinter.CTk()
window.title("zlTube")
window.geometry('300x400')
window.minsize(300, 400)
window.maxsize(300, 400)
window.iconbitmap("icon.ico")



language_ = set_lang()
length = language_[0]
title = language_[1]
seconds = language_[2]
downloading = language_[3]
saved = language_[4]
download = language_[5]
progress = language_[6]


if pyuac.isUserAdmin():
    settings_window()

# main GUI
settings_button = customtkinter.CTkButton(window, text='⚙', width=10, command=admin_prompt)
settings_button.place(x=260, y=10)

# Add a label to prompt the user to enter the video URL
url_label = customtkinter.CTkLabel(window, text='Video URL:')
url_label.pack()

# Add an entry widget to allow the user to enter the video URL
url_entry = customtkinter.CTkEntry(window)
url_entry.pack()

file_format_box = customtkinter.CTkComboBox(window, values=['.mp4', '.mp3'])
file_format_box.pack(pady=10)

# Add a button to initiate the download process
download_button = customtkinter.CTkButton(window, text=download, command=video_meta_datas)
download_button.pack(pady=15)

backround_frame = customtkinter.CTkFrame(window)
backround_frame.pack(pady=30)


title_info_vid = customtkinter.CTkLabel(backround_frame, text=title)
title_info_vid.pack(padx=80, pady=3)

value_title = customtkinter.CTkLabel(backround_frame, text='', text_color='green')
value_title.pack()


length_info_vid = customtkinter.CTkLabel(backround_frame, text=length)
length_info_vid.pack(padx=80, pady=3)

value_length = customtkinter.CTkLabel(backround_frame, text='', text_color='green')
value_length.pack()


label_done_ = customtkinter.CTkLabel(backround_frame, text=progress)
label_done_.pack(padx=80, pady=3)

label_done = customtkinter.CTkLabel(backround_frame, text='', text_color='green')
label_done.pack()



# Display the window
window.mainloop()