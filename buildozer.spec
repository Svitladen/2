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

# Требования (фиксируем Python 3.11 для стабильной сборки)
requirements = python3==3.11.9,kivy

# Ориентация экрана
orientation = portrait

# Разрешения
android.permissions = INTERNET

# Стабильные версии Android SDK
android.api = 33
android.minapi = 21
android.sdk = 33
android.build_tools_version = 33.0.3
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
