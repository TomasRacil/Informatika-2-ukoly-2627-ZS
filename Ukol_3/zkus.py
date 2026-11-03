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

        # TODO: Inicializujte atributy přes property settery pro zajištění validace
        self.nazev = nazev
        self.autor = autor

    @property
    def nazev(self) -> str:
        
        return self._nazev

    @nazev.setter
    def nazev(self, hodnota: str) -> None:
        if not isinstance(hodnota, str) or not hodnota.strip():
            raise ValueError("Jméno knihy nesmí být prázdné.")
        self._nazev = hodnota.strip()     

    @property
    def autor(self) -> str:
        return self._autor

    @autor.setter
    def autor(self, hodnota: str) -> None:
        if not isinstance(hodnota, str) or not hodnota.strip():
            raise ValueError("Jméno autora nesmí být prázdné.")
        self._autor = hodnota.strip()

    @property
    def pocet_stran(self) -> int:
        
        return self._pocet_stran

    @pocet_stran.setter
    def pocet_stran(self, hodnota: int) -> None:
        if not isinstance(hodnota, str) or not hodnota.strip() or hodnota<0:
             raise ValueError("Počet stran musí být kladné číslo.")
        self._pocet_stran = float(hodnota)  

        # TODO: Ověřte, že hodnota je > 0.
        # Pokud ne, vyvolejte ValueError("Počet stran musí být kladné číslo.")
       

    @property
    def cena(self) -> float:
        
        return self._cena

    @cena.setter
    def cena(self, hodnota: float) -> None:
        if not isinstance(hodnota, str) or not hodnota.strip() or hodnota<=0:
                raise ValueError("Cana nesmí být záporná.")
        self._cena = float(hodnota)  
        # TODO: Ověřte, že hodnota je >= 0.
        # Pokud ne, vyvolejte ValueError("Cena nesmí být záporná.")
        

    def sleva(self, procento: float) -> None:
        """
        Sníží cenu knihy o zadané procento (0 až 100).
        Výslednou cenu zaokrouhlete na 2 desetinná místa pomocí round(..., 2).
        Pokud procento není v rozsahu 0 až 100, vyvolejte ValueError("Sleva musí být v rozmezí 0 až 100 %.").
        """
        if procento>=0 and procento<=100:
            procento = procento/100
            c = self.cena
            c = c - (c*procento)
            c = round(c,2)
            self._cena = c
            return self._cena
        else: ValueError ("Sleva musí být v rozmezí 0 až 100 %.")
        

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
        self._kod: str = kod
        self._nazev: str = ""
        self._cena_za_kus: float = 0.0
        self._pocet_kusu: int = 0

        self.nazev = nazev

    @property
    def kod(self) -> str:
        
        return self._kod

    @property
    def nazev(self) -> str:
        return self._nazev

    @nazev.setter
    def nazev(self, hodnota: str) -> None:

        if not isinstance(hodnota, str) or not hodnota.strip():
            raise ValueError("Název nesmí být prázdný.")
        self._nazev = hodnota.strip()
        

    @property
    def cena_za_kus(self) -> float:
        return self._cena_za_kus

    @cena_za_kus.setter
    def cena_za_kus(self, hodnota: float) -> None:
        if hodnota<0:
            raise ValueError("Cena za kus nesmí být záporná.")
        self._cena_za_kus =float(hodnota)

        

    @property
    def pocet_kusu(self) -> int:
        return self._pocet_kusu

    @pocet_kusu.setter
    def pocet_kusu(self, hodnota: int) -> None:
        if hodnota<=0:
            raise ValueError("Počet kusů nesmí být záporný.")
        self._pocet_kusu = int(hodnota)
        # TODO: Ověřte, že počet kusů je >= 0.
        # Pokud ne, vyvolejte ValueError("Počet kusů nesmí být záporný.")
        

    @property
    def hodnota_zasob(self) -> float:
        """
        Vypočítaná vlastnost (pouze pro čtení): celková cena všech kusů na skladě (cena_za_kus * pocet_kusu).
        Zaokrouhlete na 2 desetinná místa.
        """
        zasoby = self.cena_za_kus*self.pocet_kusu
        zasoby = round(zasoby,2)
        # TODO: Doplňte výpočet
        return zasoby

    def prijem(self, pocet: int) -> None:

        if pocet<=0:
            raise ValueError("Počet kusů pro příjem musí být kladný.")
        """
        Přičte zadaný počet kusů na sklad.
        Pokud je pocet <= 0, vyvolejte ValueError("Počet kusů pro příjem musí být kladný.").
        """
        self._pocet_kusu += pocet
        # TODO: Doplňte implementaci
        pass

    def vydej(self, pocet: int) -> bool:
        """
        Odečte zadaný počet kusů ze skladu, pokud je jich dostatek.
        Pokud je pocet <= 0, vyvolejte ValueError("Počet kusů pro výdej musí být kladný.").
        Pokud je na skladě dostatek kusů, odečte je a vrátí True.
        Pokud dostatek kusů není, počet kusů se nezmění a metoda vrátí False.
        """
        kusy = self._pocet_kusu
        if pocet<=0:
            raise ValueError("Počet kusů pro výdej musí být kladný.")
        if pocet<=kusy:
            kusy-=pocet
            self._pocet_kusu = kusy
            return True

        # TODO: Doplňte implementaci

        return False

