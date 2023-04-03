import requests
re = requests.get('http://www.google.com')
print(re.status_code)