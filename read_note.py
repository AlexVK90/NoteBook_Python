import json
import os

def read_note():
    if os.path.isfile("notes.json"):  
        with open("notes.json", "r") as f:
            notes = json.load(f)
            for note in notes:
                print(f"{ note['title']}: {note['text']} \n {note ['data']}")
                print("---------------")
    else:
        print("Файл заметок не найден.")            