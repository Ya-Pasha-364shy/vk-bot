import bs4 as bs4

import requests
import answers


class VkBot:

    def __init__(self, user_id):
        self.USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)
        self.my_str = ""
        self._COMMANDS = ["привет", "погода", "время", "пока"]

        self._inputMes = {"основная информация": answers.about_us1,
                          "чем мы занимаемся ?": answers.about_us2,
                          "где мы находимся ?": answers.about_us3,
                          "ближайшие мероприятия": answers.events1,
                          "проведённые мероприятия": answers.events2,
                          "волонтёрство на мероприятие": answers.events3,
                          "действующие проекты в нгту": answers.events4,
                          "мероприятия межвузовского центра": answers.events5
                          }

    def _get_weather(self):

        city = "новосибирск"
        page = requests.get("https://sinoptik.com.ru/погода-" + city)
        soup = bs4.BeautifulSoup(page.text, "html.parser")

        output_weather = []

        current_weather = soup.find_all('div', class_="weather__content_tab current")

        for i in range(len(current_weather)):
            if current_weather[i].find('span') is not None:
                output_weather.append(current_weather[i].text)

        out = output_weather[0].strip('\n').split('\n')

        out1 = [i for i in out if i != '']

        answer = f"Сегодня {out1[0]}, {out1[1]} {out1[2]}\nНа улице {out1[3]}\n" \
                 f"Минимальная температура: {out1[5]}\n" \
                 f"Максимальная температура: {out1[7]}\n"

        return answer

    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id" + str(user_id))

        bs = bs4.BeautifulSoup(request.text, "html.parser")

        user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])

        return user_name.split()[0]

    def new_message(self, message):
        # self.my_str = " ".join(re.findall('[0-9]{2}', message))

        if message.lower() == self._COMMANDS[0]:
            return f"Привет, {self._USERNAME}!"

        elif message.lower() == self._COMMANDS[1] or message.lower() == "узнать погоду ⛅":
            return self._get_weather()

        elif message.lower() == self._COMMANDS[2] or message.lower() == "узнать точное время 🕐":
            return self._get_time()

        elif message.lower() == self._COMMANDS[3]:
            return f"До скорой встречи, {self._USERNAME}!"

        else:
            for key, value in self._inputMes.items():
                if message.lower() == key:
                    return value
            return "Не понимаю тебя 🐩"

    def _get_time(self):
        request = requests.get("https://my-calend.ru/date-and-time-today")
        b = bs4.BeautifulSoup(request.text, "html.parser")
        return f'{self._clean_all_tag_from_str(str(b.select(".page")[0].findAll("h2")[1])).split()[1]} по МСК'

    @staticmethod
    def _clean_all_tag_from_str(string_line):

        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True

        return result
