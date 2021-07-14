import requests

params = {
    'name' : 'Cola',
    'description' : 'Awful',
}
# r = requests.post('http://127.0.0.1:5000/drinks', params=params)
r2 = requests.get('http://127.0.0.1:5000/drinks')
r = requests.delete('http://127.0.0.1:5000/drinks/2')


print(r2)
print(r2.json())
# print(r)
# print(r.json())
