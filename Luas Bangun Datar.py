import tkinter as tk
import math
import subprocess
import sys
from tkinter import ttk, messagebox


def kembali():
    window.destroy()
    subprocess.Popen([sys.executable, "menu.py"])


def tampilkan_hasil(label, teks):
    label.config(text=teks, bg="#B7F3D2")
    label.after(550, lambda: label.config(bg="#EAF7FF"))


def ambil_ukuran(entry):
    nilai = float(entry.get())
    if nilai <= 0:
        raise ValueError("Ukuran harus lebih besar dari 0.")
    return nilai


# --- FUNGSI GAMBAR BANGUN DATAR ---
def buat_gambar_bangun(parent, jenis):
    kanvas = tk.Canvas(parent, width=140, height=100, bg="#EAF7FF", highlightthickness=0)
    warna = "#46A6D5"
    if jenis == "persegi":
        kanvas.create_rectangle(30, 15, 110, 95, fill="#B7E7F7", outline=warna, width=3)
    elif jenis == "persegi_panjang":
        kanvas.create_rectangle(15, 25, 125, 85, fill="#B7E7F7", outline=warna, width=3)
    elif jenis == "segitiga":
        kanvas.create_polygon(70, 15, 125, 95, 15, 95, fill="#B7E7F7", outline=warna, width=3)
    elif jenis == "lingkaran":
        kanvas.create_oval(30, 15, 110, 95, fill="#B7E7F7", outline=warna, width=3)
    elif jenis == "jajar_genjang":
        kanvas.create_polygon(35, 20, 125, 20, 105, 95, 15, 95, fill="#B7E7F7", outline=warna, width=3)
    return kanvas


# --- HITUNG LUAS ---
def hitung_persegi():
    try:
        sisi = ambil_ukuran(entry_sisi)
        luas = sisi * sisi
        tampilkan_hasil(hasil_persegi, f"Luas Persegi = {luas:g}")
    except ValueError:
        messagebox.showerror("Input tidak valid", "Masukkan angka > 0.")


def hitung_persegi_panjang():
    try:
        p = ambil_ukuran(entry_panjang)
        l = ambil_ukuran(entry_lebar)
        luas = p * l
        tampilkan_hasil(hasil_persegi_panjang, f"Luas Persegi Panjang = {luas:g}")
    except ValueError:
        messagebox.showerror("Input tidak valid", "Masukkan angka > 0.")


def hitung_segitiga():
    try:
        a = ambil_ukuran(entry_alas)
        t = ambil_ukuran(entry_tinggi)
        luas = 0.5 * a * t
        tampilkan_hasil(hasil_segitiga, f"Luas Segitiga = {luas:g}")
    except ValueError:
        messagebox.showerror("Input tidak valid", "Masukkan angka > 0.")


def hitung_lingkaran():
    try:
        r = ambil_ukuran(entry_jari_jari)
        pilih_pi = var_pi.get()
        pi_val = 22 / 7 if pilih_pi == "22/7" else 3.14159
        luas = pi_val * r * r
        tampilkan_hasil(hasil_lingkaran, f"Luas Lingkaran = {luas:.2f}")
    except ValueError:
        messagebox.showerror("Input tidak valid", "Masukkan angka > 0.")


def hitung_jajar_genjang():
    try:
        a = ambil_ukuran(entry_alasJ)
        t = ambil_ukuran(entry_tinggiJ)
        luas = a * t
        tampilkan_hasil(hasil_jajar_genjang, f"Luas Jajar Genjang = {luas:g}")
    except ValueError:
        messagebox.showerror("Input tidak valid", "Masukkan angka > 0.")


# --- INVERS LUAS ---
def invers_persegi():
    try:
        L = ambil_ukuran(entry_inv_l_p)
        sisi = math.sqrt(L)
        tampilkan_hasil(hasil_inv_p, f"Sisi = {sisi:.2f} (dari Luas)")
    except ValueError:
        messagebox.showerror("Input tidak valid", "Masukkan luas > 0.")


def invers_persegi_panjang():
    try:
        L = ambil_ukuran(entry_inv_l_pp)
        p = ambil_ukuran(entry_inv_l_pp_p)
        l_hasil = L / p
        tampilkan_hasil(hasil_inv_pp, f"Lebar = {l_hasil:.2f} (dari Luas & Panjang)")
    except ValueError:
        messagebox.showerror("Input tidak valid", "Masukkan angka valid > 0.")


