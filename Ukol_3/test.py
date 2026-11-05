import unittest
from ukol_3 import Kniha, PolozkaSkladu, Student


class TestUkol3(unittest.TestCase):

    # -------------------------------------------------------------
    # 1. Testy pro třídu: Kniha
    # -------------------------------------------------------------
    def test_kniha_platne_vytvoreni(self):
        k = Kniha("1984", "George Orwell", 328, 299.0)
        self.assertEqual(k.nazev, "1984")
        self.assertEqual(k.autor, "George Orwell")
        self.assertEqual(k.pocet_stran, 328)
        self.assertEqual(k.cena, 299.0)

    def test_kniha_oriznuti_mezer(self):
        k = Kniha("  Duna  ", "  Frank Herbert  ", 500, 350.0)
        self.assertEqual(k.nazev, "Duna")
        self.assertEqual(k.autor, "Frank Herbert")

    def test_kniha_neplatny_nazev(self):
        with self.assertRaises(ValueError):
            Kniha("", "Karel Čapek", 200, 150.0)
        with self.assertRaises(ValueError):
            Kniha("   ", "Karel Čapek", 200, 150.0)

    def test_kniha_neplatny_autor(self):
        with self.assertRaises(ValueError):
            Kniha("R.U.R.", "", 150, 120.0)
        with self.assertRaises(ValueError):
            Kniha("R.U.R.", "   \t ", 150, 120.0)

    def test_kniha_neplatny_pocet_stran(self):
        with self.assertRaises(ValueError):
            Kniha("Test", "Autor", 0, 100.0)
        with self.assertRaises(ValueError):
            Kniha("Test", "Autor", -50, 100.0)

    def test_kniha_neplatna_cena(self):
        with self.assertRaises(ValueError):
            Kniha("Test", "Autor", 100, -10.0)
        k = Kniha("Zdarma kniha", "Autor", 50, 0.0)
        self.assertEqual(k.cena, 0.0)

    def test_kniha_settery(self):
        k = Kniha("Původní název", "Původní autor", 100, 200.0)
        k.nazev = "Nový název"
        k.autor = "Nový autor"
        k.pocet_stran = 150
        k.cena = 250.0
        self.assertEqual(k.nazev, "Nový název")
        self.assertEqual(k.autor, "Nový autor")
        self.assertEqual(k.pocet_stran, 150)
        self.assertEqual(k.cena, 250.0)

        with self.assertRaises(ValueError):
            k.nazev = "  "
        with self.assertRaises(ValueError):
            k.cena = -1.0

    def test_kniha_sleva(self):
        k = Kniha("Hobit", "J.R.R. Tolkien", 300, 400.0)
        k.sleva(25.0)
        self.assertEqual(k.cena, 300.0)

        k.sleva(0.0)
        self.assertEqual(k.cena, 300.0)

        k.sleva(50.0)
        self.assertEqual(k.cena, 150.0)

    def test_kniha_neplatna_sleva(self):
        k = Kniha("Hobit", "J.R.R. Tolkien", 300, 400.0)
        with self.assertRaises(ValueError):
            k.sleva(-5.0)
        with self.assertRaises(ValueError):
            k.sleva(105.0)

    def test_kniha_str(self):
        k = Kniha("1984", "George Orwell", 328, 299.0)
        self.assertEqual(str(k), "1984 (George Orwell) - 328 str., 299.0 Kč")

    # -------------------------------------------------------------
    # 2. Testy pro třídu: PolozkaSkladu
    # -------------------------------------------------------------
    def test_sklad_platne_vytvoreni(self):
        p = PolozkaSkladu("A101", "Rezistor 10k", 2.5, 100)
        self.assertEqual(p.kod, "A101")
        self.assertEqual(p.nazev, "Rezistor 10k")
        self.assertEqual(p.cena_za_kus, 2.5)
        self.assertEqual(p.pocet_kusu, 100)

    def test_sklad_vychozi_pocet_kusu(self):
        p = PolozkaSkladu("B202", "Kondenzator", 12.0)
        self.assertEqual(p.pocet_kusu, 0)

    def test_sklad_kod_neměnny(self):
        p = PolozkaSkladu("A101", "Test", 10.0, 5)
        with self.assertRaises(AttributeError):
            p.kod = "A999"

    def test_sklad_neplatna_cena_a_pocet(self):
        with self.assertRaises(ValueError):
            PolozkaSkladu("A1", "Test", -1.0, 5)
        with self.assertRaises(ValueError):
            PolozkaSkladu("A1", "Test", 10.0, -2)

    def test_sklad_hodnota_zasob(self):
        p = PolozkaSkladu("A101", "Rezistor", 2.5, 150)
        self.assertEqual(p.hodnota_zasob, 375.0)

        p.pocet_kusu = 0
        self.assertEqual(p.hodnota_zasob, 0.0)

    def test_sklad_prijem(self):
        p = PolozkaSkladu("A101", "Rezistor", 2.0, 50)
        p.prijem(30)
        self.assertEqual(p.pocet_kusu, 80)

        with self.assertRaises(ValueError):
            p.prijem(0)
        with self.assertRaises(ValueError):
            p.prijem(-10)

    def test_sklad_vydej(self):
        p = PolozkaSkladu("A101", "Rezistor", 2.0, 50)
        uspech = p.vydej(20)
        self.assertTrue(uspech)
        self.assertEqual(p.pocet_kusu, 30)

        uspech = p.vydej(30)
        self.assertTrue(uspech)
        self.assertEqual(p.pocet_kusu, 0)

        uspech = p.vydej(5)
        self.assertFalse(uspech)
        self.assertEqual(p.pocet_kusu, 0)

        with self.assertRaises(ValueError):
            p.vydej(0)
        with self.assertRaises(ValueError):
            p.vydej(-5)

    # -------------------------------------------------------------
    # 3. Testy pro třídu: Student
    # -------------------------------------------------------------
    def test_student_platne_vytvoreni(self):
        s = Student("Jan Novák", 2)
        self.assertEqual(s.jmeno, "Jan Novák")
        self.assertEqual(s.rocnik, 2)
        self.assertEqual(s.znamky, [])
        self.assertEqual(s.prumer, 0.0)
        self.assertTrue(s.prospel)

    def test_student_neplatne_jmeno(self):
        with self.assertRaises(ValueError):
            Student("", 1)
        with self.assertRaises(ValueError):
            Student("   \n ", 1)

    def test_student_neplatny_rocnik(self):
        with self.assertRaises(ValueError):
            Student("Petr", 0)
        with self.assertRaises(ValueError):
            Student("Petr", 6)
        with self.assertRaises(ValueError):
            Student("Petr", -1)

    def test_student_zapouzdreni_znamek(self):
        s = Student("Eva", 1)
        s.pridej_znamku(1)
        vnejsi_seznam = s.znamky
        vnejsi_seznam.append(5)
        self.assertEqual(s.znamky, [1])

    def test_student_pridani_znamek_a_prumer(self):
        s = Student("Lucie", 3)
        s.pridej_znamku(1)
        s.pridej_znamku(2)
        s.pridej_znamku(3)
        self.assertEqual(s.znamky, [1, 2, 3])
        self.assertEqual(s.prumer, 2.0)

        s.pridej_znamku(2)
        self.assertEqual(s.prumer, 2.0)

    def test_student_neplatne_znamky(self):
        s = Student("Karel", 2)
        with self.assertRaises(ValueError):
            s.pridej_znamku(0)
        with self.assertRaises(ValueError):
            s.pridej_znamku(6)
        with self.assertRaises(ValueError):
            s.pridej_znamku(-2)

    def test_student_prospel_uspesne(self):
        s = Student("Marek", 1)
        s.pridej_znamku(2)
        s.pridej_znamku(3)
        s.pridej_znamku(3)
        self.assertTrue(s.prospel)

    def test_student_neprospel_kvuli_petce(self):
        s = Student("Tomáš", 1)
        s.pridej_znamku(1)
        s.pridej_znamku(1)
        s.pridej_znamku(5)
        self.assertFalse(s.prospel)

    def test_student_neprospel_kvuli_prumeru(self):
        s = Student("Adam", 2)
        s.pridej_znamku(4)
        s.pridej_znamku(4)
        s.pridej_znamku(3)
        self.assertFalse(s.prospel)


if __name__ == "__main__":
    unittest.main()
