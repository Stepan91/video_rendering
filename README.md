# video_rendering для Instories
### http://render4instories.pythonanywhere.com/
### Приложение позволяет загружать и редактировать видео
### Загружать видео можно двумя способами:
- через GUI с главной страницы по кнопке "Добавить видео";
- через API по эндпоинту http://127.0.0.1:8000/api/ (в теле POST-запроса необходимо указать/загрузить: description (описание/название), background (фоновая картинка), video (само видео))
### Рендеринг видео осущестлвяется через API по эндпоинту:
- http://127.0.0.1:8000/api/render/ (в теле POST-запроса необходимо указать text и video (id первоначального видео);

По эндпоинту http://127.0.0.1:8000/api/render/1/ можно проверить, что объект рендеринга создан.

БД заполнена тестовыми данными. Суперюзер - admin, пароль - admin.

### С помощью Dockerfile можно создать контейнер с проектом, что позволяет запустить проект "из коробки"
- Для создания образа необходимо выполнить команду: `docker build -t rendervideo .`
- Для запуска контейнера необходимо выполнить команду: `docker run -it -p 8000:8000 yamdb`
- После этого с помощью браузера зайдите на `localhost:8000` - приложение запущено и работает.

Стек: Python, Django, Django Rest Framework, Moviepy.
