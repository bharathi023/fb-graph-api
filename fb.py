import requests
import facebook
token = ''#you facebook access token
graph = facebook.GraphAPI(access_token=token,version='2.5')#here we are connecting to our account with access token using fb graph api
user = graph.get_object('me',fields='name,id,email,education,birthday,friends')
print(user)
