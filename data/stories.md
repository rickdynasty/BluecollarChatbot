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
  - utter_deny

## affirm
* affirm
  - utter_affirm
  
## deny 
* deny
    - utter_deny
    
## bye
* bye
  - utter_bye
  
## bye with greet
* greet
  - utter_greet
* bye
  - utter_bye
  
## thank
* thank
    - utter_thank
    
## thank with greet
* greet
  - utter_greet
* thank
    - utter_thank

## greet + thanks + goodbye
* greet
  - utter_greet
* thank
  - utter_thank
* bye
  - utter_bye
    
## who are you
* whoareyou
    - utter_whoareyou
    
## what to do
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