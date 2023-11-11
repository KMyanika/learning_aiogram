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


    @staticmethod
    def push_button_contacts(self):
        text = f'*Мои контакты*\n\n' \
               f'Мой телеграмм: @yanikam22\n' \
               f'GitHub: [Мой профиль](https://github.com/KMyanika)\n' \
               f'GitHub username: `KMyanika`'
        return text

    @staticmethod
    def push_command_getmyid(self):
        text = f"Ваш ID: `{self.chat.id}`"
        return text

    @staticmethod
    def push_command_start(self):
        text = f"Привет, {self.from_user.username}"
        return text


    @staticmethod
    def push_homework_ege(self, num):
         nums = [0,
                'https://stepik.org/lesson/1038531/step/1?unit=1062781',
                'https://stepik.org/lesson/1038536/step/1?unit=1062771',
                'https://stepik.org/lesson/1038679/step/1?unit=1062786',
                'https://stepik.org/lesson/1038605/step/1?unit=1062782',
                'https://stepik.org/lesson/1038432/step/1?unit=1060804',
                'https://stepik.org/lesson/1038843/step/1?unit=1062794',
                'https://stepik.org/lesson/1038609/step/1?unit=1062783',
                'https://stepik.org/lesson/1038667/step/1?unit=1062772',
                'https://stepik.org/lesson/1038670/step/1?unit=1062777',
                'https://stepik.org/lesson/1038673/step/1?unit=1062787',
                'https://stepik.org/lesson/1038676/step/1?unit=1062784',
                'https://stepik.org/lesson/1038682/step/1?unit=1062773',
                'https://stepik.org/lesson/1038700/step/1?unit=1062785',
                'https://stepik.org/lesson/1038703/step/1?unit=1062210',
                'https://stepik.org/lesson/1038706/step/1?unit=1062774',
                'https://stepik.org/lesson/1038709/step/1?unit=1062775',
                'https://stepik.org/lesson/1038775/step/1?unit=1062778',
                'https://stepik.org/lesson/1038788/step/1?unit=1062788',
                'https://stepik.org/lesson/1038794/step/1?unit=1062789',
                'https://stepik.org/lesson/1038797/step/1?unit=1062790',
                'https://stepik.org/lesson/1038803/step/1?unit=1062776',
                'https://stepik.org/lesson/1038834/step/1?unit=1062779',
                'https://stepik.org/lesson/1038816/step/1?unit=1062780'

         ]
         text=f'#ДЗ по {num} номеру ЕГЭ ([ссылка]({nums[num]}))'
         return text


    @staticmethod
    def push_homework_python(self, num):
        nums = [0,
                'https://stepik.org/lesson/1051626/step/1?unit=1060712',
                'https://stepik.org/lesson/1051610/step/1?unit=1060696',
                'https://stepik.org/lesson/1051612/step/1?unit=1060698',
                'https://stepik.org/lesson/1051615/step/1?unit=1060701',
                'https://stepik.org/lesson/1051621/step/1?unit=1060707',
                'https://stepik.org/lesson/1051693/step/1?unit=1060783']
        text = f'#ДЗ по теории python ([ссылка]({nums[num]}))'
        return text


    @staticmethod
    def push_take_homework(self):
        text = "Просто скопируйте свой код из PyCharm. \n" \
               "Бот сформирует файл и отправит его за вас 🤖\n\n " \
               "Обратите внимание, сообщение в Telegram ограничено 4096 символами!"
        return text


    @staticmethod
    def push_succesful_take_homework(self):
        text = "Домашнее задание успешно отправлено"
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

    @staticmethod
    def push_if_use_command_start(self):
        text = f'#newuser: @{self.from_user.username}\n' \
               f'ID: `{self.chat.id}`\n' \
               f'[Написать сообщение](tg://user?id={self.chat.id})'
        return text


    @staticmethod
    def push_command_start():
        text = "Привет, админ"
        return text

    @staticmethod
    def push_student_send_homework(self, name, message_homework):
        text = f'#домашка: студент #{name}\n\n' \
               f'{message_homework}'
        return text


    @staticmethod
    def push_student_take_homework_ege(self, name, num):
        nums = [0,
                'https://stepik.org/lesson/1038531/step/1?unit=1062781',
                'https://stepik.org/lesson/1038536/step/1?unit=1062771',
                'https://stepik.org/lesson/1038679/step/1?unit=1062786',
                'https://stepik.org/lesson/1038605/step/1?unit=1062782',
                'https://stepik.org/lesson/1038432/step/1?unit=1060804',
                'https://stepik.org/lesson/1038843/step/1?unit=1062794',
                'https://stepik.org/lesson/1038609/step/1?unit=1062783',
                'https://stepik.org/lesson/1038667/step/1?unit=1062772',
                'https://stepik.org/lesson/1038670/step/1?unit=1062777',
                'https://stepik.org/lesson/1038673/step/1?unit=1062787',
                'https://stepik.org/lesson/1038676/step/1?unit=1062784',
                'https://stepik.org/lesson/1038682/step/1?unit=1062773',
                'https://stepik.org/lesson/1038700/step/1?unit=1062785',
                'https://stepik.org/lesson/1038703/step/1?unit=1062210',
                'https://stepik.org/lesson/1038706/step/1?unit=1062774',
                'https://stepik.org/lesson/1038709/step/1?unit=1062775',
                'https://stepik.org/lesson/1038775/step/1?unit=1062778',
                'https://stepik.org/lesson/1038788/step/1?unit=1062788',
                'https://stepik.org/lesson/1038794/step/1?unit=1062789',
                'https://stepik.org/lesson/1038797/step/1?unit=1062790',
                'https://stepik.org/lesson/1038803/step/1?unit=1062776',
                'https://stepik.org/lesson/1038834/step/1?unit=1062779',
                'https://stepik.org/lesson/1038816/step/1?unit=1062780'

                ]
        text = f'#ДЗ Студент #{name} получил домашку по {num} номеру ЕГЭ ([ссылка]({nums[num]}))'
        return text



    @staticmethod
    def push_student_take_homework_python(self, name, num):
        nums = [0,
                'https://stepik.org/lesson/1051626/step/1?unit=1060712',
                'https://stepik.org/lesson/1051610/step/1?unit=1060696',
                'https://stepik.org/lesson/1051612/step/1?unit=1060698',
                'https://stepik.org/lesson/1051615/step/1?unit=1060701',
                'https://stepik.org/lesson/1051621/step/1?unit=1060707',
                'https://stepik.org/lesson/1051693/step/1?unit=1060783']
        text = f'#ДЗ Студент #{name} получил домашку по теории python ([ссылка]({nums[num]}))'
        return text


