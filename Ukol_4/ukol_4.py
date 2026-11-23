import argparse
import functools
import re
from abc import ABC, abstractmethod
from typing import Any, Callable


class NeplatnyKodZasilkyError(Exception):
    pass


def over_kod_zasilky(kod: str) -> dict[str, str]:
    m = re.match(r"^([A-Z]{2})-(\d{6})-([A-Z]{3})$", kod)

    if not m:
        raise NeplatnyKodZasilkyError("Neplatný formát kódu zásilky.")

    return {"zeme": m.group(1), "cislo": m.group(2), "typ": m.group(3)}


def over_kladne_argumenty(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError("Číselný argument musí být kladný.")

        for _key, value in kwargs.items():
            if isinstance(value, (int, float)) and value <= 0:
                raise ValueError("Číselný argument musí být kladný.")

        return func(*args, **kwargs)

    return wrapper


class Zasilka(ABC):
    def __init__(self, kod: str, hmotnost_kg: float) -> None:
        if not kod.strip():
            raise ValueError("Kód zásilky nesmí být prázdný.")
        if hmotnost_kg <= 0:
            raise ValueError("Hmotnost musí být kladná.")

        self.kod = kod.strip()
        self.hmotnost_kg = float(hmotnost_kg)

    @abstractmethod
    def spocitej_cenu(self) -> float:
        pass

    def __str__(self) -> str:
        return f"Zásilka {self.kod} [{self.spocitej_cenu():.2f} Kč]"

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(kod='{self.kod}', "
            f"hmotnost_kg={self.hmotnost_kg})"
        )

    def __eq__(self, other: object) -> bool:
        if self.__class__ == other.__class__ and self.kod == other.kod:
            return True
        return False

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Zasilka):
            raise NotImplementedError()

        return self.spocitej_cenu() < other.spocitej_cenu()

    def __add__(self, other: object) -> float:
        if not isinstance(other, Zasilka):
            raise NotImplementedError()

        return self.spocitej_cenu() + other.spocitej_cenu()


class StandardniZasilka(Zasilka):
    def __init__(self, kod: str, hmotnost_kg: float) -> None:
        super().__init__(kod, hmotnost_kg)

    def spocitej_cenu(self) -> float:
        return round(60.0 + self.hmotnost_kg * 15.0, 2)


class ExpresniZasilka(Zasilka):
    def __init__(
        self, kod: str, hmotnost_kg: float, priplatek: float = 100.0
    ) -> None:
        super().__init__(kod, hmotnost_kg)

        if priplatek < 0:
            raise ValueError("Příplatek nesmí být záporný")

        self.priplatek = float(priplatek)

    def spocitej_cenu(self) -> float:
        return round((60.0 + self.hmotnost_kg * 25.0) + self.priplatek, 2)


def vytvor_parser() -> argparse.ArgumentParser:
    args = argparse.ArgumentParser(
        description="Systém pro kalkulaci a správu zásilek"
    )

    args.add_argument("kod", type=str, help="Kód zásilky")

    args.add_argument("hmotnost", type=float, help="Hmotnost zásilky v kg")

    args.add_argument(
        "--typ",
        "-t",
        type=str,
        choices=["standard", "expres"],
        default="standard",
        help="Typ zásilky",
    )

    args.add_argument(
        "--priplatek",
        "-p",
        type=float,
        default=100.0,
        help="Expresní příplatek",
    )

    return args


def vytvor_zasilku_z_argumentu(args: argparse.Namespace) -> Zasilka:
    if args.typ == "standard":
        return StandardniZasilka(args.kod, args.hmotnost)
    elif args.typ == "expres":
        return ExpresniZasilka(
            args.kod, args.hmotnost, priplatek=args.priplatek
        )


if __name__ == "__main__":
    # Ukázka použití: načtěte argumenty, vytvořte zásilku a vypište ji.
    # Ošetřete NeplatnyKodZasilkyError a ValueError pomocí try/except.
    pass
