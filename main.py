import config
from text import HELLO
from vk_api.longpoll import VkEventType
from config import write_message_menu,write_message_timetable,write_message_image,write_message_null,prov,write_message_return
from lessons import lessons_p

waint = 0
for event in config.longpoll.listen(): # Ожидание сообщения от сервера VK
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:  # Проверка отправки сообщения, адресованное боту. Проверка, что сообщение является текстом.
        reseived_message = event.text
        sender = event.user_id
        mailer = sender
        temp = False

        temp = prov(reseived_message)
        # КНОПКА ПРИВЕТСТВИЯ
        if reseived_message == "Начать":
            write_message_menu(sender,HELLO)
        # КНОПКА ВОЗВРАТА В МЕНЮ
        elif reseived_message == "Возврат в меню":
            write_message_menu(sender,"Введи команду:")

        # ОСНОВНОЕ МЕНЮ
        elif reseived_message == "Расписание":
            write_message_timetable(sender, "Выбери тип расписания: ")

        # РАСПИСАНИЕ
        elif reseived_message == "Расписание занятий":
            write_message_null(sender,"Введи название группы: ")
            mailer = sender
            wait = 1

        elif reseived_message == "Расписание звонков":
            write_message_image(sender," ")

        else:
            if temp == False:
                write_message_menu(sender, "Неверно введена команда или название группы, пожалуйста, повторите попытку")



        if temp == True and sender == mailer and wait == 1:
            lessons_p(sender, reseived_message)
            write_message_return(sender, "Для возврата в меню нажмите на кнопку")
            wait = 0

