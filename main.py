import config
from text import HELLO
from vk_api.longpoll import VkEventType
from config import write_message_menu, write_message_timetable, write_message_image, write_message_null, prov, \
    write_message_return
from lessons import lessons_p

wait = 0    # ОЖИДАНИЕ ОТВЕТА ГРУППЫ
for event in config.longpoll.listen():  # Ожидание сообщения от сервера VK
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:  # Проверка отправки сообщения, адресованное боту. Проверка, что сообщение является текстом.
        reseived_message = event.text
        sender = event.user_id
        mailer = sender
        gr_check = False

        gr_check = prov(reseived_message)   # ПРОВЕРКА ГРУППЫ
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
            wait = 1

        elif reseived_message == "Расписание звонков":
            write_message_image(sender, " ")

        elif reseived_message == "Расписание сессии":
            write_message_return(sender, "В данный момент расписание сессии не имеется")

        else:
            if wait == 1 and gr_check == False:
                write_message_null(sender, "Неверно введено название группы, пожалуйста, повторите попытку")

            elif gr_check == True and wait == 0:
                write_message_timetable(sender, 'Для того, чтобы вывести расписание группы, нужно '
                                           'написать/выбрать команду "Расписание занятий"')

            elif gr_check == False:
                write_message_menu(sender, "Неверно введена команда, пожалуйста, повторите попытку")

        if gr_check == True and sender == mailer and wait == 1:
            lessons_p(sender, reseived_message)
            write_message_return(sender, "Для возврата в меню нажмите на кнопку")
            wait = 0