import vk_api
import psycopg2

from vk_api.longpoll import VkLongPoll
from vk_api import VkUpload

# ДАННЫЕ
token = "22e4298d1190fcf429861b4c5de8e211c5d82d41189b08081358ed4b492d505a91700de9842829e60e90c"  # Ключ доступа к группе
image = "C:/NNTU/Diplom/Project/Bot_irit_vk/picture/call.jpg"  # РАСПИСАНИЕ
doc = "C:/Users/bober/Google Диск/Личное/NNTU/Diplom/Project_bot/Bot_irit_vk/manual/inf.doc"

# АВТОРИЗАЦИЯ
login_vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(login_vk)  # Выбор API

# ЗАГРУЗКА ИЗОБРАЖЕНИЯ
upload = VkUpload(login_vk)
upload_image = upload.photo_messages(photos=image)[0]
attachments = ['photo{}_{}'.format(upload_image['owner_id'], upload_image['id'])]


# СОЕДИНЕНИЕ С БАЗОЙ ДАННЫХ POSTGRESQL
connection_db = psycopg2.connect(
    database="bot",
    user="postgres",
    password="root",
    host="127.0.0.1",
    port="5432"
)
