import config
from text import HELLO
from vk_api.longpoll import VkEventType
from write_message import write_message_menu, write_message_timetable, write_message_image, write_message_null, \
    write_message_return
from lessons import lessons
from auxiliary_def import gr_availability

# ОБЪЯВЛЕНИЕ ДАННЫЕ
wait_gr = 0  # ОЖИДАНИЕ ОТВЕТА ГРУППЫ
mailer = ''  # ID ПОЛЬЗОВАТЕЛЯ, КОТОРЫЙ НАЖАЛ КНОПКУ "РАСПИСАНИЕ ЗАНЯТИЙ" - НУЖНО ДЛЯ ТОГО, ЧТОБЫ БОТ НЕ ЗАСТОПОРИЛСЯ

for event in config.longpoll.listen():  # Ожидание сообщения от сервера VK
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:  # Проверка отправки сообщения,
        # адресованное боту. Проверка, что сообщение является текстом.
        reseived_message = event.text
        sender = event.user_id
        # gr_check = False
        gr_check = gr_availability(reseived_message)  # ПРОВЕРКА ГРУППЫ

        # КНОПКА ПРИВЕТСТВИЯ
        if reseived_message == "Начать":
            write_message_menu(sender, HELLO)
        # КНОПКА ВОЗВРАТА В МЕНЮ
        elif reseived_message == "Возврат в меню":
            write_message_menu(sender, "Введи команду:")
        # ОСНОВНОЕ МЕНЮ
        elif reseived_message == "Расписание":
            write_message_timetable(sender, "Выбери тип расписания: ")

        # РАСПИСАНИЕ
        elif reseived_message == "Расписание занятий":
            write_message_null(sender, "Введи название группы: ")
            mailer = sender
            wait_gr = 1

        elif reseived_message == "Расписание звонков":
            write_message_image(sender, " ")

        elif reseived_message == "Расписание сессии":
            write_message_return(sender, "В данный момент расписание сессии не имеется")

        else:
            if wait_gr == 1 and not gr_check:
                write_message_null(sender, "Неверно введено название группы, пожалуйста, повторите попытку")

            elif gr_check and wait_gr == 0:
                write_message_timetable(sender, 'Для того, чтобы вывести расписание группы, нужно '
                                                'написать/выбрать команду "Расписание занятий"')

            elif not gr_check:
                write_message_menu(sender, "Неверно введена команда, пожалуйста, повторите попытку")

        if gr_check and sender == mailer and wait_gr == 1:
            lessons(sender, reseived_message)
            write_message_return(sender, "Для возврата в меню нажмите на кнопку")
            wait_gr = 0
