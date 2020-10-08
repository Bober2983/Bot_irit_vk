from keyboard import menu, timetable, start, return_, class_uni
from config import login_vk
from vk_api.utils import get_random_id
from config import attachments


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


def write_message_class(sender, message):
    login_vk.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id(),
                                      'keyboard': class_uni.get_keyboard()})
