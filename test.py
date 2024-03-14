from requests import post, get, delete

# Правильный запрос
print(post('http://127.0.0.1:5000/api/v2',
           json={'surname': 'Userov',
                 'name': 'User',
                 'age': '30',
                 'position': 'crewmate',
                 'speciality': 'some',
                 'email': 'logi_tech__@mars.org',
                 'password': '5958',
                 'city': 'Havana',
                 'address': 'module_3'}))

# Неправильный запрос
print(post('http://127.0.0.1:5000/api/v2', json={}))

# правильный запрос
print(get('http://127.0.0.1:5000/api/v2/1').json())

# Неправильный запрос
print(get('http://127.0.0.1:5000/api/v2/90').json())

# правильный запрос
print(delete('http://127.0.0.1:5000/api/v2/4'))

# Неправильный запрос
print(delete('http://127.0.0.1:5000/api/v2/7'))

# Проверка корректности
print(get('http://127.0.0.1:5000/api/jobs').json())
