### Установка приложения Vkinder 
1. git clone https://github.com/fatrunner-39/course_work_python_advanced.git 
2. cd course_work_python_advanced 
3. python venv -m env  
4. source env/bin/activate (for windows env\Scripts\activate)
5. pip install -r requirements.txt

### Для создания токена для бота нужно
6. Создать группу в VK
7. Зайти в Управление -> Работа с API. Создать ключ
![image](https://user-images.githubusercontent.com/12861849/114929451-7c907380-9e3c-11eb-8a1a-44597b634a5c.png)
8. Включить возможность писать сообщения в группу. Управление -> Сообщения -> Сообщения 
   сообщества: включить.
9. Настройки бота. Возможности бота: Включены
![image](https://user-images.githubusercontent.com/12861849/114929568-a0ec5000-9e3c-11eb-8ea4-cafa0dc56b59.png)
   
10. Создать токен для пользователя
11. Cоздать .env файл в пакете setttings
    * Скопировать код, приведенный ниже и дополнить его полученными токенами
    ```python
    # Введите ключ доступа сообщества VK
    GROUPS_TOKEN = ''
    
    # Введите ключ доступа пользователя VK
    USERS_TOKEN = ''
    
    # Введите данные для работы с базой данных PostgreSQL
    HOST = 'localhost'
    PORT = 5432
    NAME = 'vkinder'
    USER_ = 'vkinder'
    PASSWORD = 1234
    ``` 
12. Запустить файл main.py