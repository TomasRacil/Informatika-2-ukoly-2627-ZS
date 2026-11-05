"""
Úkol 2: Datové struktury – řetězce, množiny, n-tice a slovníky.

Vyplňte těla jednotlivých funkcí podle zadání v komentářích a v README.md.
Neměňte názvy funkcí ani jejich parametry.
"""


def extrahuj_hashtagy(text: str) -> set[str]:
    hashtagy = set()

    for slovo in text.split():
        if slovo.startswith("#"):
            slovo = slovo[1:]
            slovo = slovo.rstrip(',.!?:; "')
            slovo = slovo.lower().lstrip("#")

            if slovo:
                hashtagy.add(slovo)

    return hashtagy



def porovnej_zajmy(student_a: set[str], student_b: set[str]) -> tuple[set[str], set[str], set[str]]:
    spolecne = student_a & student_b
    a = student_a - student_b
    b = student_b - student_a

    return spolecne, a, b


def katalog_knih(knihy: list[tuple[str, str, int]]) -> dict[str, list[str]]:
    katalog = {}

    for nazev, zanr, rok in knihy:
        zanr = zanr.strip()

        if zanr not in katalog:
            katalog[zanr] = []

        katalog[zanr].append(nazev)

    return katalog


def statistika_textu(text: str) -> dict:
    text = text.lower()

    for znak in ",.!?:;":
        text = text.replace(znak, "")

    slova = text.split()

    pocet_slov = len(slova)
    pocet_unikatnich = len(set(slova))
    nejdelsi_slovo = max(slova, key=len, default="")

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
