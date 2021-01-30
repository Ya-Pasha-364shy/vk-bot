import re

import vk_api
import json
from vk_api.longpoll import VkLongPoll, VkEventType

import random

from vk_bot import VkBot

main_keyboard = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "О нас 🎯"
            },
            "color": "positive"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "Мероприятия 🍔"
            },
            "color": "positive"
        },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "Приложения 🌏"
                },
                "color": "positive"
            }
        ],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"4\"}",
                "label": "Контакты 📙"
            },
            "color": "primary"
        }]
    ]
}

main_keyboard = json.dumps(main_keyboard, ensure_ascii=False).encode('utf-8')
main_keyboard = str(main_keyboard.decode('utf-8'))


about_us_keyboard = {
    "inline": True,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Основная информация"
            },
            "color": "positive"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "Чем мы занимаемся ?"
            },
            "color": "primary"
        },
        {
            "action": {
                "type": "text",
                "payload": "{\"button\": \"3\"}",
                "label": "Где мы находимся ?",
            },
            "color": "positive"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"4\"}",
                "label": "Как попасть в команду ?",
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"5\"}",
                "label": "Контакты 📙",
            },
            "color": "secondary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"6\"}",
                "label": "Задать вопрос руководителю проекта",
            },
            "color": "negative"
        }]
    ],
}

about_us_keyboard = json.dumps(about_us_keyboard, ensure_ascii=False).encode('utf-8')
about_us_keyboard = str(about_us_keyboard.decode('utf-8'))

events_keyboard = {
    "inline": True,
    "buttons": [
        [{
            "action": {
                "type": "callback",
                "payload": "{\"button\": \"1\"}",
                "label": "Ближайшие мероприятия"
            },
            "color": "negative"
        }],
        [{
            "action": {
                "type": "callback",
                "payload": "{\"button\": \"2\"}",
                "label": "Проведённые мероприятия"
            },
            "color": "positive"
        }],
        [{
            "action": {
                "type": "callback",
                "payload": "{\"button\": \"3\"}",
                "label": "Волонтёрство на мероприятие"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "callback",
                "payload": "{\"button\": \"4\"}",
                "label": "Действующие проекты в НГТУ"
            },
            "color": "secondary"
        }],
        [{
            "action": {
                "type": "callback",
                "payload": "{\"button\": \"5\"}",
                "label": "Мероприятия Межвузовского центра"
            },
            "color": "positive"
        }]
    ],
}

events_keyboard = json.dumps(events_keyboard, ensure_ascii=False).encode('utf-8')
events_keyboard = str(events_keyboard.decode('utf-8'))

app_keyboard = {
    "inline": True,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Узнать точное время 🕐"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "open_link",
                "payload": "{\"button\": \"2\"}",
                "label": "Зайти в Google 📟",
                "link": "https://www.google.com/"
            }
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"3\"}",
                "label": "Узнать погоду ⛅"
            },
            "color": "positive"
        }],
        [{
            "action": {
                "type": "callback",
                "payload": "{\"button\": \"4\"}",
                "label": "Калькулятор 💡"
            },
            "color": "negative"
        }]
    ]
}

app_keyboard = json.dumps(app_keyboard, ensure_ascii=False).encode('utf-8')
app_keyboard = str(app_keyboard.decode('utf-8'))

contacts_keyboard = {
    "inline": True,
    "buttons": [
        [{
            "action": {
                "type": "open_link",
                "payload": "{\"button\": \"1\"}",
                "label": "Никите",
                "link": "https://vk.com/nikyats"
            }
        },
            {
                "action": {
                    "type": "open_link",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Алексею",
                    "link": "https://vk.com/alex_xs"
                }
            }],
        [{
            "action": {
                "type": "open_link",
                "payload": "{\"button\": \"3\"}",
                "label": "Илье",
                "link": "https://vk.com/ki1337ki"
            }
        }],
        [{
            "action": {
                "type": "open_link",
                "payload": "{\"button\": \"3\"}",
                "label": "Связаться с тех. поддержкой",
                "link": "https://vk.com/setmyaddresspls"
            }
        }],

    ]
}

