
1. Скопируйте проект по ссылке:
   - git@github.com:Pixel2022UA/Homework_12.git

2. Откройте проект в PyCharm и установите необходимые зависимости из файла requirements.txt, используя команду 
   - pip install -r requirements.txt

3. !!База данных залита вместе с проектом, но можно создать новую(предварительно удалив старую):
   - python manage.py makemigrations
   - python manage.py migrate

5. :exclamation: __В PyCharm убедитесь, что вы находитесь в директории, где расположены файлы проекта и файл manage.py__

6. Запустите Redis в контейнере Docker используя команду: 
   - docker run -p 6379:6379 redis

8. Запустите проект, используя команду:
   - python manage.py runserver

9. Теперь вы можете открыть веб-браузер и перейти на страницы:
   - Для добавления статьи: http://127.0.0.1:8000/add-article/
   - Для редактирования статьи по id: http://127.0.0.1:8000/edit-article/   в конце ссылки указать id
   - Для вывода статьи по id: http://127.0.0.1:8000/get-article/     в конце ссылки указать id
