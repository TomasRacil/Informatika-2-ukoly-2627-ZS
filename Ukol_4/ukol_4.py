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
    """
    m = re.fullmatch(r"^([A-Z]{2})-(\d{6})-([A-Z]{3})$", kod)
    if not m:
        raise NeplatnyKodZasilkyError("Neplatný formát kódu zásilky.")
    return {"zeme": m.group(1), "cislo": m.group(2), "typ": m.group(3)}


def over_kladne_argumenty(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Dekorátor, který ověří, že všechny číselné argumenty jsou kladné.
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        for arg in (*args, *kwargs.values()):
            if isinstance(arg, (int, float)) and not isinstance(arg, bool) and arg <= 0:
                raise ValueError("Číselný argument musí být kladný.")
        return func(*args, **kwargs)

    return wrapper


class Zasilka(ABC):
    """
    Abstraktní předek všech zásilek.

    Atributy:
        kod (str): Kód zásilky (nesmí být prázdný, ukládá se oříznutý).
        hmotnost_kg (float): Hmotnost zásilky v kg (musí být > 0).
    """

    def __init__(self, kod: str, hmotnost_kg: float) -> None:
        """Inicializuje kód a hmotnost zásilky."""
        if not kod or not kod.strip():
            raise ValueError("Kód zásilky nesmí být prázdný.")
        if hmotnost_kg <= 0:
            raise ValueError("Hmotnost musí být kladná.")
        self.kod = kod.strip()
        self.hmotnost_kg = float(hmotnost_kg)

    @abstractmethod
    def spocitej_cenu(self) -> float:
        """Vypočítá a vrátí cenu zásilky v Kč. Implementují odvozené třídy."""
        pass

    def __str__(self) -> str:
        """Vrátí textový popis zásilky."""
        return f"Zásilka {self.kod} [{self.spocitej_cenu():.2f} Kč]"

    def __repr__(self) -> str:
        """Vrátí jednoznačnou reprezentaci zásilky."""
        return f"{self.__class__.__name__}(kod='{self.kod}', hmotnost_kg={self.hmotnost_kg})"

    def __eq__(self, other: object) -> bool:
        """Porovná dvě zásilky podle konkrétní třídy a kódu."""
        if isinstance(other, Zasilka) and self.__class__ == other.__class__:
            return self.kod == other.kod
        return False

    def __lt__(self, other: object) -> bool:
        """Porovná dvě zásilky podle ceny."""
        if isinstance(other, Zasilka):
            return self.spocitej_cenu() < other.spocitej_cenu()
        return NotImplemented

    def __add__(self, other: object) -> float:
        """Vrátí součet cen obou zásilek."""
        if isinstance(other, Zasilka):
            return self.spocitej_cenu() + other.spocitej_cenu()
        return NotImplemented


class StandardniZasilka(Zasilka):
    """Standardní zásilka: 60 Kč základ + 15 Kč za každý kilogram."""

    def __init__(self, kod: str, hmotnost_kg: float) -> None:
        super().__init__(kod, hmotnost_kg)

    def spocitej_cenu(self) -> float:
        return round(60.0 + self.hmotnost_kg * 15.0, 2)


class ExpresniZasilka(Zasilka):
    """Expresní zásilka: 60 Kč základ + 25 Kč za každý kilogram + příplatek."""

    def __init__(self, kod: str, hmotnost_kg: float, priplatek: float = 100.0) -> None:
        super().__init__(kod, hmotnost_kg)
        if priplatek < 0:
            raise ValueError("Příplatek nesmí být záporný.")
        self.priplatek = float(priplatek)

    def spocitej_cenu(self) -> float:
        return round((60.0 + self.hmotnost_kg * 25.0) + self.priplatek, 2)


def vytvor_parser() -> argparse.ArgumentParser:
    """Vytvoří a vrátí parser příkazové řádky."""
    parser = argparse.ArgumentParser(description="Systém pro kalkulaci a správu zásilek")
    parser.add_argument("kod", type=str, help="Kód zásilky")
    parser.add_argument("hmotnost", type=float, help="Hmotnost zásilky v kg")
    parser.add_argument(
        "--typ",
        "-t",
        type=str,
        choices=["standard", "expres"],
        default="standard",
        help="Typ zásilky",
    )
    parser.add_argument(
        "--priplatek",
        "-p",
        type=float,
        default=100.0,
        help="Expresní příplatek",
    )
    return parser


def vytvor_zasilku_z_argumentu(args: argparse.Namespace) -> Zasilka:
    """Podle args.typ vytvoří odpovídající zásilku a vrátí ji."""
    if args.typ == "expres":
        return ExpresniZasilka(args.kod, args.hmotnost, priplatek=args.priplatek)
    return StandardniZasilka(args.kod, args.hmotnost)


if __name__ == "__main__":
    parser = vytvor_parser()
    args = parser.parse_args()
    try:
        over_kod_zasilky(args.kod)
        zasilka = vytvor_zasilku_z_argumentu(args)
        print(zasilka)
    except (NeplatnyKodZasilkyError, ValueError) as e:
        print(e)