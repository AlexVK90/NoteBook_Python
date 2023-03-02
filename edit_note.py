import os
import json

def edit_note():

    title = input("Введите заголовок заметки для редактирования: ")

    if os.path.isfile("notes.json"):
        with open("notes.json", "r+") as f:
            notes = json.load(f)

            for note in notes:
                if note["title"] == title:
                    new_text = input("Введите новый текст заметки: ")
                    note["text"] = new_text

                    f.seek(0)
                    json.dump(notes, f, indent=4)
                    f.truncate()

                    print("Заметка успешно отредактирована!")
                    return

            print("Заметка с таким заголовком не найдена.")
    else:
        print("Файл с заметками не найден.")
