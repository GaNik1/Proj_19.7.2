

import json

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

class PetFriends:
    '''Библиотека содержит API запросы к приложению PetFriens'''
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

# Этот метод позволяет получить ключ API, который следует использовать для других методов API.
    def get_api_key(self, email: str, passwd: str) -> json:
        '''Метод делает запрос к API сервера и возвращает статус запроса и результат в формате
        JSON с уникальным ключем пользователя, найденного по указанным email и паролем'''

        headers = {
            'email': email,
            'password': passwd,
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

# Этот метод позволяет получить список питомцев.
    def get_list_of_pets(self, auth_key: json, filter: str) -> json:
        '''Метод делает get запрос к API сервера с секретным ключом в headers и
        пустым  значением в filter и возвращает код статуса запроса и список
        всех питомцев в формате JSON либо в виде строки'''
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url + 'api/pets', headers=headers, params=filter)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

# Этот метод позволяет добавить информацию о новом питомце (с фото).
    def add_new_pets(self, auth_key: json, name: str, animal_type: str, age: str, pet_photo: str) -> json:
        '''Метод делает post запрос к API сервера, добавляет данные data на сайт PetFriends и
        возвращает код статуса запроса результат в формате JSON с информацией о добавленном животном. '''
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })

        headers = {
            'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + '/api/pets', headers=headers, data=data)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

# Этот метод позволяет удалить информацию о питомце из базы данных.
    def delete_pets(self, auth_key: json, pet_id: str) -> json:
        '''Метод делает delete запрос к API сервера и удоляет питомца по его ID,и возвращает
        статус запроса и результат в формате JSON с текстом уведомления о успешном удалении'''
        headers = {'auth_key': auth_key['key']}

        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

# Этот метод позволяет обновить информацию о питомце.
    def update_pet_info(self, auth_key: json, pet_id: str, name: str, animal_type: str, age: str) ->json:
        '''Метод отправляет запрос на сервер о обновлении данных питомуа по указанному ID и
        возвращает статус запроса и result в формате JSON с обновлённыи данными питомца'''
        headers = {
            'auth_key': auth_key['key']}
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }

        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

# Этот метод позволяет добавить информацию о новом питомце (без фото).
    def add_new_pet_without_photo(self, auth_key: json, name: str, animal_type: str, age: str) ->json:
        '''Метод делает post запрос к API сервера, добавляет новые данные из data на сайт
        и возвращает код статуса запроса и результат в формате json с информацией о животном.'''
        headers = {
            'auth_key': auth_key['key'],
        }
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }

        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

# Этот метод позволяет добавить информацию о новом питомце (его фото).
    def add_photo_of_pet(self, auth_key: json, pet_id: str, pet_photo: str) ->json:
        '''Метод делает post запрос к API сервера и добавляет новое фото указанного
        pet_id питомца. Возвращает код статуса запроса и результат в формате json с информацией о животном.'''
        data = MultipartEncoder(
            fields={
                'pet_id' : ('id'),
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg'),
                 })

        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result
