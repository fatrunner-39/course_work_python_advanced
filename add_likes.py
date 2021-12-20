import requests
from pprint import pprint

TOKEN = '7aed241be8d2233d88fe190f6ac710a5ba3574ea91e9300ff2b5397c63b7a0c69ce81bca1e718c1740891'

class Like:

    def __init__(self, id, token=TOKEN):
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
