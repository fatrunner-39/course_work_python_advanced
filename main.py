from random import randrange
from get_users_data import ApiVk
from find_peoples import VkFinder
from get_user_photos import top_three_photos
from create_database import get_user_id, get_result, get_photo, get_result_photo, get_all_users, \
    get_user_result, get_all_domains, get_exist_pairs

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

import random

token = '6ebaec931051e22d4e358238e1b9d4e867b14c47b78563bc719b0bbdaadd35fc0a286190cf5b10faa6f8a'

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': randrange(10 ** 7),})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            # Получаем id пользователя
            request = event.text
            if (str(request),) not in get_all_users():
                get_user_id(request)

            api_vk = ApiVk(str(request))
            finders_data = api_vk.get_users_data()
            # Уточняем данные пользователя ,если их не хватает
            for key, value in finders_data.items():
                if key == 'age' and value == None:
                    if finders_data['age'] == None:
                        write_msg(event.user_id, "Укажите ваш возраст")
                        for event in longpoll.listen():
                            if event.type == VkEventType.MESSAGE_NEW:
                                if event.to_me:
                                    age = event.text
                                    finders_data['age'] = age
                                    break
                if key == 'city' and value == None:
                    if finders_data['city'] == None:
                        write_msg(event.user_id, "Укажите ваш город")
                        for event in longpoll.listen():
                            if event.type == VkEventType.MESSAGE_NEW:
                                if event.to_me:
                                    city = event.text
                                    finders_data['city'] = city
                                    break

            vkfinder = VkFinder(finders_data['city'], finders_data['sex'], finders_data['age'],
                                    finders_data['age'])
            congruence = vkfinder.get_users()
            single = random.choice(congruence)

            link = single[
                'domain']  # Получаем ссылку на найденного пользователя
            # Проверям была ли такая пара
            while (request, link) in get_exist_pairs():
                single = random.choice(congruence)
                link = single['domain']

            # Проверяем есть ли найденный пользователь в базе данных
            if (link,) in get_all_domains():
                (get_user_result(request, link))
                write_msg(event.user_id, link)
                for photo in top_three_photos(str(single['id'])):
                    ph = photo['sizes'][-1]['url']  # Получаем фото
                    get_result_photo(link, ph)
                    write_msg(event.user_id, ph)

            else:
                get_result(link)
                get_user_result(request, link)
                write_msg(event.user_id, link)
                for photo in top_three_photos(str(single['id'])):
                    ph = photo['sizes'][-1]['url']  # Получаем фото
                    get_photo(ph)
                    get_result_photo(link, ph)
                    write_msg(event.user_id, ph)

            print("Поиск завершен")
