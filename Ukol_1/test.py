import unittest
from ukol_1 import vypocet_bmi, kategorie_bmi, soucet_sudych, pocet_kroku_collatz


class TestUkol1(unittest.TestCase):

    # -------------------------------------------------------------
    # 1. Testy pro funkci: vypocet_bmi
    # -------------------------------------------------------------
    def test_vypocet_bmi_normal(self):
        self.assertAlmostEqual(vypocet_bmi(75.0, 1.80), 23.15, places=2)
        self.assertAlmostEqual(vypocet_bmi(60.0, 1.65), 22.04, places=2)
        self.assertAlmostEqual(vypocet_bmi(90.0, 1.75), 29.39, places=2)
        self.assertAlmostEqual(vypocet_bmi(100.0, 2.00), 25.00, places=2)

    def test_vypocet_bmi_neplatne_vstupy(self):
        self.assertEqual(vypocet_bmi(0.0, 1.80), 0.0)
        self.assertEqual(vypocet_bmi(70.0, 0.0), 0.0)
        self.assertEqual(vypocet_bmi(-80.0, 1.80), 0.0)
        self.assertEqual(vypocet_bmi(80.0, -1.80), 0.0)

    # -------------------------------------------------------------
    # 2. Testy pro funkci: kategorie_bmi
    # -------------------------------------------------------------
    def test_kategorie_bmi_podvaha(self):
        self.assertEqual(kategorie_bmi(16.0), "podvaha")
        self.assertEqual(kategorie_bmi(18.4), "podvaha")

    def test_kategorie_bmi_normalni(self):
        self.assertEqual(kategorie_bmi(18.5), "normalni")
        self.assertEqual(kategorie_bmi(22.0), "normalni")
        self.assertEqual(kategorie_bmi(24.9), "normalni")

    def test_kategorie_bmi_nadvaha(self):
        self.assertEqual(kategorie_bmi(25.0), "nadvaha")
        self.assertEqual(kategorie_bmi(27.5), "nadvaha")
        self.assertEqual(kategorie_bmi(29.9), "nadvaha")

    def test_kategorie_bmi_obezita(self):
        self.assertEqual(kategorie_bmi(30.0), "obezita")
        self.assertEqual(kategorie_bmi(35.5), "obezita")

    def test_kategorie_bmi_neplatne(self):
        self.assertEqual(kategorie_bmi(0.0), "neplatna hodnota")
        self.assertEqual(kategorie_bmi(-5.0), "neplatna hodnota")

    # -------------------------------------------------------------
    # 3. Testy pro funkci: soucet_sudych
    # -------------------------------------------------------------
    def test_soucet_sudych_kladne(self):
        self.assertEqual(soucet_sudych(1, 10), 30)
        self.assertEqual(soucet_sudych(2, 6), 12)
        self.assertEqual(soucet_sudych(1, 5), 6)

    def test_soucet_sudych_stejne_meze(self):
        self.assertEqual(soucet_sudych(4, 4), 4)
        self.assertEqual(soucet_sudych(5, 5), 0)

    def test_soucet_sudych_obracene_meze(self):
        self.assertEqual(soucet_sudych(10, 1), 0)

    def test_soucet_sudych_zaporna_cisla(self):
        self.assertEqual(soucet_sudych(-4, 2), -4)

    # -------------------------------------------------------------
    # 4. Testy pro funkci: pocet_kroku_collatz
    # -------------------------------------------------------------
    def test_collatz_zakladni(self):
        self.assertEqual(pocet_kroku_collatz(1), 0)
        self.assertEqual(pocet_kroku_collatz(2), 1)
        self.assertEqual(pocet_kroku_collatz(4), 2)
        self.assertEqual(pocet_kroku_collatz(6), 8)
        self.assertEqual(pocet_kroku_collatz(7), 16)

    def test_collatz_neplatne_a_hranicni(self):
        self.assertEqual(pocet_kroku_collatz(0), 0)
        self.assertEqual(pocet_kroku_collatz(-10), 0)


if __name__ == "__main__":
    unittest.main()
