"""
Úkol 3: Objektově orientované programování – třídy, typové anotace a vlastnosti.

Vyplňte těla jednotlivých tříd a metod podle zadání v komentářích a v README.md.
Neměňte názvy tříd, metod ani jejich parametrů.
"""


class Kniha:
    def __init__(self, nazev: str, autor: str, pocet_stran: int, cena: float) -> None:
        self.nazev: str = nazev
        self.autor: str = autor
        self.pocet_stran: int = pocet_stran
        self.cena: float = cena

    @property
    def nazev(self) -> str:
        return self._nazev

    @nazev.setter
    def nazev(self, hodnota: str) -> None:
        if hodnota.strip():
            self._nazev = hodnota.strip()
        else: raise ValueError("Nazev nesmi byt praydny")


    @property
    def autor(self) -> str:
        return self._autor

    @autor.setter
    def autor(self, hodnota: str) -> None:
        if hodnota.strip():
            self._autor = hodnota.strip()
        else: raise ValueError("Autor nesmi byt praydny")

    @property
    def pocet_stran(self) -> int:
        return self._pocet_stran

    @pocet_stran.setter
    def pocet_stran(self, hodnota: int) -> None:
        if hodnota>0: 
            self._pocet_stran = hodnota
        else: 
            raise ValueError("Počet stran musí být kladné číslo.")

    @property
    def cena(self) -> float:
        return self._cena

    @cena.setter
    def cena(self, hodnota: float) -> None:
        if hodnota>=0:
            self._cena = hodnota
        else:
            raise ValueError("Cena nesmí být záporná.")

    def sleva(self, procento: float) -> None:
        if procento>=0 and procento<=100:
            procento/=100
            self._cena-= self._cena*procento
            self._cena=round(self._cena,2)
        else:
            raise ValueError("Sleva musí být v rozmezí 0 až 100 %")

    def __str__(self) -> str:
        return f"{self._nazev} ({self._autor}) - {self._pocet_stran} str., {self._cena} Kč"


class PolozkaSkladu:
    def __init__(self, kod: str, nazev: str, cena_za_kus: float, pocet_kusu: int = 0) -> None:
        self._kod: str = kod
        self.nazev: str = nazev
        self.cena_za_kus: float = cena_za_kus
        self.pocet_kusu: int = pocet_kusu

    @property
    def kod(self) -> str:
        return self._kod

    @property
    def nazev(self) -> str:
        return self._nazev

    @nazev.setter
    def nazev(self, hodnota: str) -> None:
        if hodnota.strip():
            self._nazev = hodnota.strip()
        else:
            raise ValueError("Název nesmí být prázdný.")

    @property
    def cena_za_kus(self) -> float:
        return self._cena_za_kus

    @cena_za_kus.setter
    def cena_za_kus(self, hodnota: float) -> None:
        if hodnota>=0: 
            self._cena_za_kus = hodnota
        else:
            raise ValueError("Cena za kus nesmí být záporná.")

    @property
    def pocet_kusu(self) -> int:
        return self._pocet_kusu

    @pocet_kusu.setter
    def pocet_kusu(self, hodnota: int) -> None:
        if hodnota>=0:
            self._pocet_kusu = hodnota
        else:
            raise ValueError("Počet kusů nesmí být záporný.")

    @property
    def hodnota_zasob(self) -> float:
        return round(self._cena_za_kus*self._pocet_kusu,2)

    def prijem(self, pocet: int) -> None:
        if pocet>0:
            self.pocet_kusu+=pocet
        else: 
            raise ValueError("Počet kusů pro příjem musí být kladný.")

    def vydej(self, pocet: int) -> bool:
        if pocet<=0:
            raise ValueError("Počet kusů pro výdej musí být kladný.")
        
        if self._pocet_kusu>=pocet:
            self._pocet_kusu-=pocet
            return True
        
        return False


class Student:
    def __init__(self, jmeno: str, rocnik: int) -> None:
        self.jmeno: str = jmeno
        self.rocnik: int = rocnik
        self._znamky: list[int] = []

    @property
    def jmeno(self) -> str:
        return self._jmeno

    @jmeno.setter
    def jmeno(self, hodnota: str) -> None: 
        if hodnota.strip():
            self._jmeno = hodnota.strip()
        else:
            raise ValueError("Jméno studenta nesmí být prázdné.")

    @property
    def rocnik(self) -> int:
        return self._rocnik

    @rocnik.setter
    def rocnik(self, hodnota: int) -> None:
        if hodnota>=1 and hodnota<=5:
            self._rocnik = hodnota
        else:
            raise ValueError("Neplatný ročník (povolené hodnoty 1-5).")

    @property
    def znamky(self) -> list[int]:
        return list(self._znamky)

    def pridej_znamku(self, znamka: int) -> None:
        if znamka>=1 and znamka<=5:
            self._znamky.append(znamka)
        else :
            raise ValueError("Známka musí být v rozsahu 1 až 5.")


    @property
    def prumer(self) -> float:
        soucet:int=0

        if len(self.znamky) ==0:
            return 0.0
        else:
            for i in self.znamky:
                soucet+=i
            return round(soucet/len(self.znamky),2)


    @property
    def prospel(self) -> bool:
        if len(self.znamky)==0:
            return True
        elif 5 in self.znamky:
            return False
        elif self.prumer<=3.0 and 5 not in self.znamky:
            return True
        else:
            return False
