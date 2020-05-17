from utils.FeignClient import post

baseurl = 'http://askbob/'

def query_by_id(json_data):
    return post(baseurl+'ask',json=json_data)

def query_by_problem_name(str:str):
    data = {'inputText':str,'precise':True}
    return post(baseurl+'ask',json=data)
