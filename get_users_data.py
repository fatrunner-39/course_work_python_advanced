import requests
from calculate_age import calculate_age
from pprint import pprint



class ApiVk:

    def __init__(self, id=None, token='6ebaec931051e22d4e358238e1b9d4e867b14c47b78563bc719b0bbdaadd35fc0a286190cf5b10faa6f8a'):
        self.id = id,
        self.token = token

    def get_params(self):
        return {
            'user_ids': self.id,
            'access_token': self.token,
            'fields': 'bdate, sex, city',
            'v': '5.131'
        }

    def get_users_data(self):
        URL = 'https://api.vk.com/method/users.get'
        res = requests.get(URL, params=self.get_params())

        data = dict()
        if 'bdate' not in res.json()['response'][0]:
            data['age'] = None
        elif len(res.json()['response'][0]['bdate'].split('.')) < 3:
            data['age'] = None
        else:
            d_birth = res.json()['response'][0]['bdate'].split('.')
            # print(d_birth)
            age = calculate_age(d_birth)
            data['age'] = age

        sex = res.json()['response'][0]['sex']
        data['sex'] = sex

        if 'city' not in res.json()['response'][0]:
            data['city'] = None
        else:
            city = res.json()['response'][0]['city']['title']
            data['city'] = city

        id = res.json()['response'][0]['id']
        data['id'] = id

        return data


if __name__ == '__main__':
    api_vk = ApiVk()
    pprint(api_vk.get_users_data())
