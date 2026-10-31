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

# Ориентация экрана
orientation = portrait

# Разрешения
android.permissions = INTERNET

# Фиксированные стабильные версии Android SDK (предотвращают ошибку с лицензией 37)
android.api = 33
android.minapi = 21
android.sdk = 33
android.build_tools_version = 33.0.3
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
