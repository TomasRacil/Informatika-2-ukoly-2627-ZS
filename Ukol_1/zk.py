
def vypocet_bmi(vaha_kg: float, vyska_m: float) -> float:
    """ Spočítá Body Mass Index (BMI) podle vzorce:
        BMI = vaha_kg / (vyska_m ** 2)

    Výsledek zaokrouhlete na 2 desetinná místa pomocí funkce round(..., 2).
    Pokud je váha <= 0 nebo výška <= 0, vraťte 0.0.
    """
    # TODO: Doplňte výpočet BMI se zaokrouhlením na 2 desetinná místa 
    BMI = float(vaha_kg/(vyska_m**2))

    if vaha_kg <=0.0 or vyska_m <= 0.0: 
        BMI = 0.0
        
    print(f"BMI:  {BMI}")
    BMI = round(BMI, 2)
  
    
    return BMI

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

    if bmi<18.5:
        return "podvaha"
    elif 18.5 <= bmi < 25.0:
        return "normalni"
    elif 25.0 <= bmi < 30.0:
        return "nadvaha"
    elif bmi >= 30.0:
        return "obezita"
    elif bmi <= 0.0:
        return "neplatna hodnota"

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
    n =int (0)
    if start%2==1:
            start = start+1
    for i in range(start,stop+1, 2):
        n = int(n+i)

    # TODO: Doplňte cyklus for s funkcí range()
    return n

    
def main():
    print("=== Testování funkcí Úkolu 1 ===")
    vaha = 70.0
    vyska = 1.80
    bmi = vypocet_bmi(vaha, vyska)
    print(f"1. BMI ({vaha} kg, {vyska} m): {bmi}")
    print(f"2. Kategorie pro BMI {bmi}: {kategorie_bmi(bmi)}")
    print(f"3. Součet sudých čísel od 1 do 10: {soucet_sudych(1, 10)}")

if __name__ == "__main__":
    main()