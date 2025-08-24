<h2 align="center"> 
  <b> Total Visits </b><br><br>
  <img src="https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2FWannnIl%2FInjX-Scanner&countColor=%23028b91" /> <br /> <br />
</h2>

# InjX Scanner - SQLi & XSS Scanner (Belajar) 🎓 ![Python 2|3](https://img.shields.io/badge/python-2|3-yellow.svg)

<img src="https://github.com/WannnIl/InjX-Scanner/blob/main/screenshot/exa1.png?raw=true">

**InjX Scanner** adalah tools sederhana untuk mendeteksi **SQL Injection (SQLi)** dan **Reflected XSS** pada parameter URL.  
Tools ini dibuat sebagai **alat belajar** untuk memahami dasar keamanan web dan **testing parameter URL**.  
Perlu dicatat, tools ini **belum sempurna** dan masih dalam tahap pengembangan.  

---

## Fitur

- Deteksi **SQL Injection** sederhana.
- Deteksi **Reflected XSS** sederhana.
- Output berwarna untuk memudahkan identifikasi.
- Bisa memindai beberapa parameter URL sekaligus.
- Cocok digunakan untuk belajar **web security** dan **pentesting dasar**.

---

## Catatan Penting

- Tools ini hanya untuk **belajar dan testing di lingkungan yang aman** (localhost atau target yang memiliki izin eksplisit).  
- Penggunaan pada situs tanpa izin adalah **ilegal**.  
- Tools ini masih **belum sempurna**, beberapa payload atau skenario mungkin tidak terdeteksi.

---

## Instalasi

1. Clone repository:

```bash
https://github.com/WannnIl/InjX-Scanner.git
cd InjX-Scanner
```
2. Buat virtual environment (opsional):

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install dependency:

```bash
pip3 install -r requirements.txt
```
4. Penggunaan:

```bash
python3 InjX.py --url "https://target.com/page.php?id=1"
```

## Disclaimer

- Tools ini untuk tujuan edukasi saja.

- Jangan digunakan untuk menyerang website tanpa izin.

- Pembuat tidak bertanggung jawab atas penyalahgunaan.
