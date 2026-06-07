# Sprint_9 - Тестирование UI для Продуктового помощника

Автотесты для UI https://foodgram-frontend-1.foodgram.education-services.ru/

## Описание проекта

Проект содержит тесты веб приложения Продуктового помощника:

- Созадние аккаунта
- Авторизация
- Создание рецепта

## Технологии

- **Python** 3.14.2
- **Pytest** 9.0.2
- **Allure** 2.38.1
- **Page Object Pattern**
- **Selenium** 4.41.0

#### Запуск всех тестов
pytest tests/ -v

#### Запуск конкретного теста
- pytest tests/test_auth.py -v
- pytest tests/test_create_account.py -v
- pytest tests/create_receipt.py -v

#### Открытие отчёта
allure open target/allure-report


 

 