from create_note import create_note
from read_note import read_note
from edit_note import edit_note
from delete_note import delete_note
from today_notes import print_today_notes
from read_month import read_notes_this_month



def main():
    """Функция для работы с заметками"""
    while True:
        print("\n=======================================")
        print("0. Создать заметку")
        print("1. Заметки за сегодня")
        print("2. Заметки за месяц")
        print("3. Показать список заметок")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("6. Выйти из программы")
        print("---------------------------------------")
        choice = input("Введите номер действия: ")
        if choice == "1":
            print_today_notes()
        elif choice == "0":
            create_note()
        elif choice == "2":
            read_notes_this_month()   
        elif choice == "3":
            read_note()
        elif choice == "4":
            read_note()
            edit_note()
        elif choice == "5":
            delete_note()
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")
            

if __name__ == "__main__":
   main()   