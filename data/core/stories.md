## pasc chat story0
* affirm OR greet_shout OR greet OR thank OR bye OR whoareyou OR whatcanudo OR deny
  - action_pasc_chatqa

## greet
* greet
  - utter_greet
> check_greet

## greet + affirm
> check_greet
* affirm
  - utter_affirm

## greet + deny
> check_greet
* deny
  - utter_deny
  
## greet + bye
> check_greet
* bye
  - utter_bye
    
## greet + thank
> check_greet
* thank
    - utter_thank

## greet + thanks + bye
> check_greet
* thank
  - utter_thank
* bye
  - utter_bye
  
## greet + affirm + thanks
> check_greet
* affirm
  - utter_affirm
* thank
    - utter_thank
> check_greet_affirm_thanks

## greet + deny + thanks
> check_greet
* deny
  - utter_deny
* thank
    - utter_thank
> check_greet_deny_thanks
  
## greet + affirm + thanks + bye
> check_greet_affirm_thanks
* bye
  - utter_bye

## greet + deny + thanks + bye
> check_greet_deny_thanks
* bye
  - utter_bye
    
## who are you
* whoareyou
    - utter_whoareyou
    
## what to do
* whatcanudo
    - utter_whatcanudo

## greet + who are you
> check_greet
* whoareyou
    - utter_whoareyou
    
## greet + what to do
> check_greet
* whatcanudo
    - utter_whatcanudo
    
## request weather
* request_weather
    - weather_form                  <!--运行weather_form Action-->
    - form{"name": "weather_form"}  <!--激活这个form-->
    - form{"name": null}            <!--停用这个form-->
    
## unhappy path - request weather
* request_weather
    - weather_form
    - form{"name": "weather_form"}
* bye
    - utter_ask_continue
* affirm
    - action_deactivate_form
    - form{"name": null}
    
## explain city
* request_weather
    - weather_form
    - form{"name": "weather_form"}
    - slot{"requested_slot": "city"}
* explain
    - utter_explain_why_city
    - weather_form
    - form{"name": null}

## explain date_time
* request_weather
    - weather_form
    - form{"name": "weather_form"}
    - slot{"requested_slot": "date_time"}
* explain
    - utter_explain_why_date_time
    - weather_form
    - form{"name": null}

## interactive_story_1
* request_weather
    - weather_form
    - form{"name": "weather_form"}
    - slot{"date_time": "今天"}
    - slot{"requested_slot": "city"}
* form: inform{"city": "深圳"}
    - slot{"city": "深圳"}
    - form: weather_form
    - slot{"city": "深圳"}

## interactive_story_2
    - form{"name": null}
    - slot{"requested_slot": null}
* request_weather
    - weather_form
    - form{"name": "weather_form"}
    - slot{"date_time": "今天"}
    - slot{"requested_slot": "city"}
* explain
    - utter_explain_why_city
    - weather_form
    - slot{"requested_slot": "city"}
* form: inform{"city": "长沙"}
    - slot{"city": "长沙"}
    - form: weather_form
    - slot{"city": "长沙"}

## interactive_story_3
    - form{"name": null}
    - slot{"requested_slot": null}
* inform{"city": "深圳", "date_time": "今天"}
    - slot{"city": "深圳"}
    - slot{"date_time": "今天"}
    - weather_form
    - form{"name": "weather_form"}
    - slot{"date_time": "今天"}
    - slot{"city": "深圳"}
    - slot{"date_time": "今天"}
    - slot{"city": "深圳"}

## interactive_story_4
    - form{"name": null}
    - slot{"requested_slot": null}
* request_weather
    - weather_form
    - form{"name": "weather_form"}
    - slot{"date_time": "今天"}
    - slot{"requested_slot": "city"}
* greet
    - utter_greet
    - weather_form
    - slot{"requested_slot": "city"}
* form: inform{"city": "北京"}
    - slot{"city": "北京"}
    - form: weather_form
    - slot{"city": "北京"}

## interactive_story_5
    - form{"name": null}
    - slot{"requested_slot": null}
* request_weather
    - weather_form
    - form{"name": "weather_form"}
    - slot{"date_time": "今天"}
    - slot{"requested_slot": "city"}
* whatcanudo
    - utter_whatcanudo
    - weather_form
    - slot{"requested_slot": "city"}
* form: inform{"city": "广州"}
    - slot{"city": "广州"}
    - form: weather_form
    - slot{"city": "广州"}