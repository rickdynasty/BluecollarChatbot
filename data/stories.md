## interactive_story_1
* request_weather{"date_time": "今天"}
    - slot{"date_time": "今天"}
    - weather_form
    - form{"name": "weather_form"}
    - slot{"date_time": "今天"}
    - slot{"date_time": "今天"}
    - slot{"requested_slot": "city"}
* deny
    - utter_ask_continue
* affirm
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
	
## interactive_story_2
* request_weather
    - weather_form
    - form{"name": "weather_form"}
    - slot{"date_time": "今天"}
    - slot{"requested_slot": "city"}
* deny
    - utter_ask_continue
* continue
    - utter_ask_city
    - action_listen
* form: inform{"city": "北京"}
    - slot{"city": "北京"}
    - weather_form
    - slot{"city": "北京"}

## interactive_story_3
    - form{"name": null}
    - slot{"requested_slot": null}
* request_weather
    - weather_form
    - form{"name": "weather_form"}
    - slot{"date_time": "今天"}
    - slot{"requested_slot": "city"}
* deny
    - utter_ask_continue
* affirm
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
