import tkinter as tk
import random
import subprocess
import sys


def kembali():
    window.destroy()
    subprocess.Popen([sys.executable, "menu.py"])


soal_saat_ini = {}


def buat_soal():
    global soal_saat_ini
    pilihan_tipe = [
        "luas_persegi",
        "keliling_persegi",
        "invers_luas_persegi",
        "invers_keliling_persegi",
        "luas_lingkaran",
        "invers_luas_lingkaran",
    ]
    jenis = random.choice(pilihan_tipe)

    if jenis == "luas_persegi":
        s = random.randint(3, 20)
        kunci = s * s
        teks = f"Berapakah Luas Persegi dengan panjang sisi {s} cm?"
    elif jenis == "keliling_persegi":
        s = random.randint(3, 20)
        kunci = 4 * s
        teks = f"Berapakah Keliling Persegi dengan panjang sisi {s} cm?"
    elif jenis == "invers_luas_persegi":
        s = random.randint(3, 15)
        L = s * s
        kunci = s
        teks = f"(Invers) Sebuah Persegi memiliki Luas {L} cm². Berapakah panjang sisinya?"
    elif jenis == "invers_keliling_persegi":
        s = random.randint(4, 20)
        K = 4 * s
        kunci = s
        teks = f"(Invers) Sebuah Persegi memiliki Keliling {K} cm². Berapakah panjang sisinya?"
    elif jenis == "luas_lingkaran":
        r = 7  # Menggunakan r=7 agar pas dengan phi 22/7
        kunci = (22 / 7) * r * r
        teks = f"Berapakah Luas Lingkaran dengan jari-jari {r} cm? (Gunakan π = 22/7)"
    else:  # invers_luas_lingkaran
        r = 7
        L = (22 / 7) * r * r
        kunci = r
        teks = f"(Invers) Sebuah Lingkaran berluas {L:.0f} cm² (π = 22/7). Berapakah jari-jarinya (r)?"

    soal_saat_ini = {"teks": teks, "jawaban": round(kunci, 2)}
    label_soal.config(text=teks)
    entry_jawaban.delete(0, tk.END)
    label_hasil.config(text="Hasil pengecekan akan tampil di sini", fg="#68758e")


def cek_jawaban():
    try:
        user_ans = float(entry_jawaban.get())
        kunci = soal_saat_ini["jawaban"]
        if abs(user_ans - kunci) < 0.1:
            label_hasil.config(text="✔ Benar Sekali! Kerja Bagus!", fg="#27ae60")
        else:
            label_hasil.config(
                text=f"✖ Kurang tepat. Jawaban yang benar adalah {kunci:g}",
                fg="#c0392b",
            )
    except ValueError:
        label_hasil.config(text="⚠ Masukkan angka jawaban yang valid!", fg="#e67e22")


window = tk.Tk()
window.title("Latihan Soal Random Geometri & Invers")
window.geometry("650x500")
window.config(bg="#EAF7FF")

header = tk.Canvas(window, height=110, bg="#8ED8FF", highlightthickness=0)
header.pack(fill="x")


def buat_awan(x, y, ukuran=1):
    bagian = []
    for dx, dy, lebar, tinggi in (
        (0, 18, 48, 28),
        (25, 0, 55, 42),
        (58, 13, 50, 32),
        (20, 23, 75, 28),
    ):
        bagian.append(
            header.create_oval(
                x + dx * ukuran,
                y + dy * ukuran,
                x + (dx + lebar) * ukuran,
                y + (dy + tinggi) * ukuran,
                fill="white",
                outline="white",
            )
        )
    return bagian


awan_bergerak = [
    {"bagian": buat_awan(30, 25, 0.8), "kecepatan": 1.0},
    {"bagian": buat_awan(350, 10, 0.65), "kecepatan": 0.7},
]
header.create_text(
    325,
    42,
    text="Latihan Soal Random Geometri & Invers",
    font=("Arial", 19, "bold"),
    fill="#164B70",
)
header.create_text(
    325,
    75,
    text="Uji kemampuan perhitungan rumus dan fungsi invers bangun datar",
    font=("Arial", 10),
    fill="#245C7A",
)


def gerakkan_awan():
    lebar = header.winfo_width()
    for awan in awan_bergerak:
        ids = awan["bagian"]
        for item in ids:
            header.move(item, awan["kecepatan"], 0)
        batas = header.bbox(ids[0])
        if batas and batas[0] > lebar + 15:
            for item in ids:
                header.move(item, -lebar - 180, 0)
    window.after(35, gerakkan_awan)


gerakkan_awan()

frame_soal = tk.Frame(
    window, bg="white", highlightthickness=1, highlightbackground="#A8D8EA"
)
frame_soal.pack(fill="both", expand=True, padx=25, pady=20)

tk.Label(
    frame_soal,
    text="Pertanyaan:",
    font=("Arial", 11, "bold"),
    fg="#168AAD",
    bg="white",
).pack(pady=(15, 5))
label_soal = tk.Label(
    frame_soal,
    text="Tekan tombol 'Soal Baru' untuk mulai",
    font=("Arial", 12),
    fg="#172544",
    bg="white",
    wraplength=550,
    justify="center",
)
label_soal.pack(pady=10)

entry_jawaban = tk.Entry(
    frame_soal, font=("Arial", 12), justify="center", relief="solid", bd=1
)
entry_jawaban.pack(pady=10, ipady=3, ipadx=10)

btn_frame = tk.Frame(frame_soal, bg="white")
btn_frame.pack(pady=5)

tk.Button(
    btn_frame,
    text="Cek Jawaban",
    font=("Arial", 10, "bold"),
    bg="#27ae60",
    fg="white",
    padx=10,
    pady=5,
    command=cek_jawaban,
).grid(row=0, column=0, padx=5)
tk.Button(
    btn_frame,
    text="Soal Baru",
    font=("Arial", 10, "bold"),
    bg="#2980b9",
    fg="white",
    padx=10,
    pady=5,
    command=buat_soal,
).grid(row=0, column=1, padx=5)

label_hasil = tk.Label(
    frame_soal,
    text="Hasil pengecekan akan tampil di sini",
    font=("Arial", 11, "bold"),
    fg="#68758e",
    bg="white",
)
label_hasil.pack(pady=(15, 15))

tk.Button(
    window,
    text="Kembali Ke Menu",
    font=("Arial", 11, "bold"),
    bg="red",
    fg="white",
    width=25,
    command=kembali,
).pack(pady=(0, 15))

buat_soal()
window.mainloop()