"""
Úkol 2: Datové struktury – řetězce, množiny, n-tice a slovníky.

Vyplňte těla jednotlivých funkcí podle zadání v komentářích a v README.md.
Neměňte názvy funkcí ani jejich parametry.
"""


def extrahuj_hashtagy(text: str) -> set[str]:
    """
    Z textu vyextrahuje všechny hashtagy (slova začínající znakem '#').

    Pravidla:
    - Rozdělte text na slova podle bílých znaků (.split()).
    - Slovo je považováno za hashtag, pokud začíná znakem '#'.
    - Odstraňte úvodní křížek '#' a z konce slova odstraňte případnou interpunkci (',', '.', '!', '?', ':', ';', '"').
    - Převeďte název hashtagu na malá písmena.
    - Pokud po očištění zůstane neprázdný řetězec, přidejte jej do výsledné množiny.
    - Vrátí množinu (set[str]) unikátních názvů hashtagů.
    - Pokud text neobsahuje žádný platný hashtag, vrátí prázdnou množinu set().

    Příklad:
        text = "Učíme se #Python a #datové_struktury! #python je #super."
        extrahuj_hashtagy(text) -> {"python", "datové_struktury", "super"}
    """
    # TODO: Doplňte implementaci
    ocistenaSlova = set()
    for slovo in text.split():
        if slovo.startswith("#"):
            slovo = slovo[1:]

            slovo = slovo.replace(".","")
            slovo = slovo.replace(",","") 
            slovo = slovo.replace("!","")
            slovo = slovo.replace(":","") 
            slovo = slovo.replace(";","")
            slovo = slovo.replace('"',"")
            slovo = slovo.replace('?',"")
            slovo = slovo.lower()
            if slovo != "" and not slovo.startswith("#"):
                ocistenaSlova.add(slovo)
    return ocistenaSlova


def porovnej_zajmy(student_a: set[str], student_b: set[str]) -> tuple[set[str], set[str], set[str]]:
    """
    Pomocí množinových operací porovná zájmy nebo dovednosti dvou studentů.

    Návratová hodnota:
    - n-tice (tuple) o 3 prvcích: (spolecne, pouze_a, pouze_b)
      1. spolecne: množina prvků obsažených v obou množinách současně (průnik: A & B)
      2. pouze_a: množina prvků obsažených pouze v množině student_a (rozdíl: A - B)
      3. pouze_b: množina prvků obsažených pouze v množině student_b (rozdíl: B - A)

    Příklad:
        a = {"python", "c++", "linux"}
        b = {"python", "sql", "git"}
        porovnej_zajmy(a, b) -> ({"python"}, {"c++", "linux"}, {"sql", "git"})
    """
    # TODO: Doplňte implementaci
    
    spolecne = student_a & student_b
    pouze_a = student_a - student_b
    pouze_b = student_b - student_a


    return (spolecne, pouze_a, pouze_b)


def katalog_knih(knihy: list[tuple[str, str, int]]) -> dict[str, list[str]]:
    """
    Seskupí knihy ze zadaného seznamu podle jejich žánru.

    Vstup:
    - knihy: seznam n-tic, kde každá n-tice má formát (nazev_knihy, zanr, rok_vydani)

    Pravidla:
    - Výsledkem je slovník (dict[str, list[str]]), kde klíčem je žánr (oříznutý o případné
      bílé znaky na začátku a konci) a hodnotou je seznam názvů knih v tomto žánru.
    - Pořadí knih v seznamu pro daný žánr musí odpovídat původnímu pořadí v předaném seznamu.
    - Pokud je předaný seznam prázdný, funkce vrátí prázdný slovník {}.

    Příklad:
        katalog = [
            ("1984", "Sci-Fi", 1949),
            ("Pán prstenů", "Fantasy", 1954),
            ("Duna", "Sci-Fi", 1965)
        ]
        katalog_knih(katalog) -> {"Sci-Fi": ["1984", "Duna"], "Fantasy": ["Pán prstenů"]}
    """
    # TODO: Doplňte implementaci
    katalog = {}
    for nazev_knihy, zanr, rok_vydani in knihy:
        zanr = zanr.strip()
        #katalog[zanr] = [nazev_knihy]
       #print(nazev_knihy, zanr, rok_vydani)
        if zanr in katalog:
            katalog[zanr].append(nazev_knihy)
        else:
            katalog[zanr] = [nazev_knihy]

    return katalog


