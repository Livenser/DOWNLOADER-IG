import os
import requests
import instaloader
import customtkinter as ctk

def get_default_download_path():
    if os.name == 'nt':
        return os.path.join(os.environ['USERPROFILE'], 'Downloads')
    else:
        return os.path.join(os.path.expanduser('~'), 'Downloads')

def download_image_post(link, result_label, progress_bar, slide_number=None):
    try:
        loader = instaloader.Instaloader()
        save_dir = get_default_download_path()
        os.makedirs(save_dir, exist_ok=True)
        os.chdir(save_dir)
        shortcode = link.split("/p/")[1].split("/")[0]
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        main_image_url = post.url
        main_image_response = requests.get(main_image_url)
        if main_image_response.status_code == 200:
            main_image_filename = f"{post.owner_username}_{shortcode}_main.jpg"
            with open(main_image_filename, "wb") as file:
                file.write(main_image_response.content)
            downloaded_files = [main_image_filename]
        else:
            result_label.configure(text="Gagal mengunduh gambar utama.")
            return
        images = list(post.get_sidecar_nodes())
        if images:
            if slide_number is not None and 1 <= slide_number <= len(images):
                selected_image = images[slide_number - 1]
                slide_image_url = selected_image.display_url
                slide_image_response = requests.get(slide_image_url)
                if slide_image_response.status_code == 200:
                    slide_filename = f"{post.owner_username}_{shortcode}_slide{slide_number}.jpg"
                    with open(slide_filename, "wb") as file:
                        file.write(slide_image_response.content)
                    downloaded_files.append(slide_filename)
                    result_label.configure(text=f"Gambar slide {slide_number} berhasil diunduh sebagai '{slide_filename}'")
                else:
                    result_label.configure(text=f"Gagal mengunduh slide {slide_number}.")
                return
            else:
                for idx, image in enumerate(images, start=1):
                    slide_image_url = image.display_url
                    slide_image_response = requests.get(slide_image_url)
                    if slide_image_response.status_code == 200:
                        slide_filename = f"{post.owner_username}_{shortcode}_slide{idx}.jpg"
                        with open(slide_filename, "wb") as file:
                            file.write(slide_image_response.content)
                        downloaded_files.append(slide_filename)
        result_label.configure(text=f"Gambar berhasil diunduh: {', '.join(downloaded_files)}")
        progress_bar.set(1)
        progress_bar.update()
    except Exception as e:
        result_label.configure(text=f"Terjadi kesalahan: {e}")
        progress_bar.set(0)