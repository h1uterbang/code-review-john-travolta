def hitung_finansial(jam_kerja, pengeluaran=600000):
    if jam_kerja < 0 or pengeluaran < 0:
        raise ValueError("Jam kerja dan pengeluaran tidak boleh negatif.")

    rate = 15000
    jam_normal = 40
    rate_lembur = 1.5 * rate

    # Perbaikan: 40 jam tarif normal + selisih jam lembur
    if jam_kerja > jam_normal:
        jam_lembur = jam_kerja - jam_normal
        gaji = (jam_normal * rate) + (jam_lembur * rate_lembur)
    else:
        gaji = jam_kerja * rate

    sisa = gaji - pengeluaran

    if sisa > 0:
        status = "bisa menabung"
    elif sisa == 0:
        status = "tidak bisa menabung"
    else:
        status = "cari tambahan"

    return gaji, sisa, status

if __name__ == "__main__":
    jam = 52
    gaji, sisa, status = hitung_finansial(jam)
    print(f"Gaji: Rp {gaji:,} | Sisa: Rp {sisa:,} | Status: {status}")
