import requests
url = "https://jsonplaceholder.typicode.com/users"
apikey="123456"
headers = {'Authorization': 'Bearer ' + apikey}
r = requests.get(url, headers=headers)
r = requests.delete(url, headers=headers)


# r = requests.get(url, timeout=10)

# # print(r.status_code)
# # print(r.text)
# r = r.json()
# for i in r:
#     print(i['name'])
