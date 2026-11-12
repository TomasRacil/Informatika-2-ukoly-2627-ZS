"""
Úkol 4: Pokročilý Python – výjimky, regulární výrazy, dekorátory, dědičnost,
abstraktní třídy, magické metody a argparse.

Vyplňte těla funkcí, tříd a metod podle zadání v docstringech a v README.md.
Neměňte názvy tříd, funkcí, metod ani jejich parametrů.
"""

import argparse
import functools
import re
from abc import ABC, abstractmethod
from typing import Any, Callable


class NeplatnyKodZasilkyError(Exception):
    """Výjimka vyvolaná při neplatném formátu kódu zásilky."""

    pass


def over_kod_zasilky(kod: str) -> dict[str, str]:
    """
    Ověří formát kódu zásilky a vrátí jeho jednotlivé části.

    Povolený formát je přesně: dvě velká písmena, pomlčka, šest číslic,
    pomlčka a tři velká písmena (např. "CZ-123456-STD").

    Použijte regulární výraz:
        r"^([A-Z]{2})-(\\d{6})-([A-Z]{3})$"

    Pokud kód formátu neodpovídá, vyvolejte:
        NeplatnyKodZasilkyError("Neplatný formát kódu zásilky.")

    Pokud kód odpovídá, vraťte slovník:
        {"zeme": m.group(1), "cislo": m.group(2), "typ": m.group(3)}
    """
    pass


def over_kladne_argumenty(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Dekorátor, který ověří, že všechny číselné argumenty jsou kladné.

    Projde všechny poziční argumenty (*args) i klíčové argumenty (**kwargs).
    Pokud je některý argument číselný (int nebo float) a jeho hodnota je <= 0,
    vyvolá ValueError("Číselný argument musí být kladný.").

    Pozor: bool je v Pythonu podtřídou int, ale za číslo se nepovažuje.

    Nečíselné argumenty (např. str) se ignorují. Pokud jsou všechny číselné
    argumenty kladné, zavolejte původní funkci a vraťte její návratovou hodnotu.

    Na vnořenou funkci použijte @functools.wraps(func).
    """
    pass


class Zasilka(ABC):
    """
    Abstraktní předek všech zásilek.

    Atributy:
        kod (str): Kód zásilky (nesmí být prázdný, ukládá se oříznutý).
        hmotnost_kg (float): Hmotnost zásilky v kg (musí být > 0).
    """

    def __init__(self, kod: str, hmotnost_kg: float) -> None:
        """
        Inicializuje kód a hmotnost zásilky.

        Pokud je kod po .strip() prázdný, vyvolejte
        ValueError("Kód zásilky nesmí být prázdný.").
        Pokud hmotnost_kg není > 0, vyvolejte
        ValueError("Hmotnost musí být kladná.").

        Uložte self.kod = kod.strip() a self.hmotnost_kg = float(hmotnost_kg).
        """
        pass

    @abstractmethod
    def spocitej_cenu(self) -> float:
        """Vypočítá a vrátí cenu zásilky v Kč. Implementují odvozené třídy."""
        pass

    def __str__(self) -> str:
        """
        Vrátí textový popis ve formátu:
        "Zásilka {kod} [{cena:.2f} Kč]"
        Například: "Zásilka CZ-123456-STD [97.50 Kč]"
        """
        pass

    def __repr__(self) -> str:
        """
        Vrátí jednoznačnou reprezentaci ve formátu:
        f"{self.__class__.__name__}(kod='{self.kod}', hmotnost_kg={self.hmotnost_kg})"
        Například: "StandardniZasilka(kod='CZ-123456-STD', hmotnost_kg=2.5)"
        """
        pass

    def __eq__(self, other: object) -> bool:
        """
        Zásilky jsou si rovny, pokud je other instance Zasilka, má stejnou
        konkrétní třídu (self.__class__ == other.__class__) a stejný kód.
        V opačném případě vraťte False.
        """
        pass

    def __lt__(self, other: object) -> bool:
        """
        Porovná ceny: vraťte self.spocitej_cenu() < other.spocitej_cenu(),
        pokud je other instance Zasilka. Jinak vraťte NotImplemented.
        """
        pass

    def __add__(self, other: object) -> float:
        """
        Vrátí součet cen obou zásilek, pokud je other instance Zasilka.
        Jinak vraťte NotImplemented.
        """
        pass


class StandardniZasilka(Zasilka):
    """Standardní zásilka: 60 Kč základ + 15 Kč za každý kilogram."""

    def __init__(self, kod: str, hmotnost_kg: float) -> None:
        """Zavolá super().__init__(kod, hmotnost_kg)."""
        pass

    def spocitej_cenu(self) -> float:
        """Vrátí round(60.0 + self.hmotnost_kg * 15.0, 2)."""
        pass


class ExpresniZasilka(Zasilka):
    """Expresní zásilka: 60 Kč základ + 25 Kč za každý kilogram + příplatek."""

    def __init__(self, kod: str, hmotnost_kg: float, priplatek: float = 100.0) -> None:
        """
        Zavolá super().__init__(kod, hmotnost_kg).
        Pokud je priplatek < 0, vyvolejte ValueError("Příplatek nesmí být záporný.").
        Uložte self.priplatek = float(priplatek).
        """
        pass

    def spocitej_cenu(self) -> float:
        """Vrátí round((60.0 + self.hmotnost_kg * 25.0) + self.priplatek, 2)."""
        pass


def vytvor_parser() -> argparse.ArgumentParser:
    """
    Vytvoří a vrátí parser příkazové řádky.

    description="Systém pro kalkulaci a správu zásilek"
    Poziční argument "kod": type=str, help="Kód zásilky"
    Poziční argument "hmotnost": type=float, help="Hmotnost zásilky v kg"
    Volitelný "--typ"/"-t": type=str, choices=["standard", "expres"],
        default="standard", help="Typ zásilky"
    Volitelný "--priplatek"/"-p": type=float, default=100.0,
        help="Expresní příplatek"
    """
    pass


def vytvor_zasilku_z_argumentu(args: argparse.Namespace) -> Zasilka:
    """
    Podle args.typ vytvoří odpovídající zásilku a vrátí ji.

    Pro "standard" vraťte StandardniZasilka(args.kod, args.hmotnost).
    Pro "expres" vraťte
    ExpresniZasilka(args.kod, args.hmotnost, priplatek=args.priplatek).
    """
    pass


if __name__ == "__main__":
    # Ukázka použití: načtěte argumenty, vytvořte zásilku a vypište ji.
    # Ošetřete NeplatnyKodZasilkyError a ValueError pomocí try/except.
    pass
