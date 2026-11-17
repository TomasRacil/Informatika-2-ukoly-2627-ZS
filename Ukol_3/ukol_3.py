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
        self.pocet_stran = pocet_stran
        self.cena = cena

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
        
        if not isinstance(hodnota, int) or  hodnota<=0:
             raise ValueError("Počet stran musí být kladné číslo.")
        
        self._pocet_stran = hodnota  

        # TODO: Ověřte, že hodnota je > 0.
        # Pokud ne, vyvolejte ValueError("Počet stran musí být kladné číslo.")
       

    @property
    def cena(self) -> float:
        
        return self._cena

    @cena.setter
    def cena(self, hodnota: float) -> None:
        if not isinstance(hodnota,(int, float)) or hodnota<0:
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
            self.cena = round(c,2)
            
        else:
            raise ValueError ("Sleva musí být v rozmezí 0 až 100 %.")
        

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
        self.pocet_kusu = pocet_kusu
        self.cena_za_kus = cena_za_kus
        



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
        if hodnota<0:
            raise ValueError("Počet kusů nesmí být záporný.")
        else:
            self._pocet_kusu = hodnota
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

        # TODO: Inicializujte jmeno a rocnik přes property settery
        self.jmeno = jmeno
        self.rocnik = rocnik

    @property
    def jmeno(self) -> str:
        return self._jmeno

    @jmeno.setter
    def jmeno(self, hodnota: str) -> None:
         if not isinstance(hodnota, str) or not hodnota.strip():
            raise ValueError("Neplatne jmeno")
         else:
             self._jmeno = hodnota  
                # TODO: Ověřte, že hodnota je >= 0.
                # Pokud ne, vyvolejte ValueError("Cena nesmí být záporná.")
                

    @property
    def rocnik(self) -> int:
        return self._rocnik

    @rocnik.setter
    def rocnik(self, hodnota: int) -> None:
        if hodnota<1 or hodnota >5:
            raise ValueError("Neplatný ročník (povolené hodnoty 1-5).")
        else:
            self._rocnik = hodnota

        # TODO: Ověřte, že ročník je v rozsahu 1 až 5 (včetně).
        # Pokud ne, vyvolejte ValueError("Neplatný ročník (povolené hodnoty 1-5).")
        

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
        if not isinstance(znamka,int) or znamka<1 or znamka>5:
            raise  ValueError("Známka musí být v rozsahu 1 až 5.")
        self._znamky.append(znamka)

    @property
    def prumer(self) -> float:
        konec = 0.0
        for x in self._znamky:
            konec+=x
        if konec==0.0:
            return 0.0
        konec = konec/(len(self._znamky))
        konec = round(konec,2)

        """
        Vypočítaná vlastnost: aritmetický průměr všech známek zaokrouhlený na 2 desetinná místa.
        Pokud student nemá žádné známky, vrátí 0.0.
        """
        # TODO: Doplňte výpočet průměru
        return konec

    @property
    def prospel(self) -> bool:
        if not self._znamky:
            return True
        if 5 in self.znamky:
                return False
        if self.prumer <= 3:
            return True
        
        return False
        """
        Vypočítaná vlastnost:
        - Pokud student nemá žádné známky, vrátí True.
        - Pokud má alespoň jednu známku 5, vrátí False.
        - Pokud je jeho průměr <= 3.0 (a nemá 5), vrátí True.
        - Jinak (průměr > 3.0) vrátí False.
        """
        # TODO: Doplňte logiku prospěchu
        return True