def invers_segitiga():
    try:
        L = ambil_ukuran(entry_inv_l_s)
        a = ambil_ukuran(entry_inv_l_s_a)
        t = (2 * L) / a
        tampilkan_hasil(hasil_inv_s, f"Tinggi = {t:.2f} (dari Luas & Alas)")
    except ValueError:
        messagebox.showerror("Input tidak valid", "Masukkan angka valid > 0.")


def invers_lingkaran():
    try:
        L = ambil_ukuran(entry_inv_l_l)
        pilih_pi = var_pi_inv.get()
        pi_val = 22 / 7 if pilih_pi == "22/7" else 3.14159
        r = math.sqrt(L / pi_val)
        tampilkan_hasil(hasil_inv_l, f"Jari-jari (r) = {r:.2f} (dari Luas)")
    except ValueError:
        messagebox.showerror("Input tidak valid", "Masukkan luas > 0.")


def invers_jajar_genjang():
    try:
        L = ambil_ukuran(entry_inv_l_jg)
        a = ambil_ukuran(entry_inv_l_jg_a)
        t = L / a
        tampilkan_hasil(hasil_inv_jg, f"Tinggi = {t:.2f} (dari Luas & Alas)")
    except ValueError:
        messagebox.showerror("Input tidak valid", "Masukkan angka valid > 0.")


# --- GUI SETUP ---
window = tk.Tk()
window.title("Program Perhitungan Luas & Invers Bangun Datar")
window.geometry("850x880")
window.config(bg="#EAF7FF")

