# Credit by : Aruvu (livenser)
# Tanggal buat : 02-04-2025
# Jangan dihapus bg creditnya, HARGAIN GW WKWKW.

import os
import sys
import asyncio
from PIL import Image
import customtkinter as ctk
from downloadvideo import download_video_from_link
from downloadprofile import download_instagram_profile
from downloadimage import download_image_post
import threading

def resource_path(relative_path):
    """Mengembalikan path absolut untuk file resource."""
    try:
        # PyInstaller menyimpan file di _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def handle_choice(choice):
    if choice == "video":
        link = video_entry.get().strip()
        if not link:
            result_label.configure(text="Masukkan tautan video terlebih dahulu.")
            return
        if "instagram.com" not in link:
            result_label.configure(text="Tautan tidak valid. Harap masukkan tautan Instagram.")
            return
        # Jalankan unduhan dalam thread untuk menjaga GUI responsif
        threading.Thread(target=lambda: asyncio.run(download_video_from_link(link, result_label, progress_bar))).start()
    elif choice == "profile":
        username = profile_entry.get().strip()
        if not username:
            result_label.configure(text="Masukkan username terlebih dahulu.")
            return
        threading.Thread(target=download_instagram_profile, args=(username, result_label, progress_bar)).start()
    elif choice == "image":
        link = image_entry.get().strip()
        if not link:
            result_label.configure(text="Masukkan tautan postingan gambar terlebih dahulu.")
            return
        if "instagram.com" not in link:
            result_label.configure(text="Tautan tidak valid. Harap masukkan tautan Instagram.")
            return
        try:
            slide_number = int(slide_entry.get().strip()) if slide_entry.get().strip() else None
        except ValueError:
            slide_number = None
        threading.Thread(target=download_image_post, args=(link, result_label, progress_bar, slide_number)).start()

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Instagram Downloader Aruvu")
root.geometry("800x600")
root.state("zoomed")

background_frame = ctk.CTkFrame(root, fg_color="#121212", corner_radius=0)
background_frame.pack(fill="both", expand=True)

# Cek dan muat logo
logo_path = resource_path("image/logo2.png")
if os.path.exists(logo_path):
    logo_image = ctk.CTkImage(light_image=Image.open(logo_path), size=(150, 150))
    logo_label = ctk.CTkLabel(background_frame, image=logo_image, text="")
    logo_label.pack(pady=30)
else:
    logo_label = ctk.CTkLabel(background_frame, text="Instagram Downloader", font=("Arial", 32, "bold"), text_color="#FFFFFF")
    logo_label.pack(pady=30)

title_label = ctk.CTkLabel(background_frame, text="Instagram Downloader", font=("Arial", 28, "bold"), text_color="#FFFFFF")
title_label.pack(pady=10)

tab_control = ctk.CTkTabview(background_frame, width=750, height=450, corner_radius=15, fg_color="#1E1E1E")
tab_control.pack(pady=20)

video_tab = tab_control.add("Download Video")
profile_tab = tab_control.add("Download Profil")
image_tab = tab_control.add("Download Gambar")

video_label = ctk.CTkLabel(video_tab, text="Masukkan Link Video:", font=("Arial", 16), text_color="#FFFFFF")
video_label.pack(pady=10)
video_entry = ctk.CTkEntry(video_tab, width=500, font=("Arial", 14), corner_radius=10, fg_color="#2C2C2C", text_color="#FFFFFF")
video_entry.pack(pady=10)
video_button = ctk.CTkButton(
    video_tab,
    text="Download Video",
    command=lambda: handle_choice("video"),
    fg_color="#4CAF50",
    hover_color="#388E3C",
    font=("Arial", 16),
    corner_radius=10,
    height=40
)
video_button.pack(pady=20)

profile_label = ctk.CTkLabel(profile_tab, text="Masukkan Username:", font=("Arial", 16), text_color="#FFFFFF")
profile_label.pack(pady=10)
profile_entry = ctk.CTkEntry(profile_tab, width=500, font=("Arial", 14), corner_radius=10, fg_color="#2C2C2C", text_color="#FFFFFF")
profile_entry.pack(pady=10)
profile_button = ctk.CTkButton(
    profile_tab,
    text="Download Profil",
    command=lambda: handle_choice("profile"),
    fg_color="#03A9F4",
    hover_color="#0288D1",
    font=("Arial", 16),
    corner_radius=10,
    height=40
)
profile_button.pack(pady=20)

image_label = ctk.CTkLabel(image_tab, text="Masukkan Link Postingan Gambar:", font=("Arial", 16), text_color="#FFFFFF")
image_label.pack(pady=10)
image_entry = ctk.CTkEntry(image_tab, width=500, font=("Arial", 14), corner_radius=10, fg_color="#2C2C2C", text_color="#FFFFFF")
image_entry.pack(pady=10)
slide_label = ctk.CTkLabel(image_tab, text="Nomor Slide (Opsional):", font=("Arial", 14), text_color="#FFFFFF")
slide_label.pack(pady=5)
slide_entry = ctk.CTkEntry(image_tab, width=100, font=("Arial", 14), corner_radius=10, fg_color="#2C2C2C", text_color="#FFFFFF")
slide_entry.pack(pady=5)
image_button = ctk.CTkButton(
    image_tab,
    text="Download Gambar",
    command=lambda: handle_choice("image"),
    fg_color="#FF9800",
    hover_color="#F57C00",
    font=("Arial", 16),
    corner_radius=10,
    height=40
)
image_button.pack(pady=20)

progress_bar = ctk.CTkProgressBar(background_frame, width=600, mode="determinate", height=20, corner_radius=10, fg_color="#2C2C2C", progress_color="#4CAF50")
progress_bar.set(0)
progress_bar.pack(pady=20)

result_label = ctk.CTkLabel(background_frame, text="", font=("Arial", 14), text_color="#FFFFFF")
result_label.pack(pady=10)

footer_frame = ctk.CTkFrame(background_frame, fg_color="#1E1E1E", corner_radius=0)
footer_frame.pack(side="bottom", pady=20, fill="x")
footer_label = ctk.CTkLabel(
    footer_frame,
    text="© 2025 Aruvu (Livenser)",
    font=("Arial", 12, "italic"),
    text_color="#FFFFFF",
    cursor="hand2"
)
footer_label.pack()

def open_link(event):
    import webbrowser
    webbrowser.open("https://github.com/Livenser/")

footer_label.bind("<Button-1>", open_link)

root.mainloop()