contacts_keyboard = json.dumps(contacts_keyboard, ensure_ascii=False).encode('utf-8')
contacts_keyboard = str(contacts_keyboard.decode('utf-8'))

go_answer = {
    "inline": True,
    "buttons": [
        [{
            "action": {
                "type": "open_link",
                "payload": "{\"button\": \"1\"}",
                "label": "Написать руководителю проекта",
                "link": "https://vk.com/id8970990"
            }
        }]
    ]
}

go_answer = json.dumps(go_answer, ensure_ascii=False).encode('utf-8')
go_answer = str(go_answer.decode('utf-8'))

in_team = {
    "inline": True,
    "buttons": [
        [{
            "action": {
                "type": "open_link",
                "payload": "{\"button\": \"1\"}",
                "label": "Написать Никите",
                "link": "https://vk.com/nikyats"
            }
        }],
        [{
            "action": {
                "type": "open_link",
                "payload": "{\"button\": \"2\"}",
                "label": "Подать заявку на проект 612",
                "link": "https://project-study.nstu.ru/project?id=612"
            }
        }]
    ]
}

in_team = json.dumps(in_team, ensure_ascii=False).encode('utf-8')
in_team = str(in_team.decode('utf-8'))

calc_keyboard = {
    "inline": True,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"1\"}",
                "label": "Сложить числа"
            },
            "color": "positive"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"2\"}",
                "label": "Вычесть числа",
            },
            "color": "positive"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"3\"}",
                "label": "Умножить числа",
            },
            "color": "positive"
        }],
        [{
            "action": {
                "type": "text",
                "payload": "{\"button\": \"3\"}",
                "label": "Разделить числа",
            },
            "color": "positive"
        }]
    ]
}

calc_keyboard = json.dumps(calc_keyboard, ensure_ascii=False).encode('utf-8')
calc_keyboard = str(calc_keyboard.decode('utf-8'))


def write_msg(user_id, message, key):
    vk.method('messages.send',
              {'user_id': user_id,
               'message': message,
               'keyboard': key,
               'random_id': random.randint(0, 2048)})


vk = vk_api.VkApi(token=
                  "Your_token_there")


longpoll = VkLongPoll(vk)


try:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                bot = VkBot(event.user_id)

                if event.text.lower() == "о нас 🎯":
                    write_msg(event.user_id, "Немного о нашем проекте", about_us_keyboard)
                elif event.text.lower() == "мероприятия 🍔":
                    write_msg(event.user_id, "Что ты хочешь узнать?", events_keyboard)
                elif event.text.lower() == "приложения 🌏":
                    write_msg(event.user_id, "Посмотри, что есть здесь!", app_keyboard)
                elif event.text.lower() == "контакты 📙":
                    write_msg(event.user_id, "По любым вопросам можешь обращаться к:", contacts_keyboard)
                elif event.text.lower() == "задать вопрос руководителю проекта":
                    write_msg(event.user_id, "У тебя есть возможность написать сообщение нашему Руководителю проекта 👇",
                              go_answer)
                elif event.text.lower() == "калькулятор 💡":
                    write_msg(event.user_id, "В разработке...", calc_keyboard)
                # elif event.text == " ".join(re.findall('\d{2}', event.text)):
                #     write_msg(event.user_id, "Отлично, мы здесь", calc_keyboard)
                elif event.text.lower() == "как попасть в команду ?":
                    write_msg(event.user_id, "Напиши координатору проекта - Никите\n"
                                             "или перейди на сайт проектной деятельности,\n"
                                             "найди проект номер 612 и подай заявку", in_team)
                else:
                    write_msg(event.user_id, bot.new_message(event.text), main_keyboard)

except Exception as e:
    print(e)
