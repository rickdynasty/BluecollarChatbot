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

## pasc story1
* declare_wjziszdjgzzsblzncxn OR declare_fsznljxzzsbjkdj OR declare_grjkzzsb OR declare_zzsbdjkewmznlcx OR declare_zzsbjkmxxtclzmxg OR driver_license_jdcjszxxbhhz OR driver_license_jdcjszyxqmhz OR driver_license_jdcjszccsl OR driver_license_dzjsz OR driver_license_bljsz OR driver_license_hljsz OR driver_license_zmcxjszdyxq OR epidemic_yyqbnfxwgbztqbydyyes_omit31 OR face_mask_yhmywxhkycyzcyykzhdm OR face_mask_qykzyyrhqrsfzq
    - action_pasc_smt

## pasc story2
* face_mask_yydkzjdznlck OR face_mask_qyyykzzqhmyzgdsjnlq_omit5 OR face_mask_qyyykzzqhrhlq OR face_mask_yykzmyzqdqyhxyzxyydjm OR face_mask_yykzxysmtj OR face_mask_smznljxkzyy OR face_mask_znlkkzsfzq OR face_mask_qysmshksyyslkzsfxdxd OR face_mask_yykzzcmzqxcxyjxyym OR face_mask_smmczqdkzydsg OR face_mask_qyznlyyslkz OR face_mask_smkzzqlzmlq OR hukou_wsmhjxxmygx OR hukou_bysrh OR hukou_bshrhjpoznsq
    - action_pasc_smt

## pasc story3
* hukou_wcnzntkfmhjqr OR hukou_zsbgzryhjqr OR hukou_fbshjjmsfzbl OR hukou_xshkqc OR hukou_czqzhkqc OR hukou_jfrh OR hukou_fqtkhjqr OR hukou_sxnyjbbsqrzdzzyxlqdxskz_omit14 OR id_card_blsfz OR id_card_slblhljmsfz OR id_card_bllssfz OR id_card_hlsfz OR jhsy_dpxqjhsyqkzmzsz OR jhsy_ytqjhsyqkzmzsz OR jhsy_ftqjhsyqkzmzsz
    - action_pasc_smt

## pasc story4
* jhsy_baqjhsyqkzmzsz OR jjz_bljzz OR jjz_blszjzzyydzdsmhzkym OR jjz_wsblszjzzsmzxtxhzmt OR jjz_szjzzblydj OR jubao_blxxjb OR pass_blwlgatxzgryqz OR pass_blgatxzqz OR pass_twjmdltxzbnytbzrz OR pass_wdcsqtxz OR pension_cxjmylbxgxjs OR qy_grdzqybgdj OR qy_pmqyjfgscspmywbghz OR qy_hhqyzcdj OR qy_lhqyqqjqyfgba
    - action_pasc_smt

## pasc story5
* qy_nzqybgdj OR qy_hhqybgdj OR qy_nzqyzcdj OR qy_pmqyjfgssqqdcspmywzzdhz OR qy_grdzqyzcdj OR qy_ftqyqqjqyfgba OR qy_2020n2yfsbfytjhbhyxqydzccbzt OR qy_wstzhhqybgdj OR qy_pmqyfgssqqdcspmywxkdhz OR qy_ytqyqqjqyfgba OR qy_wzqyzcdj OR rzpz_lsrzpz OR social_security_szylbxydcbrzy_omit17 OR social_security_bjrsbk OR social_security_blsbk
    - action_pasc_smt

## pasc story6
* social_security_jbylbxgrzhjss_omit30 OR social_security_szssbjlxdhhdz OR social_security_hbsbk OR traffic_bjm12fjsrxxks OR un_xytjndbgdssztbknx OR un_dtswzl OR un_ddytzxyxkzhf OR un_znlcxxqqzbl OR un_jwdzdt OR un_mzwhhdly OR un_sjxxcx OR un_baqgjdmcjlxfs OR un_yhcxjsq OR un_spcykh OR un_sbkmmxgyzz
    - action_pasc_smt

## pasc story7
* un_qwsgcl OR un_mzwhhd OR un_sbcbzm OR un_gsccmdjgcx OR un_swbx OR un_bdcdjyy OR un_kzyzqznlqjxlq OR un_yhzgzc OR un_bdccxjfczm OR un_sxnyjzfclh OR un_szzx OR un_jzzqzxq OR un_lscjzm OR un_jdclpsq OR un_jtwfcxrkznl
    - action_pasc_smt

## pasc story8
* un_kzyydjcghqrmdxsclzmb OR un_swjt OR un_qyxycx OR un_jzzzmblgsxbllzfjy OR un_sfjn OR un_sjllcz OR un_mzwhhdyd OR un_wczmxxdcx OR un_ztkyqcpcx OR un_qyaqglzskyxxtbyhmhmmssm OR un_sbkgsyjg OR un_baqwcnrjzbhzx OR un_ylcsba OR un_jsrxxdcx OR un_mybzwpxsxkbg
    - action_pasc_smt