header = tk.Canvas(window, height=115, bg="#8ED8FF", highlightthickness=0)
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
    {"bagian": buat_awan(25, 30, 0.8), "kecepatan": 1.0},
    {"bagian": buat_awan(350, 12, 0.65), "kecepatan": 0.7},
]
header.create_text(
    425,
    42,
    text="Perhitungan Luas & Invers Bangun Datar",
    font=("Arial", 20, "bold"),
    fill="#164B70",
)
header.create_text(
    425,
    75,
    text="Lengkap dengan gambar, pilihan Phi (π), dan fungsi invers",
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

notebook = ttk.Notebook(window)
notebook.pack(fill="both", expand=True, padx=20, pady=10)

tab_persegi = tk.Frame(notebook, bg="#EAF7FF")
tab_persegi_panjang = tk.Frame(notebook, bg="#EAF7FF")
tab_segitiga = tk.Frame(notebook, bg="#EAF7FF")
tab_lingkaran = tk.Frame(notebook, bg="#EAF7FF")
tab_jajar_genjang = tk.Frame(notebook, bg="#EAF7FF")

notebook.add(tab_persegi, text="Persegi")
notebook.add(tab_persegi_panjang, text="Persegi Panjang")
notebook.add(tab_segitiga, text="Segitiga")
notebook.add(tab_lingkaran, text="Lingkaran")
notebook.add(tab_jajar_genjang, text="Jajar Genjang")


# 1. PERSEGI
tk.Label(
    tab_persegi, text="Luas & Invers Persegi", font=("Arial", 15, "bold"), bg="#EAF7FF"
).grid(row=0, column=0, columnspan=3, pady=10)
buat_gambar_bangun(tab_persegi, "persegi").grid(row=1, column=0, rowspan=3, padx=10)
tk.Label(
    tab_persegi, text="Rumus: L = sisi × sisi", font=("Arial", 11, "bold"), bg="#EAF7FF"
).grid(row=1, column=1, columnspan=2, sticky="w", padx=5)

tk.Label(tab_persegi, text="Panjang Sisi:", bg="#EAF7FF").grid(
    row=2, column=1, padx=5, pady=5, sticky="w"
)
entry_sisi = tk.Entry(tab_persegi)
entry_sisi.grid(row=2, column=2, padx=5, pady=5)
tk.Button(tab_persegi, text="Hitung Luas", command=hitung_persegi).grid(
    row=3, column=2, pady=5, sticky="e"
)
hasil_persegi = tk.Label(tab_persegi, text="Luas = ...", bg="#EAF7FF")
hasil_persegi.grid(row=3, column=1, sticky="w")

tk.Label(
    tab_persegi,
    text="--- Invers: Cari Sisi dari Luas ---",
    font=("Arial", 9, "bold"),
    fg="#168AAD",
    bg="#EAF7FF",
).grid(row=4, column=0, columnspan=3, pady=10)
tk.Label(tab_persegi, text="Masukkan Luas:", bg="#EAF7FF").grid(
    row=5, column=1, sticky="w", padx=5
)
entry_inv_l_p = tk.Entry(tab_persegi)
entry_inv_l_p.grid(row=5, column=2, padx=5, pady=3)
tk.Button(
    tab_persegi, text="Hitung Invers (Sisi)", command=invers_persegi
).grid(row=6, column=2, pady=3, sticky="e")
hasil_inv_p = tk.Label(tab_persegi, text="Sisi = ...", bg="#EAF7FF")
hasil_inv_p.grid(row=6, column=1, sticky="w")


# 2. PERSEGI PANJANG
tk.Label(
    tab_persegi_panjang,
    text="Luas & Invers Persegi Panjang",
    font=("Arial", 15, "bold"),
    bg="#EAF7FF",
).grid(row=0, column=0, columnspan=3, pady=10)
buat_gambar_bangun(tab_persegi_panjang, "persegi_panjang").grid(
    row=1, column=0, rowspan=4, padx=10
)
tk.Label(
    tab_persegi_panjang,
    text="Rumus: L = panjang × lebar",
    font=("Arial", 11, "bold"),
    bg="#EAF7FF",
).grid(row=1, column=1, columnspan=2, sticky="w", padx=5)

tk.Label(tab_persegi_panjang, text="Panjang:", bg="#EAF7FF").grid(
    row=2, column=1, sticky="w", padx=5
)
entry_panjang = tk.Entry(tab_persegi_panjang)
entry_panjang.grid(row=2, column=2, padx=5, pady=3)
tk.Label(tab_persegi_panjang, text="Lebar:", bg="#EAF7FF").grid(
    row=3, column=1, sticky="w", padx=5
)
entry_lebar = tk.Entry(tab_persegi_panjang)
entry_lebar.grid(row=3, column=2, padx=5, pady=3)
tk.Button(
    tab_persegi_panjang, text="Hitung Luas", command=hitung_persegi_panjang
).grid(row=4, column=2, pady=3, sticky="e")
hasil_persegi_panjang = tk.Label(
    tab_persegi_panjang, text="Luas = ...", bg="#EAF7FF"
)
hasil_persegi_panjang.grid(row=4, column=1, sticky="w")

tk.Label(
    tab_persegi_panjang,
    text="--- Invers: Cari Lebar dari Luas & Panjang ---",
    font=("Arial", 9, "bold"),
    fg="#168AAD",
    bg="#EAF7FF",
).grid(row=5, column=0, columnspan=3, pady=8)
tk.Label(tab_persegi_panjang, text="Masukkan Luas:", bg="#EAF7FF").grid(
    row=6, column=1, sticky="w", padx=5
)
entry_inv_l_pp = tk.Entry(tab_persegi_panjang)
entry_inv_l_pp.grid(row=6, column=2, padx=5, pady=3)
tk.Label(tab_persegi_panjang, text="Masukkan Panjang:", bg="#EAF7FF").grid(
    row=7, column=1, sticky="w", padx=5
)
entry_inv_l_pp_p = tk.Entry(tab_persegi_panjang)
entry_inv_l_pp_p.grid(row=7, column=2, padx=5, pady=3)
tk.Button(
    tab_persegi_panjang,
    text="Hitung Invers (Lebar)",
    command=invers_persegi_panjang,
).grid(row=8, column=2, pady=3, sticky="e")
hasil_inv_pp = tk.Label(tab_persegi_panjang, text="Lebar = ...", bg="#EAF7FF")
hasil_inv_pp.grid(row=8, column=1, sticky="w")


# 3. SEGITIGA
tk.Label(
    tab_segitiga, text="Luas & Invers Segitiga", font=("Arial", 15, "bold"), bg="#EAF7FF"
).grid(row=0, column=0, columnspan=3, pady=10)
buat_gambar_bangun(tab_segitiga, "segitiga").grid(row=1, column=0, rowspan=4, padx=10)
tk.Label(
    tab_segitiga,
    text="Rumus: L = ½ × alas × tinggi",
    font=("Arial", 11, "bold"),
    bg="#EAF7FF",
).grid(row=1, column=1, columnspan=2, sticky="w", padx=5)

tk.Label(tab_segitiga, text="Alas:", bg="#EAF7FF").grid(
    row=2, column=1, sticky="w", padx=5
)
entry_alas = tk.Entry(tab_segitiga)
entry_alas.grid(row=2, column=2, padx=5, pady=3)
tk.Label(tab_segitiga, text="Tinggi:", bg="#EAF7FF").grid(
    row=3, column=1, sticky="w", padx=5
)
entry_tinggi = tk.Entry(tab_segitiga)
entry_tinggi.grid(row=3, column=2, padx=5, pady=3)
tk.Button(tab_segitiga, text="Hitung Luas", command=hitung_segitiga).grid(
    row=4, column=2, pady=3, sticky="e"
)
hasil_segitiga = tk.Label(tab_segitiga, text="Luas = ...", bg="#EAF7FF")
hasil_segitiga.grid(row=4, column=1, sticky="w")

tk.Label(
    tab_segitiga,
    text="--- Invers: Cari Tinggi dari Luas & Alas ---",
    font=("Arial", 9, "bold"),
    fg="#168AAD",
    bg="#EAF7FF",
).grid(row=5, column=0, columnspan=3, pady=8)
tk.Label(tab_segitiga, text="Masukkan Luas:", bg="#EAF7FF").grid(
    row=6, column=1, sticky="w", padx=5
)
entry_inv_l_s = tk.Entry(tab_segitiga)
entry_inv_l_s.grid(row=6, column=2, padx=5, pady=3)
tk.Label(tab_segitiga, text="Masukkan Alas:", bg="#EAF7FF").grid(
    row=7, column=1, sticky="w", padx=5
)
entry_inv_l_s_a = tk.Entry(tab_segitiga)
entry_inv_l_s_a.grid(row=7, column=2, padx=5, pady=3)
tk.Button(
    tab_segitiga, text="Hitung Invers (Tinggi)", command=invers_segitiga
).grid(row=8, column=2, pady=3, sticky="e")
hasil_inv_s = tk.Label(tab_segitiga, text="Tinggi = ...", bg="#EAF7FF")
hasil_inv_s.grid(row=8, column=1, sticky="w")


# 4. LINGKARAN (Dengan Phi)
tk.Label(
    tab_lingkaran,
    text="Luas & Invers Lingkaran (Pilih Phi)",
    font=("Arial", 15, "bold"),
    bg="#EAF7FF",
).grid(row=0, column=0, columnspan=3, pady=10)
buat_gambar_bangun(tab_lingkaran, "lingkaran").grid(row=1, column=0, rowspan=5, padx=10)

var_pi = tk.StringVar(value="22/7")
frame_pi = tk.Frame(tab_lingkaran, bg="#EAF7FF")
frame_pi.grid(row=1, column=1, columnspan=2, sticky="w", padx=5)
tk.Label(frame_pi, text="Phi:", bg="#EAF7FF").pack(side="left")
tk.Radiobutton(
    frame_pi, text="22/7", variable=var_pi, value="22/7", bg="#EAF7FF"
).pack(side="left")
tk.Radiobutton(
    frame_pi, text="3.14", variable=var_pi, value="3.14", bg="#EAF7FF"
).pack(side="left")

tk.Label(tab_lingkaran, text="Jari-jari (r):", bg="#EAF7FF").grid(
    row=2, column=1, sticky="w", padx=5
)
entry_jari_jari = tk.Entry(tab_lingkaran)
entry_jari_jari.grid(row=2, column=2, padx=5, pady=3)
tk.Button(tab_lingkaran, text="Hitung Luas", command=hitung_lingkaran).grid(
    row=3, column=2, pady=3, sticky="e"
)
hasil_lingkaran = tk.Label(tab_lingkaran, text="Luas = ...", bg="#EAF7FF")
hasil_lingkaran.grid(row=3, column=1, sticky="w")

tk.Label(
    tab_lingkaran,
    text="--- Invers: Cari Jari-jari dari Luas ---",
    font=("Arial", 9, "bold"),
    fg="#168AAD",
    bg="#EAF7FF",
).grid(row=4, column=1, columnspan=3, pady=6)

var_pi_inv = tk.StringVar(value="22/7")
frame_pi_inv = tk.Frame(tab_lingkaran, bg="#EAF7FF")
frame_pi_inv.grid(row=5, column=1, columnspan=2, sticky="w", padx=5)
tk.Label(frame_pi_inv, text="Phi:", bg="#EAF7FF").pack(side="left")
tk.Radiobutton(
    frame_pi_inv, text="22/7", variable=var_pi_inv, value="22/7", bg="#EAF7FF"
).pack(side="left")
tk.Radiobutton(
    frame_pi_inv, text="3.14", variable=var_pi_inv, value="3.14", bg="#EAF7FF"
).pack(side="left")

tk.Label(tab_lingkaran, text="Masukkan Luas:", bg="#EAF7FF").grid(
    row=6, column=1, sticky="w", padx=5
)
entry_inv_l_l = tk.Entry(tab_lingkaran)
entry_inv_l_l.grid(row=6, column=2, padx=5, pady=3)
tk.Button(
    tab_lingkaran,
    text="Hitung Invers (r)",
    command=invers_lingkaran,
).grid(row=7, column=2, pady=3, sticky="e")
hasil_inv_l = tk.Label(tab_lingkaran, text="r = ...", bg="#EAF7FF")
hasil_inv_l.grid(row=7, column=1, sticky="w")


# 5. JAJAR GENJANG
tk.Label(
    tab_jajar_genjang,
    text="Luas & Invers Jajar Genjang",
    font=("Arial", 15, "bold"),
    bg="#EAF7FF",
).grid(row=0, column=0, columnspan=3, pady=10)
buat_gambar_bangun(tab_jajar_genjang, "jajar_genjang").grid(
    row=1, column=0, rowspan=4, padx=10
)
tk.Label(
    tab_jajar_genjang,
    text="Rumus: L = alas × tinggi",
    font=("Arial", 11, "bold"),
    bg="#EAF7FF",
).grid(row=1, column=1, columnspan=2, sticky="w", padx=5)

tk.Label(tab_jajar_genjang, text="Alas:", bg="#EAF7FF").grid(
    row=2, column=1, sticky="w", padx=5
)
entry_alasJ = tk.Entry(tab_jajar_genjang)
entry_alasJ.grid(row=2, column=2, padx=5, pady=3)
tk.Label(tab_jajar_genjang, text="Tinggi:", bg="#EAF7FF").grid(
    row=3, column=1, sticky="w", padx=5
)
entry_tinggiJ = tk.Entry(tab_jajar_genjang)
entry_tinggiJ.grid(row=3, column=2, padx=5, pady=3)
tk.Button(
    tab_jajar_genjang, text="Hitung Luas", command=hitung_jajar_genjang
).grid(row=4, column=2, pady=3, sticky="e")
hasil_jajar_genjang = tk.Label(tab_jajar_genjang, text="Luas = ...", bg="#EAF7FF")
hasil_jajar_genjang.grid(row=4, column=1, sticky="w")

tk.Label(
    tab_jajar_genjang,
    text="--- Invers: Cari Tinggi dari Luas & Alas ---",
    font=("Arial", 9, "bold"),
    fg="#168AAD",
    bg="#EAF7FF",
).grid(row=5, column=0, columnspan=3, pady=8)
tk.Label(tab_jajar_genjang, text="Masukkan Luas:", bg="#EAF7FF").grid(
    row=6, column=1, sticky="w", padx=5
)
entry_inv_l_jg = tk.Entry(tab_jajar_genjang)
entry_inv_l_jg.grid(row=6, column=2, padx=5, pady=3)
tk.Label(tab_jajar_genjang, text="Masukkan Alas:", bg="#EAF7FF").grid(
    row=7, column=1, sticky="w", padx=5
)
entry_inv_l_jg_a = tk.Entry(tab_jajar_genjang)
entry_inv_l_jg_a.grid(row=7, column=2, padx=5, pady=3)
tk.Button(
    tab_jajar_genjang,
    text="Hitung Invers (Tinggi)",
    command=invers_jajar_genjang,
).grid(row=8, column=2, pady=3, sticky="e")
hasil_inv_jg = tk.Label(tab_jajar_genjang, text="Tinggi = ...", bg="#EAF7FF")
hasil_inv_jg.grid(row=8, column=1, sticky="w")


# Tombol Kembali
tk.Button(
    window,
    text="Kembali Ke Menu",
    font=("Arial", 11, "bold"),
    bg="red",
    fg="white",
    width=25,
    command=kembali,
).pack(pady=10)
window.mainloop()