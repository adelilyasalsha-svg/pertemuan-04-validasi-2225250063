try:
    nilai_ujian = float(input("Masukkan nilai ujian: "))
    nilai_tugas = float(input("Masukkan nilai tugas: "))
    kehadiran = float(input("Masukkan persentase kehadiran: "))

    if nilai_ujian < 0 or nilai_ujian > 100:
        print("Error: nilai ujian harus berada pada rentang 0-100.")

    elif nilai_tugas < 0 or nilai_tugas > 100:
        print("Error: nilai tugas harus berada pada rentang 0-100.")

    elif kehadiran < 0 or kehadiran > 100:
        print("Error: persentase kehadiran harus berada pada rentang 0-100.")

    else:
        nilai_akhir = (0.6 * nilai_ujian) + (0.4 * nilai_tugas)

        if kehadiran < 80:
            print(f"Nilai akhir: {nilai_akhir:.2f}")
            print("Predikat: -")
            print("Status: Tidak memenuhi syarat kehadiran.")

        else:
            if nilai_akhir >= 85:
                predikat = "A"
                status = "Lulus"
            elif nilai_akhir >= 70:
                predikat = "B"
                status = "Lulus"
            elif nilai_akhir >= 60:
                predikat = "C"
                status = "Lulus"
            elif nilai_akhir >= 50:
                predikat = "D"
                status = "Belum lulus"
            else:
                predikat = "E"
                status = "Belum lulus"

            print(f"Nilai akhir: {nilai_akhir:.2f}")
            print("Predikat:", predikat)
            print("Status:", status)

except ValueError:
    print("Error: semua input harus berupa angka.")