from rasa_sdk import Tracker, Action
from rasa_sdk.events import UserUtteranceReverted, Restarted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from requests import (
    ConnectionError,
    HTTPError,
    TooManyRedirects,
    Timeout
)
from typing import Dict, Text, Any, List, Union

from actions.ChatApis import get_response
from actions.WeatherApis import get_weather_by_day
from log.BCLog import log


class WeatherForm(FormAction):
    """Collects sales information and adds it to the spreadsheet"""

    def name(self) -> Text:
        return "weather_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["date_time", "city", ]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        city = tracker.get_slot('city')
        date_time = tracker.get_slot('date_time')

        log.info("=========call WeatherForm submit=========")
        log.info("tracker.get_slot city:%s  date_time:%s", city, date_time)
        date_time_number = text_date_to_number_date(date_time)

        if isinstance(date_time_number, str):  # parse date_time failed
            dispatcher.utter_message("暂不支持查询 {} 的天气".format([city, date_time_number]));
        else:
            weather_data = get_text_weather_date(city, date_time, date_time_number)
            log.info("weather_data is %s", weather_data)
            dispatcher.utter_message(weather_data);
        return [Restarted()]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
        """A dictionary to map required slots to

        - intent: value pairs
        - a whole message
            or a list of them, where a first match will be picked"""
        log.info("=========call WeatherForm slot_mappings=========")
        return {
            "city": [
                self.from_entity(entity="city"),
                self.from_text(intent="inform"),
            ],
            "date_time": [
                self.from_entity(entity="date_time"),
                self.from_text(intent="inform"),
                self.from_trigger_intent(intent="request_weather", value=getCurDateTime())
            ],
        }


def getCurDateTime():
    log.info("=========call getCurDateTime=========")
    return "明天"


def get_text_weather_date(city, date_time, date_time_number):
    try:
        result = get_weather_by_day(city, date_time_number)
    except (ConnectionError, HTTPError, TooManyRedirects, Timeout) as e:
        text_message = "{}".format(e)
    else:
        text_message_tpl = """
            {} {} ({}) 的天气情况为：白天：{}；夜晚：{}；气温：{}-{} °C
        """
        text_message = text_message_tpl.format(
            result['location']['name'],
            date_time,
            result['result']['date'],
            result['result']['text_day'],
            result['result']['text_night'],
            result['result']["high"],
            result['result']["low"],
        )

    return text_message


def text_date_to_number_date(text_date):
    if text_date == "今天":
        return 0
    if text_date == "明天":
        return 1
    if text_date == "后天":
        return 2

    # Not supported by weather API provider freely
    if text_date == "大后天":
        # return 3
        return text_date

    if text_date.startswith("星期"):
        # TODO: using calender to compute relative date
        return text_date

    if text_date.startswith("下星期"):
        # TODO: using calender to compute relative date
        return text_date

    # follow APIs are not supported by weather API provider freely
    if text_date == "昨天":
        return text_date
    if text_date == "前天":
        return text_date
    if text_date == "大前天":
        return text_date


class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self):
        return 'action_default_fallback'

    def run(self, dispatcher, tracker, domain):
        log.info("call ActionDefaultFallback run o(╯□╰)o")
        # # 访问图灵机器人API(闲聊)
        # text = tracker.latest_message.get('text')
        # message = get_response(text)
        # if message is not None:
        #     dispatcher.utter_message(message)
        # else:
        # 分支流处理，精准映射到 responses
        dispatcher.utter_template('utter_default', tracker, silent_fail=True)
        return [UserUtteranceReverted()]