def statistika_textu(text: str) -> dict:
    """
    Spočítá souhrnnou statistiku zadaného textu.

    Postup:
    1. Text převeďte na malá písmena.
    2. Odstraňte interpunkční znaménka: ',', '.', '!', '?', ':', ';'
    3. Rozdělte text na slova podle bílých znaků.
    4. Sestavte slovník s následujícími klíči:
       - "pocet_slov": celkový počet slov v textu (int)
       - "pocet_unikatnich": počet různých slov (int)
       - "nejdelsi_slovo": nejdelší nalezené slovo (str). Pokud má více slov stejnou
         maximální délku, vyberte první z nich. Pokud je text prázdný, hodnota je "".
       - "cetnost_delek": slovník (dict[int, int]), kde klíčem je délka slova a hodnotou
         je počet slov v textu s touto délkou.

    Pro prázdný text (nebo text obsahující pouze bílé znaky a interpunkci) vrátí:
       {"pocet_slov": 0, "pocet_unikatnich": 0, "nejdelsi_slovo": "", "cetnost_delek": {}}

    Příklad:
        text = "Rychlá hnědá liška skáče přes líného psa."
        statistika_textu(text) ->
        {
            "pocet_slov": 7,
            "pocet_unikatnich": 7,
            "nejdelsi_slovo": "rychlá",
            "cetnost_delek": {6: 2, 5: 3, 4: 1, 3: 1}
        }
    """
    # TODO: Doplňte implementaci
    text = text.replace(".","")
    text = text.replace(",","") 
    text = text.replace("!","")
    text = text.replace(":","") 
    text = text.replace(";","")
    text = text.replace('?',"")
    text = text.lower()
    slova = text.split()
    #print(slova)
    pocet_slov = len(slova)
    #print(pocet_slov)
    pocet_unikatnich = len(set(slova))
    nejdelsi_slovo = ""
    for slovo in slova:
        if len(slovo) > len(nejdelsi_slovo):
            nejdelsi_slovo = slovo
    cetnost_delek = {}
    for slovo in slova:
        delka = len(slovo)
        if delka in cetnost_delek:
            cetnost_delek[delka] += 1
        else:
            cetnost_delek[delka] = 1



    return {
    "pocet_slov": pocet_slov,
    "pocet_unikatnich": pocet_unikatnich,
    "nejdelsi_slovo": nejdelsi_slovo,
    "cetnost_delek": cetnost_delek
}
    


def main():
    print("=== Testování funkcí Úkolu 2 ===")
    
    text = "Učíme se #Python a #datové_struktury! #python je #super."
    tagy = extrahuj_hashtagy(text)
    print(f"1. Hashtagy: {tagy}")

    a = {"python", "c++", "linux"}
    b = {"python", "sql", "git"}
    spolecne, pouze_a, pouze_b = porovnej_zajmy(a, b)
    print(f"2. Zájmy - Společné: {spolecne}, Pouze A: {pouze_a}, Pouze B: {pouze_b}")

    knihy = [
        ("1984", "Sci-Fi", 1949),
        ("Pán prstenů", "Fantasy", 1954),
        ("Duna", "Sci-Fi", 1965),
        ("Hobit", "Fantasy", 1937)
    ]
    kat = katalog_knih(knihy)
    print(f"3. Katalog podle žánrů: {kat}")

    ukazka = "Rychlá hnědá liška skáče přes líného psa."
    stats = statistika_textu(ukazka)
    print(f"4. Statistika textu: {stats}")


if __name__ == "__main__":
    main()
