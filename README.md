# ![AutoBuildRepo](https://img.shields.io/badge/Auto%20Build-GitHub%20Release-blue?style=for-the-badge&logo=github)

![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/-GitHub-181717?logo=github)
![Windows](https://img.shields.io/badge/-Windows-0078D6?logo=windows&logoColor=white)
![Linux](https://img.shields.io/badge/-Linux-FCC624?logo=linux&logoColor=black)
![Usage](https://img.shields.io/badge/Usage-Automated%20Releases-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

## Содержание

* [Описание](#описание)
* [Функции](#функции)
* [Требования](#требования)
* [Установка](#установка)
* [Конфигурация](#конфигурация)
* [Настройки расписания](#настройки-расписания)
* [Запуск](#запуск)
* [Важные примечания](#важные-примечания)
* [Лицензия](#лицензия)

## Описание

Мощный Python-скрипт, автоматизирующий создание релизов на GitHub путем генерации ежедневных архивов содержимого вашего репозитория. Идеально подходит для проектов, требующих регулярных сборок или резервных копий.

## Функции

* 🔄 **Автоматическое архивирование репозитория** - Создает сжатые архивы вашего репозитория
* 🚀 **Генерация релизов на GitHub** - Автоматически создает релизы на GitHub
* 📦 **Загрузка ресурсов** - Прикрепляет архивные файлы к каждому релизу
* 💻 **Кроссплатформенность** - Работает как на Windows, так и на Linux
* ⏱️ **Настраиваемое расписание** - Настройте собственное время выпуска релизов
* 🔒 **Безопасная аутентификация** - Использует персональные токены доступа GitHub для безопасного доступа к API

## Требования

* Python 3.8 или выше
* Установленный и настроенный Git
* Персональный токен доступа GitHub с соответствующими разрешениями
* Интернет-соединение для доступа к API GitHub

## Установка

<details>
<summary>

### Windows
</summary>

1. **Клонировать репозиторий**

   ```bash
   git clone https://github.com/themaster1970sf/AutoBuildRepo.git
   cd AutoBuildRepo
   ```

2. **Установить зависимости**

   ```powershell
   pip install -r requirements.txt
   ```

3. **Запустить скрипт**

   ```powershell
   python app.py
   ```
</details>

<details>
<summary>

### Linux
</summary>

1. **Клонировать репозиторий**

   ```bash
   git clone https://github.com/themaster1970sf/AutoBuildRepo.git
   cd AutoBuildRepo
   ```

2. **Создать и активировать виртуальное окружение**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Установить зависимости**

   ```bash
   pip install -r requirements.txt
   ```

4. **Запустить скрипт**

   ```bash
   python3 app.py
   ```
</details>

## Конфигурация

1. **Получить персональный токен доступа GitHub**
   
   Создайте токен со следующими разрешениями:
   - `repo` (Полный контроль над приватными репозиториями)
   - `workflow` (Обновление рабочих процессов GitHub Action)

2. **Настроить скрипт**

   Отредактируйте функцию `daily_release()` в файле `app.py`:

   ```python
   repo = {
       "path": r"/путь/к/сборке", 
       "git_config": {
           "username": "ваш_логин_github",
           "repo": "ваш_репозиторий",
           "token": "ваш_токен_github"
       }
   }
   ```

## Настройки расписания

По умолчанию скрипт запускается ежедневно в 11:23. Чтобы изменить расписание, измените функцию `main()`:

```python
schedule.every().day.at("ЧАС:МИНУТА").do(daily_release)
```

Доступные варианты расписания:
- `schedule.every().day.at("ЧЧ:ММ")` - Запуск ежедневно в указанное время
- `schedule.every().hour` - Запуск каждый час
- `schedule.every().monday` - Запуск каждый понедельник
- `schedule.every(10).minutes` - Запуск каждые 10 минут

## Запуск

Чтобы запустить автоматический процесс выпуска релизов:

```bash
python app.py
```

Скрипт продолжит работать в фоновом режиме в соответствии с установленным расписанием.

## Важные примечания

⚠️ **Соображения безопасности**

- Никогда не фиксируйте токен GitHub непосредственно в коде
- Рассмотрите возможность использования переменных окружения для хранения конфиденциальной информации
- Убедитесь, что ваш репозиторий имеет достаточно места для хранения регулярных архивов
- Проверьте, есть ли у вас необходимые разрешения для целевого репозитория

⚠️ **Соображения производительности**

- Для больших репозиториев архивирование может занять значительное время
- Следите за ограничениями скорости API GitHub
- Учитывайте использование пропускной способности сети для больших загрузок

## Лицензия

[Лицензия MIT](https://git.plazmocraft.ru/themaster1970sf/AutoBuildRepo/src/branch/main/LICENSE)

---

<p align="center">
  Сделано с ❤️ от <a href="https://git.plazmocraft.ru/themaster1970sf/">themaster1970sf</a>
</p>
