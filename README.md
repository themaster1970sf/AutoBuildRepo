# Auto Build GitHub Release Automation

## 📦 Описание проекта

Скрипт автоматизирует создание релизов в GitHub с ежедневной архивацией содержимого репозитория.

## 🚀 Функциональность

- Автоматическое создание архива репозитория
- Генерация релиза в GitHub
- Загрузка архива как asset релиза
- Поддержка Windows и Linux
- Настраиваемое расписание

## 🛠 Требования

- Python 3.8+
- Git
- Личный токен GitHub

## 📋 Установка

### Windows

1. Клонировать репозиторий:
```bash
git clone https://github.com/themaster1970sf/AutoBuildRepo.git
cd auto-build-script
```

2. Установить зависимости:
```powershell
pip install -r requirements.txt
```

3. Запуск:
```powershell
python app.py
```

### Linux

1. Клонировать репозиторий:
```bash
git clone https://github.com/themaster1970sf/AutoBuildRepo.git
cd auto-build-script
```

2. Создать виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Установить зависимости:
```bash
pip install -r requirements.txt
```

4. Запуск:
```powershell
python3 app.py
```

## 🔧 Настройка

1. Получить Personal Access Token в GitHub
2. Отредактировать `daily_release()`:
```python
repo = {
    "path": r"/path/to/build", 
    "git_config": {
        "username": "your_github_username",
        "repo": "your_repository",
        "token": "your_github_token"
    }
}
```

## 🕒 Расписание

По умолчанию скрипт запускается ежедневно в 11:23. Изменить время в функции `main()`:
```python
schedule.every().day.at("HOUR:MINUTE").do(daily_release)
```

## 🐍 Запуск

```bash
python app.py
```

## ⚠️ Важно

- Храните токен в секрете
- Проверьте права доступа к репозиторию
- Убедитесь в корректности путей

## 📄 Лицензия

[MIT License](https://github.com/themaster1970sf/AutoBuildRepo/blob/main/LICENSE)
