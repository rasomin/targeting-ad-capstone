# input type : dictionary
# data = {
#     'gender' : 'male',
#     'age' : 20,
# }

def parse_age(data: dict):
    return data['age']

def parse_gender(data: dict):
    return data['gender']
    
def age(num: str):
    if num == "(0 ~ 2)":
        return "10"
    elif num == "(4 ~ 6)":
        return "10"
    elif num == "(8 ~ 12)":
        return "10"
    elif num == "(15 ~ 20)":
        return "10"
    
    elif num == "(25 ~ 32)":
        return "20"
    
    elif num == "(38 ~ 43)":
        return "30"
    
    elif num == "(48 ~ 53)":
        return "40-50"
    
    else:
        return "60"
    
# def gender(s: str):
#     if s == "Male":
#         return "남"
#     else:
#         return "여"