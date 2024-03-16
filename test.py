from requests import post, get, delete

# Правильный запрос
print(post('http://127.0.0.1:5000/api/v2/jobs',
           json={'team_leader_id': 3,
                 'job': 'физик-ядерщик',
                 'work_size': 52,
                 'collaborators': '1,2,4',
                 'category': '1',
                 'is_finished': True}))

# Неправильный запрос
print(post('http://127.0.0.1:5000/api/v2/jobs', json={}))

# правильный запрос
print(get('http://127.0.0.1:5000/api/v2/jobs1').json())

# Неправильный запрос
print(get('http://127.0.0.1:5000/api/v2/jobs90').json())

# правильный запрос
print(delete('http://127.0.0.1:5000/api/v2/jobs/5'))

# Неправильный запрос
print(delete('http://127.0.0.1:5000/api/v2/7'))

# Проверка корректности
print(get('http://127.0.0.1:5000/api/v2/jobs').json())


