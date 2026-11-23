# Úkol 2: Datové struktury – řetězce, množiny, n-tice a slovníky

Cílem tohoto úkolu je procvičit práci se základními vestavěnými datovými strukturami jazyka Python: s **textovými řetězci** (`str`), **množinami** (`set`), **n-ticemi** (`tuple`) a **slovníky** (`dict`). Naučíte se extrahovat data z textu, provádět množinové operace a seskupovat a agregovat data do slovníků.

* **Datum zadání:** 14. 10. 2026  
* **Termín odevzdání (deadline):** **20. 10. 2026 (23:59:59)**

---

## Zadání

V souboru `ukol_2.py` naimplementujte 4 samostatné funkce podle níže uvedených specifikací.

### Soubor k úpravě:
* `Ukol_2/ukol_2.py`

*(Ostatní soubory jako `test.py` ani soubory v `.github/` neupravujte).*

---

### Funkce 1: `extrahuj_hashtagy(text: str) -> set[str]`
* **Cíl:** Najít v textu všechny hashtagy (slova uvozená znakem `#`).
* **Pravidla:**
  - Rozdělte text na slova podle mezer pomocí `.split()`.
  - Hashtag je slovo, které začíná znakem `'#'`.
  - Odstraňte úvodní křížek `'#'` a z konce slova odstraňte případnou interpunkci (`,`, `.`, `!`, `?`, `:`, `;`, `"`).
  - Převeďte název tagu na malá písmena (`.lower()`).
  - Pokud po očištění zůstane neprázdný název, přidejte jej do výsledné množiny.
  - Funkce vrátí množinu (`set`) unikátních názvů hashtagů bez znaku `'#'`.
  - Pokud text žádný platný hashtag neobsahuje (nebo je vstup prázdný), vrátí prázdnou množinu `set()`.
* **Příklad:**
  ```python
  text = "Učíme se #Python a #datové_struktury! #python je #super."
  extrahuj_hashtagy(text)
  # Vrací: {"python", "datové_struktury", "super"}
  ```

---

### Funkce 2: `porovnej_zajmy(student_a: set[str], student_b: set[str]) -> tuple[set[str], set[str], set[str]]`
* **Cíl:** Pomocí množinových operací porovnat zájmy nebo dovednosti dvou studentů.
* **Návratová hodnota:** n-tice (`tuple`) obsahující přesně 3 množiny v tomto pořadí:
  1. **Společné zájmy** ($A \cap B$): prvky, které mají v množině oba studenti (průnik).
  2. **Pouze student A** ($A \setminus B$): prvky, které má pouze student A (rozdíl).
  3. **Pouze student B** ($B \setminus A$): prvky, které má pouze student B (rozdíl).
* **Příklad:**
  ```python
  a = {"python", "c++", "linux"}
  b = {"python", "sql", "git"}
  porovnej_zajmy(a, b)
  # Vrací: ({"python"}, {"c++", "linux"}, {"sql", "git"})
  ```

---

### Funkce 3: `katalog_knih(knihy: list[tuple[str, str, int]]) -> dict[str, list[str]]`
* **Cíl:** Seskupit zadané knihy do slovníku podle jejich žánru.
* **Vstup:** Seznam n-tic ve formátu `[(nazev_knihy, zanr, rok_vydani), ...]`.
* **Pravidla:**
  - Funkce vrátí slovník (`dict[str, list[str]]`), kde klíčem je žánr (oříznutý o případné bílé znaky na začátku a konci pomocí `.strip()`) a hodnotou je **seznam názvů knih** v daném žánru.
  - Pořadí názvů knih v seznamu pro daný žánr musí odpovídat původnímu pořadí v předaném seznamu.
  - Pokud je předaný seznam knih prázdný, funkce vrátí prázdný slovník `{}`.
* **Příklad:**
  ```python
  knihy = [
      ("1984", "Sci-Fi", 1949),
      ("Pán prstenů", "Fantasy", 1954),
      ("Duna", "Sci-Fi", 1965),
      ("Hobit", "Fantasy", 1937)
  ]
  katalog_knih(knihy)
  # Vrací:
  # {
  #     "Sci-Fi": ["1984", "Duna"],
  #     "Fantasy": ["Pán prstenů", "Hobit"]
  # }
  ```

---

### Funkce 4: `statistika_textu(text: str) -> dict`
* **Cíl:** Spočítat souhrnnou statistiku zadaného textu.
* **Postup:**
  1. Text převeďte na malá písmena.
  2. Odstraňte interpunkční znaménka: `,`, `.`, `!`, `?`, `:`, `;`.
  3. Rozdělte text na slova podle mezer (`.split()`).
  4. Sestavte a vraťte slovník s přesně těmito klíči:
     - `"pocet_slov"`: celkový počet slov v textu (`int`).
     - `"pocet_unikatnich"`: počet různých (unikátních) slov (`int`).
     - `"nejdelsi_slovo"`: nejdelší nalezené slovo (`str`). Pokud má více slov stejnou maximální délku, vyberte první z nich. Pro prázdný text je hodnota `""`.
     - `"cetnost_delek"`: slovník (`dict[int, int]`), kde klíčem je délka slova a hodnotou počet slov v textu s touto délkou.
* **Ošetření prázdného textu:** Pro prázdný text (nebo text obsahující pouze bílé znaky či interpunkci) vrátí:
  ```python
  {
      "pocet_slov": 0,
      "pocet_unikatnich": 0,
      "nejdelsi_slovo": "",
      "cetnost_delek": {}
  }
  ```
* **Příklad:**
  ```python
  text = "Rychlá hnědá liška skáče přes líného psa."
  statistika_textu(text)
  # Vrací:
  # {
  #     "pocet_slov": 7,
  #     "pocet_unikatnich": 7,
  #     "nejdelsi_slovo": "rychlá",
  #     "cetnost_delek": {6: 2, 5: 3, 4: 1, 3: 1}
  # }
  ```

---

## Lokální testování

Před vytvořením commitu si své řešení lokálně vyzkoušejte:

1. **Vlastní běh programu:**
   ```shell
   cd Ukol_2
   python ukol_2.py
   ```
2. **Spuštění automatických testů:**
   ```shell
   python -m unittest test.py
   ```
   *(Na Linuxu/macOS případně: `python3 -m unittest test.py`)*

Jakmile všechny testy projdou, zobrazí se zpráva:
```text
Ran 17 tests in 0.002s

OK
```

---

## Odevzdání

1. Proveďte commit vašich změn v souboru `Ukol_2/ukol_2.py`.
2. Odešlete změny do vašeho forku (`git push origin master`).
3. Vytvořte Pull Request do vaší větve v repozitáři vyučujícího (`TomasRacil/Informatika-2-ukoly-2627-ZS`) s názvem:  
   `Odevzdani Ukol 2 - Jmeno Prijmeni`.
