### Функционал
- Добавление, удаление, редактирование и просмотр категорий, подкатегорий и продуктов
- Добавление, удаление, редактирование, просмотр продуктов в корзине. Очистка корзины
- Подсчет количества товаров и суммы стоимости товаров в корзине
- Авторизация по токену
- Авторизация по токену для взаимодействия с корзиной
- Автотесты
- swagger

### Как запустить
1) Загрузим репозиторий `git clone https://github.com/sbaisarov/django-test.git`
2) Установим необходимые пакеты `pip install -r requirements.txt`
3) Перейдем в test-app `cd test-app`
4) Запустим автотесты `python manage.py test app`
5) Откроем админ панель http://127.0.0.1:8000/admin/
   Логин: foo
   Пароль: bar

6) Откроем swagger http://127.0.0.1:8000/api/swagger/
7) Для взаимодействия с корзиной запросим токен через POST запрос /api-token-auth (логин и пароль те же)
