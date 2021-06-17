import requests

# r = requests.get('https://api.github.com/events')
r = requests.post('https://httpbin.org/post', data = {'name':'afeeq','duck': False})
print(r)

body = r.content
print(body)