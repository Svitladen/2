[app]

# Название твоего приложения
title = German Trainer
package.name = germantrainer
package.domain = org.germantrainer

# Путь к исходному коду приложения (текущая папка)
source.dir = .

# Какие файлы включать в APK
source.include_exts = py,png,jpg,kv,atlas,csv

# Главный файл приложения
source.file = app.py

# Версия
version = 1.0

# Требования (Kivy и Python)
requirements = python3,kivy

# Ориентация экрана (портретная для телефона)
orientation = portrait

# Разрешения
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
