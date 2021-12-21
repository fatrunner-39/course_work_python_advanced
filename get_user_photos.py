import requests
import json
from pprint import pprint
import os
from settings.settings import USERS_TOKEN


TOKEN = USERS_TOKEN

class UserVk:
    def __init__(self, id=None,
                 token=USERS_TOKEN,
                 offset=0):
        self.id = id,
        self.token = token,
        self.offset = offset

    def get_params(self):
        return {
            'user_id': self.id,
            'access_token': self.token,
            'v': '5.131',
            'album_id': 'profile',
            'extended': '1',
        }

    def get_profile_photos(self):
        URL = 'https://api.vk.com/method/photos.get'
        res = requests.get(URL, params=self.get_params())
        photos = res.json()#['response']['items']
        return photos

def top_three_photos(id, token=TOKEN, offset=0):
    all_photos = []
    while True:
        api_vk = UserVk(id, token, offset)
        photos = api_vk.get_profile_photos()
        # pprint(photos)
        all_photos += photos['response']['items']
        if len(photos) < 200:
            break
        offset += 200

    top_three = sorted(all_photos, key=lambda k: k['likes']['count'], reverse=True)

    return top_three[:3]

if __name__ == '__main__':
    # for photo in top_three_photos():
    #     print(photo['sizes'][-1]['url'])
    pprint(top_three_photos('62486308'))
    # user_vk = UserVk('62486308')
    # pprint(user_vk.get_profile_photos())
