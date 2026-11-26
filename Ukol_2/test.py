import unittest
from ukol_2 import extrahuj_hashtagy, porovnej_zajmy, katalog_knih, statistika_textu


class TestUkol2(unittest.TestCase):

    # -------------------------------------------------------------
    # 1. Testy pro funkci: extrahuj_hashtagy
    # -------------------------------------------------------------
    def test_extrahuj_hashtagy_zakladni(self):
        text = "Dnes se učím #Python a #git!"
        self.assertEqual(extrahuj_hashtagy(text), {"python", "git"})

    def test_extrahuj_hashtagy_velka_a_mala_pismena(self):
        text = "Zkouška #Python #PYTHON #python a #PyThOn"
        self.assertEqual(extrahuj_hashtagy(text), {"python"})

    def test_extrahuj_hashtagy_interpunkce(self):
        text = "To je #super, #skvělé! #pecka? #ano: #ne; #top\""
        ocekavano = {"super", "skvělé", "pecka", "ano", "ne", "top"}
        self.assertEqual(extrahuj_hashtagy(text), ocekavano)

    def test_extrahuj_hashtagy_zadne_tagy(self):
        text = "Běžný text bez jakéhokoliv označení a křížků."
        self.assertEqual(extrahuj_hashtagy(text), set())

    def test_extrahuj_hashtagy_prazdny_text(self):
        self.assertEqual(extrahuj_hashtagy(""), set())
        self.assertEqual(extrahuj_hashtagy("   \n\t  "), set())

    def test_extrahuj_hashtagy_neplatne_krizky(self):
        text = "Samotný # a prázdný ## nebo #! není hashtag."
        self.assertEqual(extrahuj_hashtagy(text), set())

    # -------------------------------------------------------------
    # 2. Testy pro funkci: porovnej_zajmy
    # -------------------------------------------------------------
    def test_porovnej_zajmy_zakladni(self):
        a = {"python", "c++", "linux"}
        b = {"python", "sql", "git"}
        spolecne, pouze_a, pouze_b = porovnej_zajmy(a, b)
        self.assertEqual(spolecne, {"python"})
        self.assertEqual(pouze_a, {"c++", "linux"})
        self.assertEqual(pouze_b, {"sql", "git"})

    def test_porovnej_zajmy_disjunktni(self):
        a = {"python", "django"}
        b = {"c++", "unreal"}
        spolecne, pouze_a, pouze_b = porovnej_zajmy(a, b)
        self.assertEqual(spolecne, set())
        self.assertEqual(pouze_a, {"python", "django"})
        self.assertEqual(pouze_b, {"c++", "unreal"})

    def test_porovnej_zajmy_shodne(self):
        a = {"python", "git"}
        b = {"python", "git"}
        spolecne, pouze_a, pouze_b = porovnej_zajmy(a, b)
        self.assertEqual(spolecne, {"python", "git"})
        self.assertEqual(pouze_a, set())
        self.assertEqual(pouze_b, set())

    def test_porovnej_zajmy_prazdne(self):
        spolecne, pouze_a, pouze_b = porovnej_zajmy(set(), {"linux"})
        self.assertEqual(spolecne, set())
        self.assertEqual(pouze_a, set())
        self.assertEqual(pouze_b, {"linux"})

    # -------------------------------------------------------------
    # 3. Testy pro funkci: katalog_knih
    # -------------------------------------------------------------
    def test_katalog_knih_zakladni(self):
        knihy = [
            ("1984", "Sci-Fi", 1949),
            ("Pán prstenů", "Fantasy", 1954),
            ("Duna", "Sci-Fi", 1965),
            ("Hobit", "Fantasy", 1937)
        ]
        ocekavano = {
            "Sci-Fi": ["1984", "Duna"],
            "Fantasy": ["Pán prstenů", "Hobit"]
        }
        self.assertEqual(katalog_knih(knihy), ocekavano)

    def test_katalog_knih_jeden_zanr(self):
        knihy = [
            ("R.U.R.", "Drama", 1920),
            ("Bílá nemoc", "Drama", 1937)
        ]
        self.assertEqual(katalog_knih(knihy), {"Drama": ["R.U.R.", "Bílá nemoc"]})

    def test_katalog_knih_orezani_bilych_znaku(self):
        knihy = [
            ("Kniha A", " Detektivka ", 2000),
            ("Kniha B", "Detektivka", 2005)
        ]
        self.assertEqual(katalog_knih(knihy), {"Detektivka": ["Kniha A", "Kniha B"]})

    def test_katalog_knih_prazdny(self):
        self.assertEqual(katalog_knih([]), {})

    # -------------------------------------------------------------
    # 4. Testy pro funkci: statistika_textu
    # -------------------------------------------------------------
    def test_statistika_textu_zakladni(self):
        text = "Rychlá hnědá liška skáče přes líného psa."
        stats = statistika_textu(text)
        self.assertEqual(stats["pocet_slov"], 7)
        self.assertEqual(stats["pocet_unikatnich"], 7)
        self.assertEqual(stats["nejdelsi_slovo"], "rychlá")
        self.assertEqual(stats["cetnost_delek"], {6: 2, 5: 3, 4: 1, 3: 1})

    def test_statistika_textu_opakovana_slova(self):
        text = "Pes pes PES kočka!"
        stats = statistika_textu(text)
        self.assertEqual(stats["pocet_slov"], 4)
        self.assertEqual(stats["pocet_unikatnich"], 2)
        self.assertEqual(stats["nejdelsi_slovo"], "kočka")
        self.assertEqual(stats["cetnost_delek"], {3: 3, 5: 1})

    def test_statistika_textu_prazdny(self):
        ocekavano = {
            "pocet_slov": 0,
            "pocet_unikatnich": 0,
            "nejdelsi_slovo": "",
            "cetnost_delek": {}
        }
        self.assertEqual(statistika_textu(""), ocekavano)
        self.assertEqual(statistika_textu("   \n\t  "), ocekavano)

    def test_statistika_textu_pouze_interpunkce(self):
        ocekavano = {
            "pocet_slov": 0,
            "pocet_unikatnich": 0,
            "nejdelsi_slovo": "",
            "cetnost_delek": {}
        }
        self.assertEqual(statistika_textu("... ,,, !!! ???"), ocekavano)

    def test_statistika_textu_shodna_delka_nejdelsich(self):
        # Při shodě délek vybere první nalezené nejdelší slovo
        text = "auto kolo"
        stats = statistika_textu(text)
        self.assertEqual(stats["nejdelsi_slovo"], "auto")


if __name__ == "__main__":
    unittest.main()
