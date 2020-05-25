from utils.FeignClient import get,post,delete,put


baseurl = 'http://ibrain/'

def query_by_id(json_data):
    return post(baseurl+'askbob/ask',json=json_data)

def query_by_problem_name(str:str):
    data = {'inputText':str,'precise':True}
    return post(baseurl+'askbob/ask',json=data)
