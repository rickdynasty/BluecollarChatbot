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
    
## Some question from FAQ
* faq
    - respond_faq
    
## request weather
* request_weather
    - weather_form                  <!--运行weather_form Action-->
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
    - slot{"requested_slot": "address"}
* explain
    - utter_explain_why_address
    - weather_form
    - form{"name": null}

## explain date-time
* request_weather
    - weather_form
    - form{"name": "weather_form"}
    - slot{"requested_slot": "date-time"}
* explain
    - utter_explain_why_date-time
    - weather_form
    - form{"name": null}