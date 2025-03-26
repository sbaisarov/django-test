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
3) Перейдем в папку test-app и выполним миграции:
  `python manage.py makemigrations`
  `python manage.py migrate`
4) Загрузим json `python manage.py loaddata test_data`
5) Запустим автотесты `python manage.py test app`
6) Создадим пользователя 
