import requests

res = requests.get('https://api.cloudamqp.com/')

print(res)

if res:
    print('Response OK')
else:
    print('Response Failed')

print(res.status_code)

print(res.headers)
print(res.text)

API_KEY = '91108812-7765-4a17-8541-244739155c47'

url = 'https://api.cloudamqp.com/api/integrations/metrics'

params = dict(key=API_KEY, text='Name', lang='en')

res = requests.get(url, params=params)

json = res.json()
print(json)

print(res.status_code)