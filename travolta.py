def hitung_finansial(jam_kerja, pengeluaran=600000):
    rate = 15000

    # Bug: seluruh jam kerja dikali 1.5x lembur
    if jam_kerja > 40:
        gaji = jam_kerja * (1.5 * rate)
    else:
        gaji = jam_kerja * rate

    sisa = gaji - pengeluaran

    if sisa > 0:
        status = "bisa menabung"
    elif sisa < 0:
        status = "cari tambahan"
    else:
        status = "tidak bisa menabung"

    return gaji, sisa, status

if __name__ == "__main__":
    jam = 52
    gaji, sisa, status = hitung_finansial(jam)
    print(f"Gaji: {gaji}, Sisa: {sisa}, Status: {status}")
