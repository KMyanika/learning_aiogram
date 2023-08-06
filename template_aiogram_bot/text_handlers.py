"""Модуль для хранения текстовых сообщений."""


class ForUsers():

    def __init__(self, message):
        self.message = message

    @staticmethod
    def push_command_help(self):
        text = f'Напишите свой запрос одним сообщением, используя в тексте #help'
        return text

    @staticmethod
    def push_help_handlers(self):
        text = f'Спасибо, отправил ваше сообщение. Обработаем ваш запрос в течении трёх часов.'
        return text


class ForAdmin():

    def __init__(self, message):
        self.message = message

    @staticmethod
    def push_help_handlers(self, user_text):
        text = f'#help пользователь: @{self.from_user.username}\n' \
               f'ID: `{self.chat.id}`\n' \
               f'[Написать сообщение](tg://user?id={self.chat.id})\n\n' \
               f'Сообщение: {user_text}'
        return text