## pasc story9
* un_xxgzbdyf OR un_rhcxgrgjzm OR un_kzyyzqhdlqqxsdj OR un_rqjgcx OR un_cjsyjtsl OR un_jszzr OR un_dwbzjdcx OR un_yjnc OR un_sbkzx OR un_zgsybxylfyhz OR un_szsddyyfrmz OR un_hlxsz OR un_zcqscjyxkzhfzqscjyxkzhf OR un_szjy OR un_fshlsxhtqrhbl
    - action_pasc_smt

## pasc story10
* un_sbhzmcx OR un_gjjtqdjdz OR un_jzzxqxyhkm OR un_swhdjl OR un_yytx OR un_mzwhhdty OR un_gjjwsmtqbl OR un_rhzxhztsyiszzh OR un_sjhsbdyzmzmb OR un_jszgcx OR un_sgbs OR un_kzzqldmywlxxhwsdh OR un_gatjmdzzdj OR un_zyjyy OR un_gjjzhmx
    - action_pasc_smt

## pasc story11
* un_rgfw OR un_hjqr OR un_yygh OR un_rhsqszcllm OR un_yszcx OR un_ncpjgxq OR un_gjrytb OR un_bzxrcx OR un_csdj OR un_xzhszxyglm OR un_ccm OR un_ytgxxcx OR un_kzyysddxqrmmyz24xsnfqrlqzmb OR un_jkmznlsc OR un_clnj
    - action_pasc_smt

## pasc story12
* un_qzzlhdba OR un_ytc OR un_jdbfw OR un_sznbnzxqdgjjzzblfwxy OR un_hflp OR un_jszxgywfwbky OR un_ypzs OR un_yhjjqgl OR un_mybzwpxsxkhz OR un_sbkslbkhkzxgsyjgxgmmzzmm OR un_jyfw OR un_ldxx OR un_szdgjjdkkyyyljjfm OR un_gjjzhyecx OR un_swsyylfyhz
    - action_pasc_smt

## pasc story13
* un_kzyytclxxrgrdhdzdkygzm OR un_hbdt OR un_wgsb OR un_ykcz OR un_sztt OR un_hbjfsryxyglm OR un_jfwdcx OR un_cslkcx OR un_swcnrjzbhzx OR un_jcmtgp OR un_zytjpysyisz OR un_zxzj OR un_hjzy OR un_znlckzjyyydbs OR un_hbcx
    - action_pasc_smt

## pasc story14
* un_cxtx OR un_zmqxbsyy OR un_gslk OR un_grcjjjsqzlzb OR un_wycyszxbbbhfzxzfjy OR un_rcyjyjbysjs OR un_dwcjjjsqzlzb OR un_2020ncjqjnjtbxx OR un_zzrcyj OR un_yjbj OR un_zflyb OR un_ghxsmzcw OR un_dmsyy OR un_fjyyzs OR un_dfjn
    - action_pasc_smt

## pasc story15
* un_jsrxxdsq OR un_yqpy OR un_jzzhlbl OR un_xmbg OR un_hkhyfw OR un_rmyjjyzj OR un_2020nszgqdychsdz OR un_dtlxt OR un_jtwfcx OR un_fjqcwx OR un_zqlqcghrhcxwldhhlqkd OR un_dzhzbgbazxtzsznldy OR un_jszcxzfjy OR un_kzyyzqytxm OR un_jzdj
    - action_pasc_smt

## pasc story16
* un_ksbm OR un_kyxxtb OR un_zzbgbdskd OR un_wczmsq OR un_rsdj OR un_iszgzhzn OR un_yqzrdj OR un_qyaqglzsddlmmbjdlrhzh OR un_ztkygp OR un_gjjxstqtjynx OR un_sbcx OR un_hfcz OR un_ftqfwzldjba OR un_2020szzxxxxx OR un_szslgqjzglzlxfs
    - action_pasc_smt

## pasc story17
* un_jszns OR un_tqcx OR un_qysdszs OR un_szdlmmwj OR un_qrpcsdgh OR un_kzyyzqlqcghrhcxwldhhlqkd OR un_qysqqdcspmywxkdhz OR un_zmqxgh OR un_kzyysmshkssfxyqg OR un_sbjtzhbg OR un_tfyb OR un_jtwfclzq OR un_rcyjjdcx OR un_ygacp OR un_dzzzytynx
    - action_pasc_smt

## pasc story18
* un_zfbtsq OR un_cszzmbl OR un_ssztnb OR un_ksfw OR un_gjjzzxyznlqd OR un_blpthz OR un_spjyxkzhf OR un_gzfrzsq OR un_rqfjn OR un_qyxzcf OR un_wlyyczqcysznsqz OR un_dazrksdh OR un_xyjbsc OR un_yjzs OR un_pcscx
    - action_pasc_smt

## pasc story19
* un_yjjzy OR un_szszftzxmys OR un_sxnyjzggzlfwlh OR un_mzwhhdyc OR un_yqqjkcjsznlsq OR un_mzwhhdys OR un_mzwhhdzl OR un_gjssjzlxxxcyxmys OR un_hcpw OR un_rcydt OR un_qyfgbbyzy OR un_wxccx OR un_flzxwd OR verified_smrzsrlsbwftggzmb OR verified_gatjmrhziszjxsmrz
    - action_pasc_smt