import os
import instaloader
import customtkinter as ctk

def get_default_download_path():
    if os.name == 'nt':
        return os.path.join(os.environ['USERPROFILE'], 'Downloads')
    else:
        return os.path.join(os.path.expanduser('~'), 'Downloads')

def download_instagram_profile(username, result_label, progress_bar):
    try:
        loader = instaloader.Instaloader()
        save_dir = get_default_download_path()
        os.makedirs(save_dir, exist_ok=True)
        os.chdir(save_dir)
        progress_bar.set(0.5)
        progress_bar.update()
        loader.download_profile(username, profile_pic_only=True)
        result_label.configure(text=f"Profil pengguna '{username}' berhasil diunduh ke '{save_dir}'")
        progress_bar.set(1)
        progress_bar.update()
    except Exception as e:
        result_label.configure(text=f"Terjadi kesalahan: {e}")
        progress_bar.set(0)