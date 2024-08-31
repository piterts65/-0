def send_email(message, recipient, *, sender="university.help@gmail.com"):
    konec = (".com", ".ru", ".net")
    if '@' not in recipient or not recipient.endswith(konec):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    if '@' not in sender or not sender.endswith(konec):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif "university.help@gmail.com" not in sender:
        print(f'"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}."')
    else:
        print(f'"Письмо успешно отправлено с адреса {sender} на адрес {recipient}."')

send_email('Это сообщение для проверки связи', 'vasyok@1337gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')