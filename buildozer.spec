[app]

title = German Trainer
package.name = germantrainer
package.domain = org.germantrainer

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,csv
source.file = app.py
version = 1.0

requirements = python3,kivy

orientation = portrait
android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.sdk = 33
android.build_tools_version = 33.0.3
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
