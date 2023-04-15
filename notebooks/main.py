import json
import datetime


def load_notes():
    try:
        with open('notes.json', 'r') as f:
            notes = json.load(f)
    except FileNotFoundError:
        notes = []
    return notes


def save_notes(notes):
    with open('notes.json', 'w') as f:
        json.dump(notes, f, indent=4)


def create_note():
    title = input('Введите заголовок заметки: ')
    body = input('Введите тело заметки: ')
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    note = {
        'id': len(notes) + 1,
        'title': title,
        'body': body,
        'timestamp': timestamp
    }
    notes.append(note)
    print('Заметка успешно создана!')


def read_note():
    if not notes:
        print('Нет доступных заметок.')
    else:
        note_id = input('Введите идентификатор заметки: ')
        note = next(
            (note for note in notes if note['id'] == int(note_id)), None)
        if note:
            print(f'Заголовок: {note["title"]}')
            print(f'Тело: {note["body"]}')
            print(f'Дата/время создания: {note["timestamp"]}')
        else:
            print('Заметка не найдена.')


def update_note():
    if not notes:
        print('Нет доступных заметок.')
    else:
        note_id = input('Введите идентификатор заметки: ')
        note = next(
            (note for note in notes if note['id'] == int(note_id)), None)
        if note:
            title = input(
                'Введите новый заголовок заметки (оставьте пустым, чтобы не изменять): ')
            body = input(
                'Введите новое тело заметки (оставьте пустым, чтобы не изменять): ')
            if title:
                note['title'] = title
            if body:
                note['body'] = body
            note['timestamp'] = datetime.datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S')
            print('Заметка успешно обновлена!')
        else:
            print('Заметка не найдена.')


def delete_note():
    if not notes:
        print('Нет доступных заметок.')
    else:
        note_id = input('Введите идентификатор заметки: ')
        note = next(
            (note for note in notes if note['id'] == int(note_id)), None)
        if note:
            notes.remove(note)
            print('Заметка успешно удалена!')
        else:
            print('Заметка не найдена.')


def show_menu():
    print('Меню:')
    print('1. Создать заметку')
    print('2. Прочитать заметку')
    print('3. Обновить заметку')
    print('4. Удалить заметку')
    print('5. Выйти')

notes = load_notes()

while True:
    show_menu()
    choice = input('Введите номер команды: ')
    if choice == '1':
        create_note()
    elif choice == '2':
        read_note()
    elif choice == '3':
        update_note()
    elif choice == '4':
        delete_note()
    elif choice == '5':
        save_notes(notes)
        print('Программа завершена. До свидания!')
        break
    else:
        print('Некорректный выбор. Попробуйте еще раз.')

