import datetime
import json
import os

def print_today_notes():
    if os.path.isfile("notes.json"):
        today = datetime.date.today()

        with open("notes.json", "r") as f:
            notes = json.load(f)
            today_notes = [note for note in notes if note["date"] == str(today)]

            if today_notes:
                print("Заметки за сегодня:")
                for note in today_notes:
                    print(f"Заголовок: {note['title']}")
                    print(f"Текст: {note['text']}")
            
            else:
                print("За сегодняшний день заметок нет.")
    else:
        print("Файл заметок не найден.")