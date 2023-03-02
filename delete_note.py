import os
import json

def delete_note():
    title = input("Введите заголовок заметки для удаления: ")
    if os.path.isfile("notes.json"):
        with open("notes.json", "r+") as f:
            notes = json.load(f)
            for note in notes:
                if note["title"] == title:         
                    notes.remove(note)
                    f.seek(0)
                    json.dump(notes, f, indent=4)
                    f.truncate()
                    print("Заметка успешно удалена!")
                    return
            print("Заметка с таким заголовком не найдена.")
    else:    
        print("Файл с заметками не найден.")
