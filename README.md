# Sprint_9 — UI-тесты для Foodgram

UI-автотесты для сервиса [Продуктовый помощник (Foodgram)](https://foodgram-frontend-1.foodgram.education-services.ru/).  
Покрыты сценарии создания аккаунта, авторизации и создания рецепта.

## Список реализованных тестов

### 👤 Создание аккаунта (`TestSignup`)

| Тест | Описание |
|:---|:---|
| `test_signup_redirects_to_signin` | После регистрации происходит переход на страницу авторизации. |
| `test_signup_shows_signin_form` | После регистрации отображается форма авторизации. |

### 🔑 Авторизация (`TestSignin`)

| Тест | Описание |
|:---|:---|
| `test_signin_redirects_to_recipes` | После авторизации происходит переход на главную страницу с рецептами. |
| `test_signin_shows_logout_button` | После авторизации отображается кнопка «Выход». |

### 🍽️ Создание рецепта (`TestCreateRecipe`)

| Тест | Описание |
|:---|:---|
| `test_created_recipe_card_is_visible` | После создания рецепта отображается его карточка. |
| `test_created_recipe_has_correct_name` | Название созданного рецепта совпадает с введённым. |

---

## 🛠 Технические особенности

- **Page Object Model** — каждая страница описана отдельным классом в пакете `pages/`. Общие методы вынесены в `BasePage`.
- **Локаторы** — вынесены в отдельный пакет `locators/`, по файлу на каждую страницу.
- **Тестовые данные** — хранятся в `data.py` (`URLS`, `RecipeData`) и `helpers.py` (генерация уникальных пользователей).
- **Фикстуры** — `registered_user` создаёт уникального пользователя через UI перед тестом; `logged_in_driver` возвращает уже залогиненный браузер.
- **Allure-отчёты** — каждый тест и класс размечен `@allure.feature`, `@allure.title`, шаги в Page Object — `@allure.step`.
- **Загрузка файлов** — реализована через `send_keys()` на `input[type=file]`, путь формируется через `pathlib.Path`.
- **Docker + Selenoid** — тесты запускаются в `selenium/standalone-chrome` контейнере через `webdriver.Remote`.
- **CI/CD** — GitHub Actions запускает тесты при каждом пуше в `develop` и `main`.

---

## 🚀 Запуск проекта

### Установка зависимостей
```bash
pip install -r requirements.txt
```

### Локальный запуск
```bash
pytest -v
```

### Запуск с Allure-отчётом
```bash
make test
make report
```

### Запуск в Docker (с selenium/standalone-chrome)
```bash
docker compose up --build
```

---

## 📁 Структура проекта

```
Sprint_9/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions пайплайн
├── assets/
│   └── test_image.png      # Тестовое изображение для загрузки
├── locators/
│   ├── main_page_locators.py
│   ├── recipe_page_locators.py
│   ├── signin_page_locators.py
│   └── signup_page_locators.py
├── pages/
│   ├── base_page.py
│   ├── main_page.py
│   ├── recipe_page.py
│   ├── signin_page.py
│   └── signup_page.py
├── tests/
│   ├── test_recipe.py
│   ├── test_signin.py
│   └── test_signup.py
├── browser.json            # Конфиг браузеров для Selenoid
├── conftest.py
├── data.py
├── docker-compose.yml
├── Dockerfile
├── helpers.py
├── Makefile
├── pytest.ini
└── requirements.txt
```