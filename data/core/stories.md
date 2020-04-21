## greet
* greet
  - utter_greet
> check_greet

## affirm
* affirm
  - utter_affirm
  
## deny 
* deny
    - utter_deny
  
## thank
* thank
    - utter_thank
    
## bye
* bye
  - utter_bye

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
    
## explain address
* request_weather
    - weather_form
    - form{"name": "weather_form"}
    - slot{"requested_slot": "address"}
* explain
    - utter_explain_why_address
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
    - slot{"requested_slot": "address"}
* form: inform{"address": "深圳"}
    - slot{"address": "深圳"}
    - form: weather_form
    - slot{"address": "深圳"}

## interactive_story_2
    - form{"name": null}
    - slot{"requested_slot": null}
* request_weather
    - weather_form
    - form{"name": "weather_form"}
    - slot{"date_time": "今天"}
    - slot{"requested_slot": "address"}
* explain
    - utter_explain_why_address
    - weather_form
    - slot{"requested_slot": "address"}
* form: inform{"address": "长沙"}
    - slot{"address": "长沙"}
    - form: weather_form
    - slot{"address": "长沙"}

## interactive_story_3
    - form{"name": null}
    - slot{"requested_slot": null}
* inform{"address": "深圳", "date_time": "今天"}
    - slot{"address": "深圳"}
    - slot{"date_time": "今天"}
    - weather_form
    - form{"name": "weather_form"}
    - slot{"date_time": "今天"}
    - slot{"address": "深圳"}
    - slot{"date_time": "今天"}
    - slot{"address": "深圳"}

## interactive_story_4
    - form{"name": null}
    - slot{"requested_slot": null}
* request_weather
    - weather_form
    - form{"name": "weather_form"}
    - slot{"date_time": "今天"}
    - slot{"requested_slot": "address"}
* greet
    - utter_greet
    - weather_form
    - slot{"requested_slot": "address"}
* form: inform{"address": "商丘"}
    - slot{"address": "商丘"}
    - form: weather_form
    - slot{"address": "商丘"}

## interactive_story_5
    - form{"name": null}
    - slot{"requested_slot": null}
* request_weather
    - weather_form
    - form{"name": "weather_form"}
    - slot{"date_time": "今天"}
    - slot{"requested_slot": "address"}
* whatcanudo
    - utter_whatcanudo
    - weather_form
    - slot{"requested_slot": "address"}
* form: inform{"address": "萍乡"}
    - slot{"address": "萍乡"}
    - form: weather_form
    - slot{"address": "萍乡"}