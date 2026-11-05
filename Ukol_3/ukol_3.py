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
        if nazev.strip() == "":
            raise ValueError("Název knihy nesmí být prázdný.")
        self._nazev: str = nazev.strip()
        if autor.strip() == "":
            raise ValueError("Jméno autora nesmí být prázdné.")
        self._autor: str = autor.strip()
        if pocet_stran <=0:
            raise ValueError("Počet stran musí být kladné číslo > 0.")
        self._pocet_stran: int = pocet_stran
        if cena <0:
            raise ValueError("Cena musí být nezáporné číslo >= 0")
        self._cena: float = cena

        

    @property
    def nazev(self) -> str:
        
        return self._nazev

    @nazev.setter
    def nazev(self, hodnota: str) -> None:
        if not hodnota.strip():
            raise ValueError("Název nesmí být prázdný.")
        
        self._nazev = hodnota.strip()


    @property
    def autor(self) -> str:
        return self._autor

    @autor.setter
    def autor(self, hodnota: str) -> None:
        if not hodnota.strip():  
            raise ValueError("Autor nesmí být prázdný.")
                
        self._autor = hodnota.strip()
        

    @property
    def pocet_stran(self) -> int:
        return self._pocet_stran

    @pocet_stran.setter
    def pocet_stran(self, hodnota: int) -> None:
        if hodnota<=0:
            raise ValueError("Počet stran musí být kladné číslo.")
        self._pocet_stran = hodnota

    @property
    def cena(self) -> float:
        return self._cena

    @cena.setter
    def cena(self, hodnota: float) -> None:
        if hodnota<=0:
            raise ValueError("Cena nesmí být záporná.")
        self._cena = hodnota

    def sleva(self, procento: float) -> None:
        """
        Sníží cenu knihy o zadané procento (0 až 100).
        Výslednou cenu zaokrouhlete na 2 desetinná místa pomocí round(..., 2).
        Pokud procento není v rozsahu 0 až 100, vyvolejte ValueError("Sleva musí být v rozmezí 0 až 100 %.").
        """

        if not (0<=procento<=100):
                    raise ValueError("Sleva musí být v rozmezí 0 až 100 %.")
        self._cena = round(self._cena - (self._cena*(procento/100)),2)

    def __str__(self) -> str:
        """
        Vrátí textovou reprezentaci ve formátu:
        "{nazev} ({autor}) - {pocet_stran} str., {cena} Kč"
        Například: "1984 (George Orwell) - 328 str., 299.0 Kč"
        """
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
        if kod.strip() == "":
            raise ValueError("Kód nesmí být prázdný.")
        self._kod: str = kod.strip()
        if nazev.strip() == "":
            raise ValueError("Nazev nesmí být prázdný")
        self._nazev: str = nazev.strip()
        if cena_za_kus <0:
                raise ValueError("Cena musí být nezáporné číslo >= 0")
        self._cena_za_kus: float = cena_za_kus
        if pocet_kusu <0:
            raise ValueError("Počet kusů musí být >=0")
        self._pocet_kusu: int = pocet_kusu


        
                
    @property
    def kod(self) -> str:
        """Vrátí kód položky (pouze pro čtení)."""
        return self._kod

    @property
    def nazev(self) -> str:
        return self._nazev

    @nazev.setter
    def nazev(self, hodnota: str) -> None:
        if not hodnota.strip():  
                raise ValueError("Nazev nesmí být prázdný.")
                    
        self._nazev = hodnota.strip()

    @property
    def cena_za_kus(self) -> float:
        return self._cena_za_kus

    @cena_za_kus.setter
    def cena_za_kus(self, hodnota: float) -> None:
        if hodnota <0:
            raise ValueError("Cena za kus nesmí být záporná.")
        self._cena_za_kus = hodnota

    @property
    def pocet_kusu(self) -> int:
        return self._pocet_kusu

    @pocet_kusu.setter
    def pocet_kusu(self, hodnota: int) -> None:
        if hodnota <0:
            raise ValueError("Počet kusů nesmí být záporný.")
        self._pocet_kusu = hodnota

    @property
    def hodnota_zasob(self) -> float:
        """
        Vypočítaná vlastnost (pouze pro čtení): celková cena všech kusů na skladě (cena_za_kus * pocet_kusu).
        Zaokrouhlete na 2 desetinná místa.
        """
        return round(self._cena_za_kus * self._pocet_kusu,2)

    def prijem(self, pocet: int) -> None:
        """
        Přičte zadaný počet kusů na sklad.
        Pokud je pocet <= 0, vyvolejte ValueError("Počet kusů pro příjem musí být kladný.").
        """
        if pocet <=0:
            raise ValueError("Počet kusů pro příjem musí být kladný.")
        self._pocet_kusu += pocet

    def vydej(self, pocet: int) -> bool:
        """
        Odečte zadaný počet kusů ze skladu, pokud je jich dostatek.
        Pokud je pocet <= 0, vyvolejte ValueError("Počet kusů pro výdej musí být kladný.").
        Pokud je na skladě dostatek kusů, odečte je a vrátí True.
        Pokud dostatek kusů není, počet kusů se nezmění a metoda vrátí False.
        """
        if pocet <=0:
            raise ValueError("Počet kusů pro výdej musí být kladný.")

        if self._pocet_kusu >= pocet:
            self._pocet_kusu -= pocet
            return True
        else:
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

        if jmeno.strip() == "":
            raise ValueError("Jméno nesmí být prázdné")
        self._jmeno: str = jmeno
        if (rocnik >5 or rocnik <1):
            raise ValueError("Ročník musí být v rozsahu 1 až 5")
        self._rocnik: int = rocnik
        self._znamky: list[int] = []
        

    @property
    def jmeno(self) -> str:
        return self._jmeno

    @jmeno.setter
    def jmeno(self, hodnota: str) -> None:
        if hodnota.strip() == "":
            raise ValueError("Jméno studenta nesmí být prázdné.")
        self._jmeno = hodnota.strip()

    @property
    def rocnik(self) -> int:
        return self._rocnik

    @rocnik.setter
    def rocnik(self, hodnota: int) -> None:
        if (hodnota>5 or hodnota<1):
            raise ValueError("Neplatný ročník (povolené hodnoty 1-5).")
        self._rocnik = hodnota

    @property
    def znamky(self) -> list[int]:
        """
        Vrátí kopii seznamu známek (aby vnější kód nemohl přímo měnit vnitřní seznam).
        """
        return list(self._znamky)

    def pridej_znamku(self, znamka: int) -> None:
        """
        Přidá novou známku do seznamu studenta.
        Známka musí být celé číslo v rozsahu 1 až 5.
        Pokud hodnota není v rozsahu 1 až 5, vyvolejte ValueError("Známka musí být v rozsahu 1 až 5.").
        """
        if (znamka>5 or znamka <1):
            raise ValueError("Známka musí být v rozsahu 1 až 5.")
        self._znamky.append(znamka)

    @property
    def prumer(self) -> float:
        """
        Vypočítaná vlastnost: aritmetický průměr všech známek zaokrouhlený na 2 desetinná místa.
        Pokud student nemá žádné známky, vrátí 0.0.
        """
        if self._znamky != []:
            return sum(self._znamky)/len(self._znamky)
        else:
            return 0.0

    @property
    def prospel(self) -> bool:
        """
        Vypočítaná vlastnost:
        - Pokud student nemá žádné známky, vrátí True.
        - Pokud má alespoň jednu známku 5, vrátí False.
        - Pokud je jeho průměr <= 3.0 (a nemá 5), vrátí True.
        - Jinak (průměr > 3.0) vrátí False.
        """
        if self._znamky == []:
            return True
        if (self.prumer <= 3.0) and (5 not in self._znamky):
            return True
        if (5 in self._znamky) or (self.prumer > 3.0):
            return False
