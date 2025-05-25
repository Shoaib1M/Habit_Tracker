import requests
import datetime




username="shoaib1234"
token='123456789'

pixela_endpoint="https://pixe.la/v1/users"

graph_endpoint="https://pixe.la/v1/users/shoaib1234/graphs"

post_endpoint="https://pixe.la/v1/users/shoaib1234/graphs/graph1"

user_params={
    "token":username,
    "username":token,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

header={
    "X-USER-TOKEN":token,
}
#response = requests.post(url=pixela_endpoint,json=user_params)

#print(response.text)

graph_params={
    "id":"graph1",
    "name":"Coding Graph",
    "unit":"Hours",
    "type":"int",
    "color":"sora",

}
today=datetime.datetime.now()
print(today.strftime("%Y%m%d"))
quant=input("How many hours did you code for")

pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":quant,
}



#response=requests.post(graph_endpoint, json=graph_params,headers=header)
#print(response.text)


response=requests.post(url=post_endpoint,json=pixel_data,headers=header)
print(response.text)
