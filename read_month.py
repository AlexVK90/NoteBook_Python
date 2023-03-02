import json
from datetime import datetime
import os

def read_notes_this_month():
    if os.path.isfile("notes.json"):
        today = datetime.today()
        year = today.year
        month = today.month
    
        with open("notes.json", "r") as f:
            notes = json.load(f)
        
            # Фильтруем заметки по месяцу и году
            notes_this_month = [note for note in notes if int(note["date"].split("/")[1]) == month and int(note["date"].split("/")[2]) == year]
        
            if notes_this_month:
                # Выводим заметки
                print(f"Заметки за {today.strftime('%B %Y')}:\n")
                for note in notes_this_month:
                    print(f"Дата: {note['date']}")
                    print(f"Заголовок: {note['title']}")
                    print(f"Текст: {note['text']}\n")
            else:
                print(f"За {today.strftime('%B %Y')} заметок нет.")
    else:
        print("Файл заметок не найден.")