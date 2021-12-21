import requests
from get_users_data import ApiVk
from pprint import pprint
from settings.settings import USERS_TOKEN


TOKEN = USERS_TOKEN



class VkFinder:

    def __init__(self,
                 hometown, sex, age_from, age_to,
                 token=USERS_TOKEN):
        self.token = token,
        self.hometown = hometown,
        if sex == 1:
            self.sex = 2
        elif sex == 2:
            self.sex = 1,
        # Устанавливаем семейное положение "не женат"/"не замужем"
        self.status = 1,
        self.age_from = age_from,
        self.age_to = age_to

    def get_params(self):
        return {
            'access_token': self.token,
            'count': 1000,
            'fields': 'id, domain, is_closed',
            'hometown': self.hometown,
            'sex': self.sex,
            'status': self.status,
            'age_from': self.age_from,
            'age_to': self.age_to,
            'v': '5.131'
        }

    def get_users(self):
        URL = 'https://api.vk.com/method/users.search'
        res = requests.get(URL, params=self.get_params())
        users_info = []
        for user in res.json()['response']['items']:
            user_ids = dict()
            if user['is_closed'] == False: # Проверка на закрытый аккаунт
                user_ids['id'] = user['id']
                user_ids['domain'] = 'https://vk.com/' + user['domain']
                users_info.append(user_ids)
        return users_info
        # return  res.json()['response']['items']

if __name__ == '__main__':
    # api_vk = ApiVk('')
    api_vk = ApiVk('')
    # api_vk = ApiVk("")
    data = api_vk.get_users_data()
    vkfinder = VkFinder(data['city'], data['sex'], 32, 32)
    pprint(vkfinder.get_users())
