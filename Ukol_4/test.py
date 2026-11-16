import argparse
import contextlib
import io
import unittest

from ukol_4 import (
    ExpresniZasilka,
    NeplatnyKodZasilkyError,
    StandardniZasilka,
    Zasilka,
    over_kladne_argumenty,
    over_kod_zasilky,
    vytvor_parser,
    vytvor_zasilku_z_argumentu,
)


class TestUkol4(unittest.TestCase):

    # -------------------------------------------------------------
    # 1. Testy pro: NeplatnyKodZasilkyError a over_kod_zasilky
    # -------------------------------------------------------------
    def test_kod_platny_standardni(self):
        self.assertEqual(
            over_kod_zasilky("CZ-123456-STD"),
            {"zeme": "CZ", "cislo": "123456", "typ": "STD"},
        )

    def test_kod_platny_expresni(self):
        self.assertEqual(
            over_kod_zasilky("SK-987654-EXP"),
            {"zeme": "SK", "cislo": "987654", "typ": "EXP"},
        )

    def test_kod_platny_nulove_cislo(self):
        self.assertEqual(
            over_kod_zasilky("DE-000001-STD"),
            {"zeme": "DE", "cislo": "000001", "typ": "STD"},
        )

    def test_kod_platny_ruzne_zeme(self):
        for kod, zeme in (("PL-111111-STD", "PL"), ("DE-222222-EXP", "DE")):
            with self.subTest(kod=kod):
                self.assertEqual(over_kod_zasilky(kod)["zeme"], zeme)

    def test_kod_neplatny_chybi_pomlcky(self):
        with self.assertRaises(NeplatnyKodZasilkyError):
            over_kod_zasilky("CZ123456STD")
        with self.assertRaises(NeplatnyKodZasilkyError):
            over_kod_zasilky("CZ-123456STD")

    def test_kod_neplatna_mala_pismena(self):
        with self.assertRaises(NeplatnyKodZasilkyError):
            over_kod_zasilky("cz-123456-std")
        with self.assertRaises(NeplatnyKodZasilkyError):
            over_kod_zasilky("Cz-123456-STD")

    def test_kod_neplatny_pocet_cislic(self):
        with self.assertRaises(NeplatnyKodZasilkyError):
            over_kod_zasilky("CZ-12345-STD")
        with self.assertRaises(NeplatnyKodZasilkyError):
            over_kod_zasilky("CZ-1234567-STD")

    def test_kod_neplatny_suffix(self):
        with self.assertRaises(NeplatnyKodZasilkyError):
            over_kod_zasilky("CZ-123456-ST")
        with self.assertRaises(NeplatnyKodZasilkyError):
            over_kod_zasilky("CZ-123456-STDX")

    def test_kod_neplatny_prazdny_ci_jiny_text(self):
        for kod in ("", "   ", "abc", "CZ-123456-STD navic", "123456"):
            with self.subTest(kod=kod):
                with self.assertRaises(NeplatnyKodZasilkyError):
                    over_kod_zasilky(kod)

    def test_kod_je_potomek_exception(self):
        self.assertTrue(issubclass(NeplatnyKodZasilkyError, Exception))

    # -------------------------------------------------------------
    # 2. Testy pro dekorátor: over_kladne_argumenty
    # -------------------------------------------------------------
    def test_dekorator_kladne_argumenty_projde(self):
        @over_kladne_argumenty
        def secti(a, b):
            return a + b

        self.assertEqual(secti(2, 3), 5)
        self.assertEqual(secti(1.5, 2.5), 4.0)
        self.assertEqual(secti(a=10, b=20), 30)
        self.assertEqual(secti(2, b=3.5), 5.5)

    def test_dekorator_vraci_navratovou_hodnotu(self):
        @over_kladne_argumenty
        def vynasob(a, b):
            return a * b

        self.assertEqual(vynasob(3, 4), 12)

    def test_dekorator_zaporny_pozicni_argument(self):
        @over_kladne_argumenty
        def funkce(a, b):
            return a + b

        with self.assertRaises(ValueError):
            funkce(-1, 5)

    def test_dekorator_nulovy_argument(self):
        @over_kladne_argumenty
        def funkce(a, b):
            return a + b

        with self.assertRaises(ValueError):
            funkce(0, 5)
        with self.assertRaises(ValueError):
            funkce(0.0, 5.0)

    def test_dekorator_zaporny_klicovy_argument(self):
        @over_kladne_argumenty
        def funkce(a, b):
            return a + b

        with self.assertRaises(ValueError):
            funkce(a=1, b=-2.5)
        with self.assertRaises(ValueError):
            funkce(1, b=0)

    def test_dekorator_chybova_zprava(self):
        @over_kladne_argumenty
        def funkce(a):
            return a

        with self.assertRaises(ValueError) as ctx:
            funkce(-5)
        self.assertEqual(str(ctx.exception), "Číselný argument musí být kladný.")

    def test_dekorator_ignoruje_neciselne_argumenty(self):
        @over_kladne_argumenty
        def pozdrav(jmeno, vek):
            return f"{jmeno} ({vek})"

        self.assertEqual(pozdrav("Jan", 20), "Jan (20)")
        self.assertEqual(pozdrav("Eva", 1), "Eva (1)")
        self.assertEqual(pozdrav("Bez čísla", "text"), "Bez čísla (text)")

    def test_dekorator_funkce_bez_argumentu(self):
        @over_kladne_argumenty
        def konstantni():
            return 42

        self.assertEqual(konstantni(), 42)

    def test_dekorator_zachovava_jmeno_a_docstring(self):
        @over_kladne_argumenty
        def puvodni_funkce(hodnota):
            """Toto je docstring původní funkce."""
            return hodnota

        self.assertEqual(puvodni_funkce.__name__, "puvodni_funkce")
        self.assertEqual(puvodni_funkce.__doc__, "Toto je docstring původní funkce.")

    # -------------------------------------------------------------
    # 3. Testy pro abstraktní třídu: Zasilka
    # -------------------------------------------------------------
    def test_zasilka_je_abstraktni(self):
        with self.assertRaises(TypeError):
            Zasilka("CZ-123456-STD", 2.5)

    def test_zasilka_ma_abstraktni_metodu(self):
        self.assertIn("spocitej_cenu", Zasilka.__abstractmethods__)

    # -------------------------------------------------------------
    # 4. Testy pro: StandardniZasilka
    # -------------------------------------------------------------
    def test_standardni_platne_vytvoreni(self):
        z = StandardniZasilka("CZ-123456-STD", 2.5)
        self.assertEqual(z.kod, "CZ-123456-STD")
        self.assertEqual(z.hmotnost_kg, 2.5)
        self.assertIsInstance(z, Zasilka)

    def test_standardni_oriznuti_kodu(self):
        z = StandardniZasilka("  SK-987654-EXP  ", 1.0)
        self.assertEqual(z.kod, "SK-987654-EXP")

    def test_standardni_cena(self):
        self.assertEqual(StandardniZasilka("CZ-123456-STD", 2.5).spocitej_cenu(), 97.5)
        self.assertEqual(StandardniZasilka("CZ-123456-STD", 1.0).spocitej_cenu(), 75.0)
        self.assertEqual(StandardniZasilka("CZ-123456-STD", 10.0).spocitej_cenu(), 210.0)

    def test_standardni_neplatny_kod(self):
        with self.assertRaises(ValueError):
            StandardniZasilka("", 2.5)
        with self.assertRaises(ValueError):
            StandardniZasilka("   \t ", 2.5)

    def test_standardni_neplatna_hmotnost(self):
        with self.assertRaises(ValueError):
            StandardniZasilka("CZ-123456-STD", 0)
        with self.assertRaises(ValueError):
            StandardniZasilka("CZ-123456-STD", -1.5)

    # -------------------------------------------------------------
    # 5. Testy pro: ExpresniZasilka
    # -------------------------------------------------------------
    def test_expresni_platne_vytvoreni(self):
        z = ExpresniZasilka("SK-987654-EXP", 3.0)
        self.assertEqual(z.kod, "SK-987654-EXP")
        self.assertEqual(z.hmotnost_kg, 3.0)
        self.assertIsInstance(z, Zasilka)

    def test_expresni_vychozi_priplatek(self):
        z = ExpresniZasilka("SK-987654-EXP", 2.5)
        self.assertEqual(z.priplatek, 100.0)
        self.assertEqual(z.spocitej_cenu(), 222.5)

    def test_expresni_vlastni_priplatek(self):
        z = ExpresniZasilka("SK-987654-EXP", 2.5, priplatek=150.0)
        self.assertEqual(z.priplatek, 150.0)
        self.assertEqual(z.spocitej_cenu(), 272.5)

    def test_expresni_nulovy_priplatek(self):
        z = ExpresniZasilka("SK-987654-EXP", 2.0, priplatek=0.0)
        self.assertEqual(z.spocitej_cenu(), 110.0)

    def test_expresni_neplatny_priplatek(self):
        with self.assertRaises(ValueError):
            ExpresniZasilka("SK-987654-EXP", 2.5, priplatek=-10.0)

    def test_expresni_neplatny_kod_a_hmotnost(self):
        with self.assertRaises(ValueError):
            ExpresniZasilka("", 2.5)
        with self.assertRaises(ValueError):
            ExpresniZasilka("SK-987654-EXP", 0)

    # -------------------------------------------------------------
    # 6. Testy pro magické metody
    # -------------------------------------------------------------
    def test_str(self):
        z = StandardniZasilka("CZ-123456-STD", 2.5)
        self.assertEqual(str(z), "Zásilka CZ-123456-STD [97.50 Kč]")

        e = ExpresniZasilka("SK-987654-EXP", 2.5)
        self.assertEqual(str(e), "Zásilka SK-987654-EXP [222.50 Kč]")

    def test_repr(self):
        z = StandardniZasilka("CZ-123456-STD", 2.5)
        self.assertEqual(
            repr(z),
            "StandardniZasilka(kod='CZ-123456-STD', hmotnost_kg=2.5)",
        )

        e = ExpresniZasilka("SK-987654-EXP", 3.0)
        self.assertEqual(
            repr(e),
            "ExpresniZasilka(kod='SK-987654-EXP', hmotnost_kg=3.0)",
        )

    def test_eq_stejna_trida_a_kod(self):
        a = StandardniZasilka("CZ-123456-STD", 2.5)
        b = StandardniZasilka("CZ-123456-STD", 8.0)
        self.assertTrue(a == b)
        self.assertFalse(a != b)

    def test_eq_jiny_kod(self):
        a = StandardniZasilka("CZ-123456-STD", 2.5)
        b = StandardniZasilka("CZ-999999-STD", 2.5)
        self.assertFalse(a == b)

    def test_eq_jina_trida(self):
        a = StandardniZasilka("CZ-123456-STD", 2.5)
        b = ExpresniZasilka("CZ-123456-STD", 2.5)
        self.assertFalse(a == b)
        self.assertFalse(b == a)

    def test_eq_jiny_typ_objektu(self):
        a = StandardniZasilka("CZ-123456-STD", 2.5)
        self.assertFalse(a == "CZ-123456-STD")
        self.assertFalse(a == 42)

    def test_lt_podle_ceny(self):
        levna = StandardniZasilka("CZ-111111-STD", 1.0)    # 75.0
        draha = StandardniZasilka("CZ-222222-STD", 10.0)   # 210.0
        self.assertTrue(levna < draha)
        self.assertFalse(draha < levna)

    def test_lt_razeni_seznamu(self):
        z1 = ExpresniZasilka("SK-987654-EXP", 2.5)          # 222.5
        z2 = StandardniZasilka("CZ-123456-STD", 2.5)        # 97.5
        z3 = StandardniZasilka("DE-000001-STD", 10.0)       # 210.0

        serazene = sorted([z1, z2, z3])
        self.assertEqual(serazene, [z2, z3, z1])
        self.assertIs(serazene[0], z2)

    def test_add_soucet_cen(self):
        a = StandardniZasilka("CZ-123456-STD", 2.5)   # 97.5
        b = ExpresniZasilka("SK-987654-EXP", 2.5)     # 222.5
        self.assertEqual(a + b, 320.0)
        self.assertEqual(b + a, 320.0)

    def test_add_stejne_zasilky(self):
        a = StandardniZasilka("CZ-123456-STD", 1.0)
        self.assertEqual(a + a, 150.0)

    # -------------------------------------------------------------
    # 7. Testy pro argparse
    # -------------------------------------------------------------
    def test_parser_vytvoreni(self):
        parser = vytvor_parser()
        self.assertIsInstance(parser, argparse.ArgumentParser)

    def test_parser_pozicni_argumenty(self):
        parser = vytvor_parser()
        args = parser.parse_args(["CZ-123456-STD", "2.5"])

        self.assertEqual(args.kod, "CZ-123456-STD")
        self.assertEqual(args.hmotnost, 2.5)
        self.assertEqual(args.typ, "standard")
        self.assertEqual(args.priplatek, 100.0)

        zasilka = vytvor_zasilku_z_argumentu(args)
        self.assertIsInstance(zasilka, StandardniZasilka)
        self.assertEqual(zasilka.kod, "CZ-123456-STD")
        self.assertEqual(zasilka.hmotnost_kg, 2.5)
        self.assertEqual(zasilka.spocitej_cenu(), 97.5)

    def test_parser_expresni_dlouhe_prepinace(self):
        parser = vytvor_parser()
        args = parser.parse_args(
            ["SK-987654-EXP", "3.0", "--typ", "expres", "--priplatek", "150.0"]
        )

        zasilka = vytvor_zasilku_z_argumentu(args)
        self.assertIsInstance(zasilka, ExpresniZasilka)
        self.assertEqual(zasilka.kod, "SK-987654-EXP")
        self.assertEqual(zasilka.hmotnost_kg, 3.0)
        self.assertEqual(zasilka.priplatek, 150.0)
        self.assertEqual(zasilka.spocitej_cenu(), 285.0)

    def test_parser_expresni_kratke_prepinace(self):
        parser = vytvor_parser()
        args = parser.parse_args(["DE-000001-STD", "1.0", "-t", "expres", "-p", "50"])

        zasilka = vytvor_zasilku_z_argumentu(args)
        self.assertIsInstance(zasilka, ExpresniZasilka)
        self.assertEqual(zasilka.priplatek, 50.0)
        self.assertEqual(zasilka.spocitej_cenu(), 135.0)

    def test_parser_vychozi_priplatek_u_expresu(self):
        parser = vytvor_parser()
        args = parser.parse_args(["CZ-123456-STD", "2.0", "-t", "expres"])

        zasilka = vytvor_zasilku_z_argumentu(args)
        self.assertIsInstance(zasilka, ExpresniZasilka)
        self.assertEqual(zasilka.priplatek, 100.0)

    def test_parser_neplatny_typ(self):
        parser = vytvor_parser()
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                parser.parse_args(["CZ-123456-STD", "2.5", "--typ", "kurýr"])


if __name__ == "__main__":
    unittest.main()
