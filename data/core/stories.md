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
* form: inform{"city": "商丘"}
    - slot{"city": "商丘"}
    - form: weather_form
    - slot{"city": "商丘"}

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
* form: inform{"city": "萍乡"}
    - slot{"city": "萍乡"}
    - form: weather_form
    - slot{"city": "萍乡"}

## ask familyplanning
* ask_fp_certificate OR ask_fp_service_card OR deal_with_family_planning OR ask_fp_expatriate OR ask_fp_maternity_insurance OR ask_fp_only_child_reward OR ask_fp_technical_services OR determine_fp_surgical_complications OR ask_fp_surgical_complications_assistance
    - action_pasc_smt
    
## ask certification 
* ask_cer_binding_info OR cer_modify_info OR cer_special_characters OR expatriate_cer_by_app OR hk_tw_cer_by_app OR cer_by_app OR cer_business_registration OR cer_who_need OR cer_cancel OR cer_setup_market_reg_contact OR cer_not_exist OR cer_format_error OR cer_fail
    - action_pasc_smt