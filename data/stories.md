## greet
* greet
  - utter_greet

## affirm with greet
* greet
  - utter_greet
* affirm
  - utter_affirm

## thank with greet
* greet
    - utter_greet
* thank
    - utter_thank

## deny with greet
* greet
  - utter_greet
* deny
  - utter_bye

## affirm
* affirm
  - utter_affirm
  
## deny 
* deny
    - utter_deny
    
## bye
* bye
  - utter_bye
    
## thank
* thank
    - utter_thank
    
## stop 
* stop
    - utter_stop
    
## who are you
* whoareyou
    - utter_whoareyou
    
## what to do
* whattodo
    - utter_whattodo
    
## request weather
* request_weather
    - weather_form                  <!--运行sales_form Action-->
    - form{"name": "weather_form"}  <!--激活这个form-->
    - form{"name": null}            <!--停用这个form-->
    
## just request weather, continue
* request_weather
    - weather_form
    - form{"name": "weather_form"}
* faq
    - respond_faq
    - weather_form
    - form{"name": null}
    
## explain address
* request_weather
    - weather_form
    - form{"name": "weather_form"}
    - slot{"requested_slot": "email"}
* explain
    - utter_ask_address
    - weather_form
    - form{"name": null}

## explain date-time
* request_weather
    - weather_form
    - form{"name": "weather_form"}
    - slot{"requested_slot": "date-time"}
* explain
    - utter_ask_date-time
    - weather_form
    - form{"name": null}