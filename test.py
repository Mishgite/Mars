from requests import post, get, delete, put

# Правильный запрос
print(get('http://127.0.0.1:5000/api/users/4').json())