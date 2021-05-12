import requests, sys

#usage:
# deactivate_purple_users.py userid
# will deactivate user id passed in argument, on Purple
# can use a simple loop in shell to deactivate several users... 
# for i in $(cat user_to_deactivate_20200708); do python3 deactivate_purple_users.py $i >> logfile; done


payload = {}
headers = {
  'Authorization': 'Bearer 04c4a9747e16a9f18038ef2d26f9c32bedaa9597a1f87e6149f742b19f4',
  'Accept': 'application/json'
}

if sys.argv[1] is not None :
	#get user id as only argument
	user_id = sys.argv[1]

	url = "https://purple.api.engagement.dimelo.com/1.0/users/" + user_id + "?enabled=false"

	print(url)

	response = requests.request("PUT", url, headers=headers, data = payload)

	print(response.text.encode('utf8'))