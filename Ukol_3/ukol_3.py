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
        self.nazev: str = nazev
        self.autor: str = autor
        self.pocet_stran: int = pocet_stran
        self.cena: float = cena

        # TODO: Inicializujte atributy přes property settery pro zajištění validace
        pass

    @property
    def nazev(self) -> str:
        # TODO: Doplňte getter
        return self._nazev

    @nazev.setter
    def nazev(self, hodnota: str) -> None:
        # TODO: Ověřte, že hodnota je neprázdný řetězec po oříznutí mezer (.strip()).
        # Pokud je prázdný, vyvolejte ValueError("Název nesmí být prázdný.")
        hodnota = hodnota.strip()
        
        if hodnota == "":
            raise ValueError("Název nesmí být prázdný.")
        self._nazev = hodnota

    @property
    def autor(self) -> str:
        # TODO: Doplňte getter
        return self._autor

    @autor.setter
    def autor(self, hodnota: str) -> None:
        # TODO: Ověřte, že hodnota je neprázdný řetězec po oříznutí mezer (.strip()).
        # Pokud je prázdný, vyvolejte ValueError("Autor nesmí být prázdný.")
        hodnota = hodnota.strip()
        if hodnota == "":
            raise ValueError("Autor nesmí být prázdný.")
        self._autor = hodnota

    @property
    def pocet_stran(self) -> int:
        # TODO: Doplňte getter
        return self._pocet_stran

    @pocet_stran.setter
    def pocet_stran(self, hodnota: int) -> None:
        # TODO: Ověřte, že hodnota je > 0.
        # Pokud ne, vyvolejte ValueError("Počet stran musí být kladné číslo.")
        if hodnota > 0:
            self._pocet_stran = hodnota
        else:
            raise ValueError("Počet stran musí být kladné číslo.")

    @property
    def cena(self) -> float:
        # TODO: Doplňte getter
        return self._cena

    @cena.setter
    def cena(self, hodnota: float) -> None:
        # TODO: Ověřte, že hodnota je >= 0.
        # Pokud ne, vyvolejte ValueError("Cena nesmí být záporná.")
        if hodnota >=0:
            self._cena = hodnota
        else:
            raise ValueError("Cena nesmí být záporná.")


    def sleva(self, procento: float) -> None:
        """
        Sníží cenu knihy o zadané procento (0 až 100).
        Výslednou cenu zaokrouhlete na 2 desetinná místa pomocí round(..., 2).
        Pokud procento není v rozsahu 0 až 100, vyvolejte ValueError("Sleva musí být v rozmezí 0 až 100 %.").
        """
        # TODO: Doplňte implementaci
        if 0<=procento<=100:
            self._cena = self._cena - ((self._cena/100)*procento)
            self._cena = round(self._cena,2)
        else:
            raise ValueError("Sleva musí být v rozmezí 0 až 100 %.")
        

    def __str__(self) -> str:
        """
        Vrátí textovou reprezentaci ve formátu:
        "{nazev} ({autor}) - {pocet_stran} str., {cena} Kč"
        Například: "1984 (George Orwell) - 328 str., 299.0 Kč"
        """
        # TODO: Doplňte implementaci
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
        self.nazev: str = nazev
        self.cena_za_kus: float = cena_za_kus
        self.pocet_kusu: int = pocet_kusu

        # TODO: Inicializujte atributy přes settery s validací
        pass

    @property
    def kod(self) -> str:
        """Vrátí kód položky (pouze pro čtení)."""
        return self._kod

    @property
    def nazev(self) -> str:
        return self._nazev

    @nazev.setter
    def nazev(self, hodnota: str) -> None:
        # TODO: Ověřte, že hodnota je neprázdný řetězec po oříznutí mezer.
        # Pokud je prázdný, vyvolejte ValueError("Název nesmí být prázdný.")
        hodnota = hodnota.strip()
        if hodnota == "":
            raise ValueError("Název nesmí být prázdný.")
        self._nazev = hodnota

    @property
    def cena_za_kus(self) -> float:
        return self._cena_za_kus

    @cena_za_kus.setter
    def cena_za_kus(self, hodnota: float) -> None:
        # TODO: Ověřte, že cena je >= 0.
        # Pokud ne, vyvolejte ValueError("Cena za kus nesmí být záporná.")
        if hodnota<0:
            raise ValueError("Cena za kus nesmí být záporná.")
        self._cena_za_kus = hodnota

    @property
    def pocet_kusu(self) -> int:
        return self._pocet_kusu

    @pocet_kusu.setter
    def pocet_kusu(self, hodnota: int) -> None:
        # TODO: Ověřte, že počet kusů je >= 0.
        # Pokud ne, vyvolejte ValueError("Počet kusů nesmí být záporný.")

        if hodnota<0:
            raise ValueError("Počet kusů nesmí být záporný.")
        else:
            self._pocet_kusu = hodnota
        

    @property
    def hodnota_zasob(self) -> float:
        """
        Vypočítaná vlastnost (pouze pro čtení): celková cena všech kusů na skladě (cena_za_kus * pocet_kusu).
        Zaokrouhlete na 2 desetinná místa.
        """
        # TODO: Doplňte výpočet
        hodnota = round(self._pocet_kusu*self._cena_za_kus,2)
        return hodnota

    def prijem(self, pocet: int) -> None:
        """
        Přičte zadaný počet kusů na sklad.
        Pokud je pocet <= 0, vyvolejte ValueError("Počet kusů pro příjem musí být kladný.").
        """
        # TODO: Doplňte implementaci
        if pocet<=0:
            raise ValueError("Počet kusů pro příjem musí být kladný.")
        else:
            self._pocet_kusu+=pocet

    def vydej(self, pocet: int) -> bool:
        """
        Odečte zadaný počet kusů ze skladu, pokud je jich dostatek.
        Pokud je pocet <= 0, vyvolejte ValueError("Počet kusů pro výdej musí být kladný.").
        Pokud je na skladě dostatek kusů, odečte je a vrátí True.
        Pokud dostatek kusů není, počet kusů se nezmění a metoda vrátí False.
        """
        # TODO: Doplňte implementaci
        if 0>=pocet:
            raise ValueError("Počet kusů pro výdej musí být kladný.")
        elif self._pocet_kusu>=pocet:
            self._pocet_kusu-=pocet
            return True
        elif self._pocet_kusu<pocet:
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
        self.jmeno: str = jmeno
        self.rocnik: int = rocnik
        self._znamky: list[int] = []

        # TODO: Inicializujte jmeno a rocnik přes property settery

    @property
    def jmeno(self) -> str:
        return self._jmeno

    @jmeno.setter
    def jmeno(self, hodnota: str) -> None:
        # TODO: Ověřte, že jméno je neprázdný řetězec po oříznutí mezer.
        # Pokud je prázdný, vyvolejte ValueError("Jméno studenta nesmí být prázdné.")
        hodnota = hodnota.strip()
        if hodnota == "":
            raise ValueError("Jméno studenta nesmí být prázdné.")
        self._jmeno = hodnota

    @property
    def rocnik(self) -> int:
        return self._rocnik

    @rocnik.setter
    def rocnik(self, hodnota: int) -> None:
        # TODO: Ověřte, že ročník je v rozsahu 1 až 5 (včetně).
        # Pokud ne, vyvolejte ValueError("Neplatný ročník (povolené hodnoty 1-5).")
        if 1>hodnota or hodnota>5:
            raise ValueError("Neplatný ročník (povolené hodnoty 1-5).")
        self._rocnik = hodnota


    @property
    def znamky(self) -> list[int]:
        """
        Vrátí kopii seznamu známek (aby vnější kód nemohl přímo měnit vnitřní seznam).
        """
        # TODO: Vraťte kopii self._znamky
        return list(self._znamky)

    def pridej_znamku(self, znamka: int) -> None:
        """
        Přidá novou známku do seznamu studenta.
        Známka musí být celé číslo v rozsahu 1 až 5.
        Pokud hodnota není v rozsahu 1 až 5, vyvolejte ValueError("Známka musí být v rozsahu 1 až 5.").
        """
        # TODO: Doplňte validaci a přidání známky
        if znamka<1 or znamka>5:
            raise ValueError("Známka musí být v rozsahu 1 až 5.")
        else:
            self._znamky.append(znamka)

    @property
    def prumer(self) -> float:
        """
        Vypočítaná vlastnost: aritmetický průměr všech známek zaokrouhlený na 2 desetinná místa.
        Pokud student nemá žádné známky, vrátí 0.0.
        """
        # TODO: Doplňte výpočet průměru
        celkem:float = 0
        for znamka in self._znamky:
            celkem+=znamka
        if celkem == 0:
            return 0.0
        else:
            return celkem/len(self._znamky)

    @property
    def prospel(self) -> bool:
        """
        Vypočítaná vlastnost:
        - Pokud student nemá žádné známky, vrátí True.
        - Pokud má alespoň jednu známku 5, vrátí False.
        - Pokud je jeho průměr <= 3.0 (a nemá 5), vrátí True.
        - Jinak (průměr > 3.0) vrátí False.
        """
        # TODO: Doplňte logiku prospěchu
        prospel:bool = True

        for i in self._znamky:
            if i == 5:
                prospel = False

        if self.prumer<=3.0 and prospel:
            return True
        elif self.prumer>3.0 or prospel:
            return False
