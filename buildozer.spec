[app]
title = Расписание
package.name = raspisanie
package.domain = org.example
source.dir = .
source.include_exts = py,kv,png,jpg
version = 0.1
requirements = python3,kivy
orientation = portrait
icon = icon.png
# в некоторых случаях нужно явно указать android.api и ndk:
android.api = 33
# android.ndk = 21b

[buildozer]
log_level = 2
warn_on_root = 1
