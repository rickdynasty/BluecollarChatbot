## greet
* greet
  - utter_greet

## thank
* thanks
  - utter_thanks

## goodbye
* goodbye
  - utter_goodbye
  
## Some question from FAQ
* faq
    - respond_faq
    
## story: who are you
* whoareyou
    - utter_whoareyou
    
## story: who are you with greet
* greet
    - utter_greet
* whoareyou
    - utter_whoareyou
    
## story: what to do
* whattodo
    - utter_whattodo
    
## story: what to do with greet
* greet
    - utter_greet
* whattodo
    - utter_whattodo
    
## say no 
* deny
    - utter_deny
    
## sales form
* contact_sales
    - sales_form                   <!--运行sales_form Action-->
    - form{"name": "sales_form"}   <!--激活这个form-->
    - form{"name": null}           <!--停用这个form-->

## just sales, continue
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
* faq
    - respond_faq
    - sales_form
    - form{"name": null}
    
## explain email
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - slot{"requested_slot": "email"}
* explain
    - utter_explain_why_email
    - sales_form
    - form{"name": null}

## explain company
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - slot{"requested_slot": "company"}
* explain
    - utter_explain_why_company
    - sales_form
    - form{"name": null}
    
## explain name
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - slot{"requested_slot": "name"}
* explain
    - utter_explain_why_name
    - sales_form
    - form{"name": null}
    
## explain use_case
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - slot{"requested_slot": "use_case"}
* explain
    - utter_explain_why_use_case
    - sales_form
    - form{"name": null}

## explain budget
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - slot{"requested_slot": "budget"}
* explain
    - utter_explain_why_budget
    - sales_form
    - form{"name": null}
    
## explain job
* contact_sales
    - sales_form
    - form{"name": "sales_form"}
    - slot{"requested_slot": "job"}
* explain
    - utter_explain_why_job
    - sales_form
    - form{"name": null}
   
## out of scope
* out_of_scope
  utter_out_of_scope