[app]
title = Расписание
package.name = raspisanie
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv
version = 0.1
requirements = python3,kivy
orientation = portrait
# (опционально) icon = icon.png

# (android)
android.api = 33
# android.ndk = 21b   # иногда нужно фиксировать NDK; см. раздел "проблемы" ниже
# android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 1
