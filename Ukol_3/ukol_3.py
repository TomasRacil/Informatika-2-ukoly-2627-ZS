"""
Úkol 3: Objektově orientované programování – třídy, typové anotace a vlastnosti.

Vyplňte těla jednotlivých tříd a metod podle zadání v komentářích a v README.md.
Neměňte názvy tříd, metod ani jejich parametrů.
"""


class Kniha:
    """
    Třída reprezentující knihu.

    Atributy (chráněné):
        _nazev (str): Název knihy (nesmí být prázdný).
        _autor (str): Jméno autora (nesmí být prázdné).
        _pocet_stran (int): Počet stran knihy (musí být kladné číslo > 0).
        _cena (float): Cena knihy v Kč (musí být nezáporné číslo >= 0).
    """

    def __init__(self, nazev: str, autor: str, pocet_stran: int, cena: float) -> None:

        self._nazev: str = ""
        self._autor: str = ""
        self._pocet_stran: int = 1
        self._cena: float = 0.0

        self.nazev = nazev
        self.autor = autor
        self.pocet_stran = pocet_stran
        self.cena = cena

        # TODO: Inicializujte atributy přes property settery pro zajištění validace
        pass

    @property
    def nazev(self) -> str:
        # TODO: Doplňte getter
        return self._nazev

    @nazev.setter
    def nazev(self, novy_nazev: str) -> None:
        if not novy_nazev.strip():
            raise ValueError("Název nesmí být prázdný.")
        self._nazev = novy_nazev.strip()

    @property
    def autor(self) -> str:
        # TODO: Doplňte getter
        return self._autor

    @autor.setter
    def autor(self, novy_autor: str) -> None:
        if not novy_autor.strip():
            raise ValueError("Autor nesmí být prázdný.")
        self._autor = novy_autor.strip()

    @property
    def pocet_stran(self) -> int:
        # TODO: Doplňte getter
        return self._pocet_stran

    @pocet_stran.setter
    def pocet_stran(self, hodnota: int) -> None:
        if hodnota <= 0:
            raise ValueError("Počet stran musí být kladné číslo.")
        self._pocet_stran = hodnota

    @property
    def cena(self) -> float:
        # TODO: Doplňte getter
        return self._cena

    @cena.setter
    def cena(self, hodnota: float) -> None:
        if hodnota < 0:
            raise ValueError("Cena nesmí být záporná.")
        self._cena = hodnota

    def sleva(self, procento: float) -> None:
        if procento < 0 or procento > 100:
            raise ValueError("Sleva musí být v rozmezí 0 až 100 %.")

        self._cena = round(self._cena * (1 - procento / 100), 2)

    def __str__(self) -> str:
        return f"{self._nazev} ({self._autor}) - {self._pocet_stran} str., {self._cena} Kč"


class PolozkaSkladu:
    """
    Třída reprezentující položku na skladě.

    Atributy (chráněné):
        _kod (str): Jedinečný kód položky (neměnný, pouze pro čtení).
        _nazev (str): Název položky (nesmí být prázdný).
        _cena_za_kus (float): Cena za jeden kus v Kč (musí být >= 0).
        _pocet_kusu (int): Aktuální počet kusů na skladě (musí být >= 0).
    """

    def __init__(self, kod: str, nazev: str, cena_za_kus: float, pocet_kusu: int = 0) -> None:
        self._kod: str = kod
        self._nazev: str = ""
        self._cena_za_kus: float = 0.0
        self._pocet_kusu: int = 0

        self.nazev = nazev
        self.cena_za_kus = cena_za_kus
        self.pocet_kusu = pocet_kusu


    @property
    def kod(self) -> str:
        return self._kod

    @property
    def nazev(self) -> str:
        return self._nazev

    @nazev.setter
    def nazev(self, hodnota: str) -> None:
        if not hodnota.strip():
            raise ValueError("Název nesmí být prázdný.")
        self._nazev = hodnota

    @property
    def cena_za_kus(self) -> float:
        return self._cena_za_kus

    @cena_za_kus.setter
    def cena_za_kus(self, hodnota: float) -> None:
        if hodnota < 0:
            raise ValueError("Cena za kus nesmí být záporná.")
        self._cena_za_kus = hodnota

    @property
    def pocet_kusu(self) -> int:
        return self._pocet_kusu

    @pocet_kusu.setter
    def pocet_kusu(self, hodnota: int) -> None:
        if hodnota < 0:
            raise ValueError("Počet kusů nesmí být záporný.")
        self._pocet_kusu = hodnota

    @property
    def hodnota_zasob(self) -> float:
        return round(self._cena_za_kus * self._pocet_kusu, 2)

    def prijem(self, pocet: int) -> None:
        if pocet <= 0:
            raise ValueError("Počet kusů pro příjem musí být kladný.")

        self._pocet_kusu += pocet

    def vydej(self, pocet: int) -> bool:
        if pocet <= 0:
            raise ValueError("Počet kusů pro výdej musí být kladný.")

        if self._pocet_kusu >= pocet:
            self._pocet_kusu -= pocet
            return True

        return False

class Student:
    """
    Třída reprezentující studenta a jeho prospěch.

    Atributy (chráněné):
        _jmeno (str): Jméno studenta (nesmí být prázdné).
        _rocnik (int): Ročník studia (musí být v rozsahu 1 až 5).
        _znamky (list[int]): Seznam zapsaných známek (číselné hodnoty 1 až 5).
    """

    def __init__(self, jmeno: str, rocnik: int) -> None:
        self._jmeno: str = ""
        self._rocnik: int = 1
        self._znamky: list[int] = []

        self.jmeno = jmeno
        self.rocnik = rocnik

        

    @property
    def jmeno(self) -> str:
        return self._jmeno

    @jmeno.setter
    def jmeno(self, hodnota: str) -> None:
        if not hodnota.strip():
            raise ValueError("Jméno studenta nesmí být prázdné.")
        self._jmeno = hodnota.strip()

    @property
    def rocnik(self) -> int:
        return self._rocnik

    @rocnik.setter
    def rocnik(self, hodnota: int) -> None:
        if hodnota < 1 or hodnota > 5:
            raise ValueError("Neplatný ročník (povolené hodnoty 1-5).")
        self._rocnik = hodnota

    @property
    def znamky(self) -> list[int]:

        return list(self._znamky)

    def pridej_znamku(self, znamka: int) -> None:
        if znamka < 1 or znamka > 5:
            raise ValueError("Známka musí být v rozsahu 1 až 5.")
        self._znamky.append(znamka)

    @property
    def prumer(self) -> float:
        if len(self._znamky) == 0:
            return 0.0

        return round(sum(self._znamky) / len(self._znamky), 2)

    @property
    def prospel(self) -> bool:
        if len(self._znamky) == 0:
            return True

        if 5 in self._znamky:
            return False

        return self.prumer <= 3.0
