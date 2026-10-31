[app]
# Название твоего приложения
title = German Trainer
package.name = germantrainer
package.domain = org.germantrainer

# Какие файлы включать в APK (обязательно укажи все свои модули и CSV-базу!)
source.include_exts = py,png,jpg,kv,atlas,csv
source.include_patterns = assets/*, *.csv, *.py

# Главный файл приложения
source.file = app.py

# Версия
version = 1.0

# Требования (Kivy и Python)
requirements = python3,kivy

# Ориентация экрана (портретная для телефона)
orientation = portrait

# Разрешения (если нужны, но пока не требуются)
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1