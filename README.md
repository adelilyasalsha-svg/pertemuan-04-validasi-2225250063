# Pertemuan 04 Seleksi Multi-Kondisi dan Validasi Input

Nama: Adelilya Salsha
NIM: 2225250063
Kelas: 3B

## Tujuan

Mempelajari penggunaan seleksi multi-kondisi dengan if-elif-else serta validasi input menggunakan try-except ValueError.

## Cara Menjalankan

Jalankan program praktik dengan perintah:

python3 praktik/validasi_klasifikasi_nilai.py

## Tabel Keputusan

| Kondisi | Predikat | Status |
|---|---|---|
| Kehadiran < 80% | - | Tidak memenuhi syarat kehadiran |
| Nilai akhir >= 85 | A | Lulus |
| Nilai akhir >= 70 | B | Lulus |
| Nilai akhir >= 60 | C | Lulus |
| Nilai akhir >= 50 | D | Belum lulus |
| Nilai akhir < 50 | E | Belum lulus |

## Hasil Pengujian

| No | Nilai Ujian | Nilai Tugas | Kehadiran | Hasil |
|---|---:|---:|---:|---|
| 1 | 90 | 80 | 95 | 86.00, A, Lulus |
| 2 | 75 | 70 | 85 | 73.00, B, Lulus |
| 3 | 60 | 60 | 80 | 60.00, C, Lulus |
| 4 | 55 | 50 | 90 | 53.00, D, Belum lulus |
| 5 | 40 | 30 | 100 | 36.00, E, Belum lulus |
| 6 | 90 | 90 | 75 | Tidak memenuhi syarat kehadiran |
| 7 | 105 | 80 | 90 | Error: nilai ujian harus berada pada rentang 0-100 |
| 8 | 80 | -5 | 90 | Error: nilai tugas harus berada pada rentang 0-100 |
| 9 | 80 | 80 | abc | Error: semua input harus berupa angka |

## Refleksi

Pada pertemuan ini saya mempelajari penggunaan if-elif-else untuk membuat klasifikasi nilai. Saya juga mempelajari validasi input menggunakan try-except ValueError agar program dapat menangani input yang bukan angka. Selain itu, saya memahami bahwa validasi kehadiran harus dilakukan sebelum menentukan predikat nilai.