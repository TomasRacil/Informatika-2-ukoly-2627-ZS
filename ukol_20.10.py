class Bankovni_Ucet:
    def __init__(self, cislo_uctu: str, majitel: str, pocatecni_zustatek: float = 0.0):
        self._cislo_uctu:str = cislo_uctu
        self._majitel:str = majitel
        self._zustatek:float = pocatecni_zustatek
        self._historie:list[tuple[str, float]]=[]
        if float(pocatecni_zustatek)!= 0:
            self._historie.append(("Vklad", pocatecni_zustatek))

    @property
    def majitel(self):
        return self._majitel

    @majitel.setter
    def majitel(self, jmeno):
        if jmeno.strip() == "":
            raise ValueError("Jméno majitele nesmí být prázdné")
        self._majitel = jmeno

    @property
    def zustatek(self):
        return self._zustatek
    
    @zustatek.setter
    def zustatek(self, hodnota):
        if hodnota>=0:
            self._zustatek=hodnota
        else:
            raise ValueError("Zůstatek nemůže být záporný")

    @property
    def cislo_uctu(self):
        return self._cislo_uctu

    def vloz(self,castka:float)->bool:
        if castka>0:
            self._zustatek+=castka
            self._historie.append(("Vklad",castka))
            return True
        else:
            return False

    def vyber(self,castka:float)->bool:
        if castka>0 and castka<=self._zustatek:
            self._zustatek-=castka
            self._historie.append(("Výběr",castka))
            return True
        else:
            return False

    def vypis_transakce(self)->list[str]:
        h:list[str]=[]
        for typ, castka in self._historie:
            if typ == "Vklad":
                h.append(f"Vklad: +{castka:.2f} kč")
            elif typ == "Výběr":
                h.append(f"Výběr: -{castka:.2f} kč")
        return h

    def __str__(self) -> str:
        return (f"Účet {self._cislo_uctu} ({self._majitel}) - Zůstatek: {self._zustatek:.2f} Kč")

    def __repr__(self) -> str:
        return (f"BankovniUcet(cislo_uctu='{self._cislo_uctu}', majitel='{self._majitel}', zustatek={self._zustatek})")

class Banka:
    def __init__(self,nazev:str):
        self.nazev = nazev
        self._ucty: dict[str, Bankovni_Ucet] = {}

    def zaloz_ucet(self, cislo_uctu: str, majitel: str, pocatecni_vklad: float = 0.0) -> Bankovni_Ucet:
        if cislo_uctu in self._ucty:
            raise ValueError(f"Účet {cislo_uctu} již existuje.")
        
        novy = Bankovni_Ucet(cislo_uctu,majitel,pocatecni_vklad)
        self._ucty[cislo_uctu] = novy
        return novy


    def ziskej_ucet(self, cislo_uctu: str) -> Bankovni_Ucet | None:
        if cislo_uctu in self._ucty:
            return self._ucty[cislo_uctu]
        else:
            return None

    def preved_penize(self, z_uctu: str, na_ucet: str, castka: float) -> bool:
        if z_uctu in self._ucty and na_ucet in self._ucty:
            if self._ucty[z_uctu]._zustatek-castka>=0:
                self._ucty[z_uctu].vyber(castka)
                self._ucty[na_ucet].vloz(castka)
                return True
        else:
            return False 

    @property
    def celkovy_kapital(self):
        celkem = 0
        for i in self._ucty:
            celkem+=self._ucty[i]._zustatek
        return celkem


banka = Banka("Python Banka")
ucet1 = banka.zaloz_ucet("111/0800", "Jan Novák", 1000.0)
ucet2 = banka.zaloz_ucet("222/0800", "Eva Černá", 500.0)

ucet1.vloz(500.0)
ucet1.vyber(200.0)

uspech = banka.preved_penize("111/0800", "222/0800", 300.0)
print(f"Převod proběhl: {uspech}")

print(ucet1)
print(ucet2)
print("Celkový kapitál banky:", banka.celkovy_kapital)
print("Historie účtu 1:", ucet1.vypis_transakce())
