from datetime import datetime
import os
import json

def create_note():
    title = input("Введите заголовок заметки: ")
    text = input("Введите текст заметки: ")
    data = datetime.now().strftime("%d/%m/%Y")
    new_note = {
        "title": title,
        "text": text,
        "data": data
    }

    
    if os.path.isfile("notes.json"):
        with open("notes.json", "r+") as f:
            notes = json.load(f)
            notes.append(new_note)
            f.seek(0)
            json.dump(notes, f, indent=4)
            f.truncate()

    else:
        with open("notes.json", "w") as f:
            json.dump([new_note], f, indent=4)

    print("Заметка успешно создана!")        
