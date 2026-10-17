"""
Úkol 1: Základy jazyka Python – proměnné, operátory, větvení a cykly.

Vyplňte těla jednotlivých funkcí podle zadání v komentářích a v README.md.
Neměňte názvy funkcí ani jejich parametry.
"""


def vypocet_bmi(vaha_kg: float, vyska_m: float) -> float:
    # TODO: Doplňte výpočet BMI se zaokrouhlením na 2 desetinná místa
    if vaha_kg <=0 or vyska_m<=0:
        return 0.0
    else:
        return round(vaha_kg/vyska_m**2,2)


def kategorie_bmi(bmi: float) -> str:
    # TODO: Doplňte větvení if-elif-else
    if bmi<=0 :
        return "neplatna hodnota"
    elif 18.5 <= bmi and bmi< 25.0:
        return "normalni"
    elif bmi<18.5:
        return "podvaha"
    elif 25.0 <= bmi and bmi < 30.0:
        return "nadvaha"
    elif bmi>=30.0:
        return "obezita"
    #nebo 
    #else : return "obezita"


def soucet_sudych(start: int, stop: int) -> int:
    # TODO: Doplňte cyklus for s funkcí range()
    sum=0
    for i in range(start,stop+1):
        if i%2==0:
            sum+=i
        elif start>stop: return 0
    return sum



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
    pocet_kroku =0

    if n<=1: return 0
    while n!=1:
        if n%2==0:
            n= n//2
        elif n%2!=0:
            n = 3*n+1
        pocet_kroku+=1
    return pocet_kroku



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
