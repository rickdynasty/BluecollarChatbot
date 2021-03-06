## End-to-End tests where a custom action appends events（greet + goodbye）
* greet: Hi!
  - utter_greet
* bye: Bye
  - utter_bye

## greet + affirm
* greet: Hi!
  - utter_greet
* affirm: 好
  - utter_affirm

## greet + affirm + goodbye
* greet: Hi!
  - utter_greet
* affirm: yes
  - utter_affirm
* bye: 下次再聊
  - utter_bye
  
## greet + thanks
* greet: Hello there
  - utter_greet
* thank: thanks
  - utter_thank
  
## greet + deny + goodbye
* greet: Hello there
  - utter_greet
* deny: 不，谢谢
  - utter_deny
* bye: 886
  - utter_bye

## greet + thanks + goodbye
* greet: Hey
  - utter_greet
* thank: thank you
  - utter_thank
* bye: bye bye
  - utter_bye
  
## ask channels
* faq: rasa支持哪些通讯渠道？
  - respond_faq

## ask languages
* faq: 我可以用哪种语言来构建assistants?
  - respond_faq

## ask rasa x
* faq: Rasa X是什么?
  - respond_faq
  
## request whoareyou
* whoareyou: 你是谁
  - utter_whoareyou
  
## request whatcanudo
* whatcanudo: 你有什么用
  - utter_whatcanudo

## Testing request weather with a form
* greet: hi
    - utter_greet
* request_weather: 查下[今天](date_time)[北京](city)的天气
    - weather_form
    - form{"name": "weather_form"}
* thank: thanks
    - utter_thank

## Testing request weather with a form and unexpected user input
* greet: hi
    - utter_greet
* request_weather: 查下[今天](date_time)的天气
    - weather_form
    - form{"name": "weather_form"}
<!-- The user sends a message which should not be handled by the form. -->
* whatcanudo: 你能做什么
    - utter_whatcanudo
    - weather_form
    - form{"name": null}
    - slot{"requested_slot": "city"}
* thank: thanks
    - utter_thank