import unittest
# Mengimpor fungsi dari file utama Anda
from travolta import hitung_finansial

class TestPerhitunganGajiTravolta(unittest.TestCase):

    def test_kasus_lembur_bisa_menabung(self):
        """Uji coba jam kerja di atas standar (52 jam): harus dapat lembur dan sisa positif"""
        jam_uji = 52
        pengeluaran = 600000
        gaji, sisa, status = hitung_finansial(jam_uji, pengeluaran)
        
        self.assertEqual(gaji, 870000.0)
        self.assertEqual(sisa, 270000.0)
        self.assertEqual(status, "bisa menabung")

    def test_kasus_standar_tidak_bisa_menabung(self):
        """Uji coba jam kerja tepat 40 jam: gaji pas dengan pengeluaran (sisa 0)"""
        jam_uji = 40
        pengeluaran = 600000
        gaji, sisa, status = hitung_finansial(jam_uji, pengeluaran)
        
        self.assertEqual(gaji, 600000.0)
        self.assertEqual(sisa, 0.0)
        self.assertEqual(status, "tidak bisa menabung")

    def test_kasus_kurang_cari_tambahan(self):
        """Uji coba jam kerja di bawah standar (30 jam): pemasukan defisit/minus"""
        jam_uji = 30
        pengeluaran = 600000
        gaji, sisa, status = hitung_finansial(jam_uji, pengeluaran)
        
        self.assertEqual(gaji, 450000.0)
        self.assertEqual(sisa, -150000.0)
        self.assertEqual(status, "cari tambahan")

    def test_input_negatif_harus_error(self):
        """Uji batas ekstrim (boundary/defensive): jam minus harus memicu ValueError"""
        with self.assertRaises(ValueError):
            hitung_finansial(-5, 600000)

if __name__ == "__main__":
    unittest.main()
