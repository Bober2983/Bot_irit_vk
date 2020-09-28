import vk_api
import psycopg2
import time

from vk_api.longpoll import VkLongPoll
from vk_api.utils import get_random_id
from vk_api import VkUpload
from keyboard import menu, timetable, start, return_

# ДАННЫЕ
token = "b42b5b0772a7ed33e092aa71106b250c35fee7dd4a14b08d0b2b4e9735f7bd29d20626b87ebe843ea16bd"  # Ключ доступа к группе
image = "C:/NNTU/Diplom/Project/Bot_irit_vk/picture/call.jpg"  # РАСПИСАНИЕ ЗВОНКОВ

# АВТОРИЗАЦИЯ
login_vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(login_vk)  # Выбор API

# ЗАГРУЗКА ИЗОБРАЖЕНИЯ
upload = VkUpload(login_vk)
upload_image = upload.photo_messages(photos=image)[0]
attachments = []
attachments.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))


# ОБРАБОТКА СООБЩЕНИЙ
def write_message_menu(sender, message):
    login_vk.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                      'keyboard': menu.get_keyboard()})


def write_message_timetable(sender, message):
    login_vk.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                      'keyboard': timetable.get_keyboard()})


def write_message_start(sender, message):
    login_vk.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                      'keyboard': start.get_keyboard()})


def write_message_null(sender, message):
    login_vk.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id()})


def write_message_image(sender, message):
    login_vk.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                      'attachment': ','.join(attachments), 'keyboard': return_.get_keyboard()})


def write_message_return(sender, message):
    login_vk.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                      'keyboard': return_.get_keyboard()})


# СОЕДИНЕНИЕ С БАЗОЙ ДАННЫХ POSTGRESQL
con = psycopg2.connect(
    database="bot",
    user="postgres",
    password="root",
    host="127.0.0.1",
    port="5432"
)


# ЧЕТНОСТЬ НЕЧЕТНОСТЬ НЕДЕЛИ

def ch_nch_week():
    week_year = int(time.strftime('%W', ))
    if (week_year % 2) == 1:
        week_c_n = 'НЧ'
    else:
        week_c_n = 'ЧН'
    return week_c_n


# СПИСОК ГРУПП
def prov(reseived_message):
    command = False
    i = 0
    group = ['20-ИВТ-1', '20-ИВТ-2', '20-ИВТ-3', '20-ИСТ-1', '20-ИСТ-2', '20-ИСТ-3', '20-ИСТ-4', '20-ИТС', '20-КТЭС',
             '20-ПМ-1', '20-ПМ-2', '20-Р', 'С 20-РЭС', '19-ИВТ-1', '19-ИВТ-2', '19-ИВТ-3', '19-ИСТ-1', '19-ИСТ-2',
             '19-ИСТ-3', '19-ИСТ-4', '19-ИТС', '19-КТЭС', '19-ПМ-1', '19-ПМ-2', '19-Р', 'С 19-РЭС']
    while i < len(group):
        if group[i] == reseived_message:
            command = True
        i = i + 1
    return command
