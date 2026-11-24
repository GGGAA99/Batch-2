import time

class PerekamWaktu:
    def __enter__(self):
        self.mulai = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) :
        self.selesai = time.perf_counter()
        self.durasi = self.selesai - self.mulai 
        print(f"Blok kode selesai diekseskusi dalam {self.durasi:.6f} detik")

# contoh penggunaan :
with PerekamWaktu():
    # Maskukkan kode yang ingin diukur di sini 
    daftar_kata = [str(x) for x in range(2_000_000)]
    teks = ", ".join(daftar_kata)