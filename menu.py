import tkinter as tk
import subprocess
import sys


def buka_luas():
    window.destroy()
    subprocess.Popen([sys.executable, "Luas Bangun Datar.py"])


def buka_keliling():
    window.destroy()
    subprocess.Popen([sys.executable, "Keliling Bangun Datar.py"])


def buka_soal():
    window.destroy()
    subprocess.Popen([sys.executable, "Soal Random Geometri.py"])


awan = []


def posisikan_awan(item):
    x = item["x"]
    y = item["y"] * canvas.winfo_height()
    skala = item["skala"]
    bentuk = [
        (x, y + 19 * skala, x + 38 * skala, y + 48 * skala),
        (x + 18 * skala, y + 4 * skala, x + 72 * skala, y + 48 * skala),
        (x + 49 * skala, y + 15 * skala, x + 91 * skala, y + 48 * skala),
        (x + 7 * skala, y + 27 * skala, x + 88 * skala, y + 51 * skala),
    ]
    for bagian, koordinat in zip(item["bagian"], bentuk):
        canvas.coords(bagian, *koordinat)


def gambar_gradasi(event=None):
    canvas.delete("gradient")
    lebar = max(canvas.winfo_width(), 1)
    tinggi = max(canvas.winfo_height(), 1)

    warna_awal = (91, 183, 235)
    warna_akhir = (208, 239, 255)
    for y in range(tinggi):
        t = y / max(tinggi - 1, 1)
        warna = "#%02x%02x%02x" % tuple(
            int(a + (b - a) * t) for a, b in zip(warna_awal, warna_akhir)
        )
        canvas.create_line(0, y, lebar, y, fill=warna, tags="gradient")
    canvas.tag_lower("gradient")

    if not awan:
        for x, posisi_y, skala, kecepatan in [
            (-90, 0.13, 1.1, 0.45),
            (lebar * 0.30, 0.78, 0.8, 0.30),
            (lebar * 0.72, 0.34, 1.0, 0.38),
        ]:
            bagian = [
                canvas.create_oval(
                    0, 0, 0, 0, fill="#f8fdff", outline="", tags="cloud"
                )
                for _ in range(4)
            ]
            awan.append({
                "x": x,
                "y": posisi_y,
                "skala": skala,
                "kecepatan": kecepatan,
                "bagian": bagian,
            })

    for item in awan:
        posisikan_awan(item)


def gerakkan_awan():
    lebar = canvas.winfo_width()
    for item in awan:
        item["x"] += item["kecepatan"]
        if item["x"] > lebar + 100 * item["skala"]:
            item["x"] = -100 * item["skala"]
        posisikan_awan(item)
    window.after(35, gerakkan_awan)


def atur_hover(tombol, warna_normal, warna_hover):
    tombol.bind(
        "<Enter>", lambda event: tombol.config(bg=warna_hover, cursor="hand2")
    )
    tombol.bind("<Leave>", lambda event: tombol.config(bg=warna_normal, cursor=""))


window = tk.Tk()
window.title("Program Geometri & Latihan Soal")
window.geometry("600x530")
window.minsize(500, 480)
window.config(bg="#5bb7eb")

canvas = tk.Canvas(window, highlightthickness=0, bd=0)
canvas.pack(fill="both", expand=True)
canvas.bind("<Configure>", gambar_gradasi)

kartu = tk.Frame(
    canvas, bg="#ffffff", highlightthickness=1, highlightbackground="#dce4f2"
)
kartu.place(relx=0.5, rely=0.5, anchor="center", width=460, height=420)

ikon = tk.Label(
    kartu, text="KALKULATOR GEOMETRI", font=("Arial", 10, "bold"), fg="#3978d4", bg="#ffffff"
)
ikon.pack(pady=(20, 2))

judul = tk.Label(
    kartu,
    text="PROGRAM BANGUN DATAR",
    font=("Arial", 18, "bold"),
    fg="#172544",
    bg="#ffffff",
)
judul.pack(pady=(3, 5))

aksen = tk.Frame(kartu, bg="#4d8df5", height=4, width=70)
aksen.pack(pady=(0, 10))

deskripsi = tk.Label(
    kartu,
    text="Hitung Luas, Keliling, Invers & Latihan Soal",
    font=("Arial", 10),
    fg="#68758e",
    bg="#ffffff",
)
deskripsi.pack(pady=(0, 14))

button_luas = tk.Button(
    kartu,
    text="⌂   HITUNG LUAS & INVERS",
    font=("Arial", 11, "bold"),
    fg="#ffffff",
    bg="#3978d4",
    activebackground="#285fae",
    activeforeground="#ffffff",
    relief="flat",
    bd=0,
    width=28,
    height=2,
    command=buka_luas,
)
button_luas.pack(pady=6)
atur_hover(button_luas, "#3978d4", "#285fae")

button_keliling = tk.Button(
    kartu,
    text="◉   HITUNG KELILING & INVERS",
    font=("Arial", 11, "bold"),
    fg="#ffffff",
    bg="#19a985",
    activebackground="#128367",
    activeforeground="#ffffff",
    relief="flat",
    bd=0,
    width=28,
    height=2,
    command=buka_keliling,
)
button_keliling.pack(pady=6)
atur_hover(button_keliling, "#19a985", "#128367")

button_soal = tk.Button(
    kartu,
    text="✎   LATIHAN SOAL RANDOM",
    font=("Arial", 11, "bold"),
    fg="#ffffff",
    bg="#f0932b",
    activebackground="#e0821b",
    activeforeground="#ffffff",
    relief="flat",
    bd=0,
    width=28,
    height=2,
    command=buka_soal,
)
button_soal.pack(pady=6)
atur_hover(button_soal, "#f0932b", "#e0821b")

catatan = tk.Label(
    kartu,
    text="Pilih menu pembelajaran yang kamu inginkan",
    font=("Arial", 9),
    fg="#9aa5b7",
    bg="#ffffff",
)
catatan.pack(pady=(10, 0))

window.after(35, gerakkan_awan)
window.mainloop()