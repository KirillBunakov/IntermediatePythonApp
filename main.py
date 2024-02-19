import datetime

# Инициализируем список с шаблонными данными
notes_title = []
notes_body = []

while True:
    # Показываем пользователю возможные команды для работы с приложением
    print("Введите 'q для выхода")
    print("Введите 'add' чтобы добавить заметку: ")
    print("Введите 'show' чтобы просмотреть заметку: ")
    print("Введите 'show all' чтобы просмотреть все заметки: ")
    print("Введите 'edit note' чтобы отредактировать заметку: ")
    print("Введите 'delete' чтобы отредактировать заметку: ")
    print("Введите 'save' для сохранения заметки в файл")
    q = input()
    # Проверяем введеные данные пользовател
    if q == 'q':
        break
    if q == "add":
        # Функция заголовка и поля заметки в списки
        x = input("Введите заголовок заметки: ")
        notes_title.append(x)
        y = input("Введите заметку: ")
        notes_body.append(y)
        print("Заметка успешно добавлена")
    if q == "show":
        # Функция показа заметки на заданному номеру
        numberNote = int(input("Введите номер заметки для отображения: "))
        if numberNote > len(notes_title):
            print("Заметки под номером", numberNote, "не существует")
        else:
            print("---------")
            print("Заметка номер:", numberNote)
            print("Заголовок:", notes_title[numberNote-1])  # вывод заголовка
            # вывод тела заметки
            print("Поле заметки: ", notes_body[numberNote-1])
            print("---------")
    if q == "show all":
        # Функция показа всех заметок
        for i in range(len(notes_title)):
            print("Заметка номер:", i+1)
            print("Заголовок:", notes_title[i])
            print("Поле заметки:", notes_body[i])
            print("---------")
    if q == "edit note":
        # Функция изменения заметки
        numberNote = int(input("Введите номер заметки для редактирования: "))
        print("Данные которые Вы хотите перезаписать:",
              notes_body[numberNote-1])
        a = input("Введите новое поле заметки: ")
        notes_body[numberNote-1] = a
        print("Заметка успешно отредактирована")
    if q == "delete":
        # Функция удаления заметки
        numberNote = int(input("Введите номер заметки для удаления: "))
        notes_title.remove(notes_title[numberNote-1])
        notes_body.remove(notes_body[numberNote-1])
        print("Заметка номер", numberNote, "успешно удалена")
        print("Осталось заметок", len(notes_body))
    if q == 'save':
        # Функция сохранения в новый файл / или перезапись в уже созданный
        with open("notes.json", "w") as file:
            for i in range(len(notes_title)):
                file.write("Заголовок: ")
                file.write(notes_title[i])
                file.write(" Заметка: ")
                file.write(notes_body[i] + '\n')
            now = datetime.datetime.now()
            file.write("Время создания файла: ")
            file.write(now.strftime("%d-%m-%Y %H:%M:%S"))
        file.close()
        print("Ваши заметки успешно сохранены в файл")
        break
