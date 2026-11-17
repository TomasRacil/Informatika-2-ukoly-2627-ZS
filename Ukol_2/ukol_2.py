"""
Úkol 2: Datové struktury – řetězce, množiny, n-tice a slovníky.

Vyplňte těla jednotlivých funkcí podle zadání v komentářích a v README.md.
Neměňte názvy funkcí ani jejich parametry.
"""


def extrahuj_hashtagy(text: str) -> set[str]:
    
    save = set()
    x = text.split()
    for slova in x:
        if slova.startswith('#') and len(slova) > 1:
            cisty = slova[1:].rstrip(',.!?:;"').lower()
    
            if cisty and cisty != '#':
                save.add(cisty)
    return save


def porovnej_zajmy(student_a: set[str], student_b: set[str]) -> tuple[set[str], set[str], set[str]]:
    
    spolecne = set()
    for x in student_a:
        for y in student_b:
            if x==y:
                spolecne.add(x)
    

    pouze_a = set()
    for x in student_a:
            if x not in student_b:
                pouze_a.add(x)

    pouze_b = set()
    for x in student_b:
                if x not in student_a:
                    pouze_b.add(x)
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
    return (spolecne, pouze_a, pouze_b)


def katalog_knih(knihy: list[tuple[str, str, int]]) -> dict[str, list[str]]:

     konecne={}

     for k in knihy:
         nazev = k[0]
         zanr = k[1]

         zanr = zanr.strip()
         if zanr not in konecne:
             konecne[zanr] = []
         konecne[zanr].append(nazev)
   
    #TODO: Doplňte implementaci
     return konecne
def katalog_knih(knihy: list[tuple[str, str, int]]) -> dict[str, list[str]]:

     konecne={}

     for k in knihy:
         nazev = k[0]
         zanr = k[1]

         zanr = zanr.strip()

         if zanr not in konecne:
             konecne[zanr] = []

         konecne[zanr].append(nazev)
   
    #TODO: Doplňte implementaci
     return konecne


def statistika_textu(text: str) -> dict:
     if text==0:
        return {
            "pocet_slov": 0,
              "pocet_unikatnich": 0, 
              "nejdelsi_slovo": "", 
            "cetnost_delek": {}
        }
     else:
        text =text.lower()
        text = text.split()
        slova = []
        for s in text:
         cista = s.rstrip(',.!?:;')
         if cista:
           slova.append(cista)

        if not slova:
            return {
                        "pocet_slov": 0,
                          "pocet_unikatnich": 0, 
                          "nejdelsi_slovo": "", 
                        "cetnost_delek": {}
                    }
           
   
    
        else:
            pocet_slov:int
            pocet_slov = len(slova)

            unikatni = set(slova)
            pocet_unikatnich = len(unikatni)

            nejdelsi_slovo = slova[0]
            for x in slova:
             if len(nejdelsi_slovo)< len(x):
                nejdelsi_slovo = x

            cetnost_delek = {}
            for z in slova:
             delka = len(z)

             if delka in cetnost_delek:
                 cetnost_delek[delka]+=1

             else:
                cetnost_delek[delka] = 1
    
   
    # TODO: Doplňte implementaci
        return {
            "pocet_slov": pocet_slov,
            "pocet_unikatnich": pocet_unikatnich,
            "nejdelsi_slovo": f"{nejdelsi_slovo}",
            "cetnost_delek": cetnost_delek
         }
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

    ukazka = "Rychlá hnědá liška ? skáče přes líného psa."
    stats = statistika_textu(ukazka)
    print(f"4. Statistika textu: {stats}")


if __name__ == "__main__":
    main()
