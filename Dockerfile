FROM python:3.13-slim

WORKDIR /app

# Копируем зависимости и устанавливаем
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Запуск тестов по умолчанию
CMD ["pytest", "-v", "--alluredir=allure-results"]