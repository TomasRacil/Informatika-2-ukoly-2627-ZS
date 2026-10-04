"""
Úkol 1: Základy jazyka Python – proměnné, operátory, větvení a cykly.

Vyplňte těla jednotlivých funkcí podle zadání v komentářích a v README.md.
Neměňte názvy funkcí ani jejich parametry.
"""


def vypocet_bmi(vaha_kg: float, vyska_m: float) -> float:
    """
    Spočítá Body Mass Index (BMI) podle vzorce:
        BMI = vaha_kg / (vyska_m ** 2)

    Výsledek zaokrouhlete na 2 desetinná místa pomocí funkce round(..., 2).
    Pokud je váha <= 0 nebo výška <= 0, vraťte 0.0.
    """
    # TODO: Doplňte výpočet BMI se zaokrouhlením na 2 desetinná místa
    return 0.0


def kategorie_bmi(bmi: float) -> str:
    """
    Na základě hodnoty BMI určí váhovou kategorii:
        - bmi < 18.5: "podvaha"
        - 18.5 <= bmi < 25.0: "normalni"
        - 25.0 <= bmi < 30.0: "nadvaha"
        - bmi >= 30.0: "obezita"

    Pokud je bmi <= 0, vraťte "neplatna hodnota".
    """
    # TODO: Doplňte větvení if-elif-else
    return ""


def soucet_sudych(start: int, stop: int) -> int:
    """
    Pomocí cyklu for spočítá součet všech SUDÝCH celých čísel
    v uzavřeném intervalu od start do stop (včetně obou mezí).

    Příklady:
        start = 1, stop = 6 -> sudá jsou 2, 4, 6 -> součet = 12
        start = 2, stop = 2 -> sudé je 2 -> součet = 2
        start = 5, stop = 5 -> žádné sudé -> součet = 0

    Pokud je start > stop, vraťte 0.
    """
    # TODO: Doplňte cyklus for s funkcí range()
    return 0


def pocet_kroku_collatz(n: int) -> int:
    """
    Pomocí cyklu while spočítá, kolik kroků trvá, než kladné celé číslo n
    dosáhne hodnoty 1 podle pravidel Collatzovy posloupnosti:
        - pokud je číslo sudé, vydělte ho 2 (celočíselně: n // 2)
        - pokud je číslo liché, vynásobte ho 3 a přičtěte 1 (3 * n + 1)
        - proces se opakuje, dokud n není 1.

    Pokud je n <= 1, funkce vrátí 0 (pro hodnotu 1 je potřeba 0 kroků).

    Příklad pro n = 6:
        6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 (celkem 8 kroků)
    """
    # TODO: Doplňte cyklus while a počítadlo kroků
    return 0


def main():
    print("=== Testování funkcí Úkolu 1 ===")
    vaha = 75.0
    vyska = 1.80
    bmi = vypocet_bmi(vaha, vyska)
    print(f"1. BMI ({vaha} kg, {vyska} m): {bmi}")
    print(f"2. Kategorie pro BMI {bmi}: {kategorie_bmi(bmi)}")
    print(f"3. Součet sudých čísel od 1 do 10: {soucet_sudych(1, 10)}")
    print(f"4. Počet kroků Collatzovy posloupnosti pro číslo 6: {pocet_kroku_collatz(6)}")


if __name__ == "__main__":
    main()
