import customtkinter
import json


def settings_window():
    
    # this is the function called when the button is clicked
    def save_settings():
        language = language_combo.get() # get the selected language from the combobox
        with open('settings.json', 'r+') as f:
            data = json.load(f) # load the JSON data from the file
            data['language'] = language # add the new language entry to the data
            f.seek(0) # move the file pointer to the beginning of the file
            json.dump(data, f, indent=4) # write the updated data back to the file with indentation
        status.configure(text='✅')
        

    root = customtkinter.CTk()
    

    # This is the section of code which creates the main window
    root.geometry('250x150')
    root.title('settings')
    root.iconbitmap("icon.ico")


    # This is the section of code which creates the a label
    customtkinter.CTkLabel(root, text='Language:').pack(pady=10)


    # This is the section of code which creates a combo box
    language_combo= customtkinter.CTkComboBox(root, values=['English', 'Deutsch', 'Espanol'])
    language_combo.pack()


    # This is the section of code which creates a button
    customtkinter.CTkButton(root, text='save', command=save_settings).pack(pady=20)

    status = customtkinter.CTkLabel(root, text='')
    status.place(x=3, y=125)


    root.mainloop()
    