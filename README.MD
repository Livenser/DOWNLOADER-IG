<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Instagram Downloader</title>
  <style>
    /* General Styling */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #121212;
      color: #ffffff;
    }
    .container {
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
    }
    h1, h2, h3 {
      color: #bb86fc;
    }
    p {
      line-height: 1.6;
    }
    .center {
      text-align: center;
    }
    .banner img {
      max-width: 100%;
      height: auto;
      border-radius: 10px;
    }
    .feature-table {
      width: 100%;
      border-collapse: collapse;
      margin: 20px 0;
    }
    .feature-table td {
      padding: 15px;
      text-align: center;
      border: 1px solid #333;
      background-color: #1e1e1e;
      border-radius: 5px;
    }
    .code-block {
      background-color: #1e1e1e;
      padding: 10px;
      border-radius: 5px;
      margin: 10px 0;
    }
    .code-block code {
      color: #bb86fc;
      font-size: 14px;
    }
    .button {
      display: inline-block;
      padding: 10px 20px;
      background-color: #bb86fc;
      color: #121212;
      text-decoration: none;
      border-radius: 5px;
      font-weight: bold;
    }
    .button:hover {
      background-color: #9c27b0;
    }
    ul {
      list-style-type: disc;
      padding-left: 20px;
    }
    ol {
      padding-left: 20px;
    }
    a {
      color: #bb86fc;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>
  <div class="container">
    <div style="text-align: center;">
      <h1>🌟 Instagram Downloader</h1>
    </div>

    <div class="banner">
      <img src="https://cdn.discordapp.com/attachments/1313720907629330432/1357974116438900746/ChatGPT_Image_Apr_2_2025_09_15_52_PM.png?ex=67f22773&is=67f0d5f3&hm=346ef24a9af96da6a99925d93b372d6550ea7a190445b8aa2e723a31c12a9b59&" alt="Instagram Downloader Banner" />
    </div>

    <p class="center">
      Halo semuanya! 👋 Aku <strong>Livenser</strong>, seorang siswa SMK kelas 12 yang lagi belajar bikin aplikasi sambil nyiapin diri buat lulus. Kali ini aku bikin <strong>Instagram Downloader</strong>, sebuah aplikasi simpel buat bantu kamu download konten dari Instagram kayak video, gambar, atau foto profil orang. Aplikasi ini aku bikin pake Python sama library <code>customtkinter</code>. Lumayan kan buat latihan coding sambil bantu kalian juga. 😊
    </p>

    <p class="center">
      Oh iya, aplikasi ini punya tampilan GUI yang enak dilihat (menurutku sih 😂) dengan tema gelap (<em>dark mode</em>). Jadi, buat kamu yang suka sesuatu yang simpel dan estetik, cocok banget deh!
    </p>

    <h2>📋 Fitur-Fitur Aplikasi</h2>
    <table class="feature-table">
      <tr>
        <td>
          <img src="https://img.icons8.com/ios-filled/50/ffffff/download.png" alt="Download Icon" width="40" />
          <br />
          <strong>Download Video 🎥</strong>
          <br />
          Download video dari Instagram cuma dengan paste link videonya. Ada progress bar biar kamu bisa liat prosesnya sampe mana.
        </td>
        <td>
          <img src="https://img.icons8.com/ios-filled/50/ffffff/image.png" alt="Image Icon" width="40" />
          <br />
          <strong>Download Gambar 🖼️</strong>
          <br />
          Download gambar dari postingan Instagram, termasuk postingan berslide. Kamu bisa milih mau download satu-satu atau semua gambarnya sekaligus.
        </td>
        <td>
          <img src="https://img.icons8.com/ios-filled/50/ffffff/user-male-circle.png" alt="Profile Icon" width="40" />
          <br />
          <strong>Download Profil Pengguna 👤</strong>
          <br />
          Simpan foto profil pengguna Instagram hanya dengan masukkan username-nya. Gampang banget!
        </td>
      </tr>
    </table>

    <h2>🛠️ Cara Pake Aplikasi Ini</h2>

    <h3>Langkah-Langkah Menggunakan Aplikasi</h3>
    <ol>
      <li>**Download File APK**  
        - Buka folder **APK** di repositori proyek ini.  
        - Download file APK bernama `DOWNLODER IG.apk` ke perangkat kamu.</li>
      <li>**Instal Aplikasi**  
        - Buka file APK yang sudah didownload.  
        > **Catatan:** Jika muncul peringatan "Sumber Tidak Dikenal", aktifkan izin untuk menginstal aplikasi dari sumber eksternal di pengaturan perangkat kamu.  
        - Ikuti langkah-langkah instalasi sampai selesai.</li>
      <li>**Buka Aplikasi**  
        - Setelah instalasi selesai, buka aplikasi **Instagram Downloader** dari menu aplikasi di perangkat kamu.</li>
      <li>**Enjoy!**  
        - Sekarang kamu bisa langsung menikmati fitur-fitur aplikasi tanpa perlu repot setting Python atau library tambahan. Tinggal pilih fitur yang mau dipakai dan ikuti panduan di aplikasi.</li>
    </ol>

    <h2>📂 Hasil Unduhan Disimpan Di Mana?</h2>
    <p>
      Semua file yang kamu download bakal tersimpan di folder **"Downloads"** di laptop kamu. Filenya bakal diberi nama sesuai username atau shortcode postingan. Jadi gampang banget nyari filenya nanti.
    </p>

    <h2>⚙️ Spesifikasi Sistem</h2>
    <ul>
      <li><strong>Python</strong>: Versi 3.7 atau lebih baru.</li>
      <li><strong>Library Python</strong>:
        <ul>
          <li>`customtkinter`</li>
          <li>`requests`</li>
          <li>`instaloader`</li>
          <li>`pillow`</li>
        </ul>
      </li>
    </ul>

    <h2>🚨 Catatan Penting</h2>
    <ul>
      <li><strong>Tautan Harus Valid</strong>: Pastiin link yang kamu masukin itu bener-bener dari Instagram ya.</li>
      <li><strong>Koneksi Internet</strong>: Aplikasi ini butuh koneksi internet yang stabil biar bisa download kontennya.</li>
      <li><strong>Keterbatasan</strong>: Aplikasi ini gak bisa download konten dari akun privat atau yang butuh login.</li>
    </ul>

    <h2>👨‍💻 Tentang Penulis</h2>
    <p>
      Halo lagi! Aku Livenser, anak kelas 12 SMK yang suka ngoding meskipun kadang masih bingung sendiri 😅. Aplikasi ini aku bikin buat latihan aja, tapi kalau ada yang mau kasih masukan atau nanya-nanya, boleh banget hubungi aku di:
    </p>
    <ul>
      <li>📧 Email: <a href="mailto:asmercell2278@gmail.com">asmercell2278@gmail.com</a></li>
      <li>💻 GitHub: <a href="https://github.com/Livenser">https://github.com/Livenser</a></li>
    </ul>

    <h2>🙏 Terima Kasih!</h2>
    <p>
      Makasih banyak udah mau coba aplikasi ini! Semoga aplikasi ini bisa bantu kamu buat nyimpen konten favorit dari Instagram. Kalau kamu suka, jangan lupa kasih bintang (⭐) di repositori GitHub aku ya! 😊
    </p>

    <p class="center">
      <a href="https://github.com/Livenser/DOWNLOADER-IG/tree/main" class="button">GitHub Repository</a>
    </p>
  </div>
</body>
</html>
