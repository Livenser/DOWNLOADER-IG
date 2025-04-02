import os
import instaloader
import aiohttp
import asyncio
import customtkinter as ctk

def get_default_download_path():
    if os.name == 'nt':
        return os.path.join(os.environ['USERPROFILE'], 'Downloads')
    else:
        return os.path.join(os.path.expanduser('~'), 'Downloads')

async def download_video_from_link(link, result_label, progress_bar):
    try:
        loader = instaloader.Instaloader()

        # Ekstrak shortcode dari URL
        try:
            shortcode = link.split("/reel/")[1].split("/")[0]
        except IndexError:
            result_label.configure(text="Tautan tidak valid. Pastikan Anda memasukkan tautan video Instagram yang benar.")
            return

        # Dapatkan informasi postingan
        try:
            post = instaloader.Post.from_shortcode(loader.context, shortcode)
        except Exception as e:
            result_label.configure(text=f"Gagal memuat postingan: {e}")
            return

        # Pastikan postingan adalah video
        if not post.is_video:
            result_label.configure(text="Postingan ini bukan video.")
            return

        # Dapatkan URL video langsung
        video_url = post.video_url

        # Unduh video menggunakan aiohttp
        save_dir = get_default_download_path()
        os.makedirs(save_dir, exist_ok=True)
        filename = f"{post.owner_username}_{shortcode}.mp4"
        save_path = os.path.join(save_dir, filename)

        async with aiohttp.ClientSession() as session:
            async with session.get(video_url) as response:
                if response.status == 200:
                    total_size = int(response.headers.get("content-length", 0))
                    block_size = 16384  # Ukuran chunk lebih besar untuk meningkatkan kecepatan
                    downloaded = 0
                    update_interval = 10  # Perbarui progress bar setiap 10 chunk
                    chunk_count = 0

                    with open(save_path, 'wb') as file:
                        async for chunk in response.content.iter_chunked(block_size):
                            if chunk:
                                file.write(chunk)
                                downloaded += len(chunk)
                                chunk_count += 1
                                if chunk_count % update_interval == 0:
                                    progress = downloaded / total_size
                                    progress_bar.set(progress)
                                    progress_bar.update()

                    # Verifikasi ukuran file
                    if os.path.getsize(save_path) < total_size:
                        result_label.configure(text="Video tidak sepenuhnya diunduh.")
                        return

                    result_label.configure(text=f"Video berhasil diunduh ke '{save_path}'")
                    progress_bar.set(0)
                else:
                    result_label.configure(text="Gagal mengunduh video. Pastikan tautan valid.")
    except Exception as e:
        result_label.configure(text=f"Terjadi kesalahan: {e}")
        progress_bar.set(0)