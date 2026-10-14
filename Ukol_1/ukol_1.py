"""
Úkol 1: Základy jazyka Python – proměnné, operátory, větvení a cykly.

Vyplňte těla jednotlivých funkcí podle zadání v komentářích a v README.md.
Neměňte názvy funkcí ani jejich parametry.
"""


def vypocet_bmi(vaha_kg: float, vyska_m: float) -> float:

    if vaha_kg <= 0 or vyska_m <= 0:
        return 0.0

    BMI = vaha_kg / (vyska_m ** 2)
    
    BMI = round(BMI, 2)
    return BMI


def kategorie_bmi(bmi: float) -> str:


    if bmi <= 0:
        return "neplatna hodnota"
    elif bmi < 18.5:
        return "podvaha"
    elif bmi < 25.0:
        return "normalni"
    elif bmi < 30.0:
        return "nadvaha"
    else:
        return "obezita"


def soucet_sudych(start: int, stop: int) -> int:

    soucet = 0

    if start > stop:
        return 0

    for i in range(start, stop + 1):

        if(i % 2 == 0):
            soucet += i

    return soucet


def pocet_kroku_collatz(n: int) -> int:

    pocitadlo = 0

    if n <=1:
        return 0

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        pocitadlo += 1

    return pocitadlo


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
