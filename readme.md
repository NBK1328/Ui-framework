Ui-framework
Это легковесный фреймворк для автоматизированного UI-тестирования веб-приложений с использованием Python, Selenium и Pytest. Проект организован по принципам Page Object Model (POM), обеспечивая читаемость, масштабируемость и повторное использование кода.

📦 Стек технологий

Python 3
Selenium WebDriver
Pytest
Pytest Fixtures
Page Object Model (POM)

📁 Структура проекта

Ui-framework/
├── pages/                   # Page Object классы
│   ├── __init__.py
│   └── ...                  # (файлы с реализациями страниц)
├── tests/                   # Тестовые сценарии
│   ├── test_login_page.py
│   ├── test_main_page.py
│   ├── test_product_page.py
│   └── test_negative_product_page.py
├── conftest.py              # Общие фикстуры для Pytest
├── requirements.txt         # Зависимости проекта
├── pytest.ini               # Конфигурация Pytest
└── .gitignore

🚀 Установка и запуск
1. Клонирование репозитория
git clone https://github.com/NBK1328/Ui-framework.git
cd Ui-framework
2. Создание виртуального окружения (опционально)
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
3. Установка зависимостей
pip install -r requirements.txt
4. Запуск тестов
pytest

🧪 Примеры тестов
Проект содержит следующие тестовые файлы:

test_login_page.py — тесты для страницы входа

test_main_page.py — тесты для главной страницы

test_product_page.py — позитивные сценарии для страницы продукта

test_negative_product_page.py — негативные сценарии для страницы продукта

Каждый тест использует соответствующие Page Object классы из директории pages/, обеспечивая модульность и читаемость кода.

⚙️ Конфигурация
conftest.py содержит общие фикстуры, такие как инициализация драйвера браузера.
pytest.ini используется для настройки Pytest, включая параметры запуска и отчётности.
