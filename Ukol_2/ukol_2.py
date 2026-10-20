"""
Úkol 2: Datové struktury – řetězce, množiny, n-tice a slovníky.

Vyplňte těla jednotlivých funkcí podle zadání v komentářích a v README.md.
Neměňte názvy funkcí ani jejich parametry.
"""


def extrahuj_hashtagy(text: str) -> set[str]:
    """
    Z textu vyextrahuje všechny hashtagy (slova začínající znakem '#').
    """
    vysledek = set()
    interpunkce = (',', '.', '!', '?', ':', ';', '"')
    
    for slovo in text.split():
        if slovo.startswith('#'):
            ciste = slovo[1:]
            ciste = ciste.rstrip(''.join(interpunkce))
            ciste = ciste.lower()
            
            if ciste and ciste != '#':
                vysledek.add(ciste)
                
    return vysledek


def porovnej_zajmy(student_a: set[str], student_b: set[str]) -> tuple[set[str], set[str], set[str]]:
    """
    Pomocí množinových operací porovná zájmy nebo dovednosti dvou studentů.
    """
    spolecne = student_a & student_b
    pouze_a = student_a - student_b
    pouze_b = student_b - student_a
    
    return (spolecne, pouze_a, pouze_b)


def katalog_knih(knihy: list[tuple[str, str, int]]) -> dict[str, list[str]]:
    """
    Seskupí knihy ze zadaného seznamu podle jejich žánru.
    """
    vysledek = {}
    
    for nazev, zanr, _ in knihy:
        cisty_zanr = zanr.strip()
        if cisty_zanr not in vysledek:
            vysledek[cisty_zanr] = []
        vysledek[cisty_zanr].append(nazev)
        
    return vysledek


def statistika_textu(text: str) -> dict:
    """
    Spočítá souhrnnou statistiku zadaného textu.
    """
    upraveny_text = text.lower()
    
    interpunkce = (',', '.', '!', '?', ':', ';')
    for znak in interpunkce:
        upraveny_text = upraveny_text.replace(znak, '')
        
    slova = upraveny_text.split()
    
    if not slova:
        return {
            "pocet_slov": 0,
            "pocet_unikatnich": 0,
            "nejdelsi_slovo": "",
            "cetnost_delek": {}
        }
        
    pocet_slov = len(slova)
    pocet_unikatnich = len(set(slova))
    
    nejdelsi_slovo = slova[0]
    for slovo in slova[1:]:
        if len(slovo) > len(nejdelsi_slovo):
            nejdelsi_slovo = slovo
            
    cetnost_delek = {}
    for slovo in slova:
        delka = len(slovo)
        cetnost_delek[delka] = cetnost_delek.get(delka, 0) + 1
        
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