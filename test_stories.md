## greet + goodbye
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