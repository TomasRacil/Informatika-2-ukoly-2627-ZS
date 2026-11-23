# Úkol 4: Pokročilý Python – Dědičnost, abstraktní třídy, magické metody, dekorátory, regex a CLI

Cílem tohoto úkolu je procvičit pokročilejší nástroje Pythonu, se kterými se běžně setkáte v praxi:
1. **Vlastní výjimky:** Definice vlastní třídy výjimky děděním z `Exception` a její cílené vyhazování.
2. **Regulární výrazy (`re`):** Ověřování formátu vstupu a vytahování skupin (`match.group(...)`) pomocí modulu `re`.
3. **Dekorátory:** Funkce, která obaluje jinou funkci, ověří její argumenty a používá `@functools.wraps`.
4. **Dědičnost a abstraktní třídy:** `ABC`, `@abstractmethod`, přepisování metod a volání `super().__init__()`.
5. **Magické metody:** `__str__`, `__repr__`, `__eq__`, `__lt__` a `__add__`.
6. **Argumenty příkazové řádky:** Načtení a validace vstupů z terminálu pomocí `argparse`.

* **Datum zadání:** 6. 11. 2026  
* **Termín odevzdání (deadline):** **13. 11. 2026 (23:59:59)**

---

## Zadání

Vytvořte jednoduchý **systém pro kalkulaci a správu zásilek (zásilková služba)**. Systém umí ověřit kód zásilky, hlídat kladné číselné argumenty, spočítat cenu standardní i expresní zásilky a obsloužit volání z příkazové řádky.

V souboru `ukol_4.py` naimplementujte tyto části:
* `NeplatnyKodZasilkyError` a `over_kod_zasilky`
* `over_kladne_argumenty`
* `Zasilka`, `StandardniZasilka` a `ExpresniZasilka`
* `vytvor_parser` a `vytvor_zasilku_z_argumentu`

### Soubor k úpravě:
* `Ukol_4/ukol_4.py`

*(Ostatní soubory jako `test.py` ani soubory v `.github/` neupravujte).*

---

### Část 1: Vlastní výjimka a validace kódu zásilky

Každá zásilka má svůj **kód** v jednotném formátu, např. `CZ-123456-STD`. Kód se skládá ze tří částí oddělených pomlčkami:

| Skupina | Význam | Formát |
| :---: | :--- | :--- |
| 1 | Kód země | přesně 2 velká písmena (např. `CZ`, `SK`, `PL`, `DE`) |
| 2 | Číslo zásilky | přesně 6 číslic (`0`–`9`) |
| 3 | Kód typu služby | přesně 3 velká písmena (`STD` nebo `EXP`) |

* **Třída `NeplatnyKodZasilkyError(Exception)`:** Vlastní výjimka pro neplatný kód zásilky. Tělo třídy může být pouze `pass`.

* **Funkce `over_kod_zasilky(kod: str) -> dict[str, str]`:**
  - Ověří, zda `kod` odpovídá regulárnímu výrazu:
    ```python
    r"^([A-Z]{2})-(\d{6})-([A-Z]{3})$"
    ```
  - Pokud kód **neodpovídá** formátu (chybí pomlčky, malá písmena, jiný počet číslic, jinak dlouhý suffix apod.), vyvolá:
    ```python
    NeplatnyKodZasilkyError("Neplatný formát kódu zásilky.")
    ```
  - Pokud kód **odpovídá**, vrátí slovník s jednotlivými skupinami:
    ```python
    {"zeme": m.group(1), "cislo": m.group(2), "typ": m.group(3)}
    ```
    kde `m` je výsledek porovnání (`re.match`). Např. pro `"SK-987654-EXP"` vrátí
    `{"zeme": "SK", "cislo": "987654", "typ": "EXP"}`.
  - Pro vyhledání použijte `re.match(...)` (případně `re.fullmatch` s upraveným vzorem) a výsledek ošetřete, protože při neúspěchu vrací `None`.

---

### Část 2: Dekorátor `over_kladne_argumenty`

* **Funkce `over_kladne_argumenty(func: Callable[..., Any]) -> Callable[..., Any]`:**
  - Jedná se o **dekorátor** – přijme funkci a vrátí novou (vnořenou) funkci `wrapper`, která obalí tu původní.
  - Uvnitř `wrapper` projděte **všechny poziční argumenty** (`*args`) i **všechny klíčové argumenty** (`**kwargs`).
  - Pokud je některý argument **číselný** (`int` nebo `float`) a jeho hodnota je `<= 0`, vyvolá:
    ```python
    ValueError("Číselný argument musí být kladný.")
    ```
  - **Pozor na `bool`:** v Pythonu je `bool` podtřídou `int` (`True == 1`, `False == 0`). Logické hodnoty se za čísla nepovažují, proto použijte například `type(x) in (int, float)` nebo `isinstance(x, (int, float)) and not isinstance(x, bool)`.
  - **Nečíselné** argumenty (např. `str`, seznamy) se ignorují a nikdy nevyvolají chybu.
  - Pokud jsou všechny číselné argumenty kladné, zavolejte původní funkci (`func(*args, **kwargs)`) a **její návratovou hodnotu vraťte**.
  - Na vnořenou funkci použijte `@functools.wraps(func)`, aby se zachovalo jméno a docstring původní funkce.
  - Dekorátor musí fungovat i pro funkce bez argumentů a pro kombinaci pozičních a klíčových argumentů.

Příklad použití:

```python
@over_kladne_argumenty
def obsah_obdelniku(a: float, b: float) -> float:
    """Vypočítá obsah obdélníku."""
    return a * b

obsah_obdelniku(2.0, 3.0)      # 6.0
obsah_obdelniku(2.0, b=-1.0)   # ValueError
```

---

### Část 3: Abstraktní třída `Zasilka` a odvozené třídy

#### Třída `Zasilka(ABC)`

Abstraktní předek všech zásilek. Nelze ji přímo vytvořit (obsahuje abstraktní metodu).

* **Konstruktor `__init__(self, kod: str, hmotnost_kg: float) -> None`:**
  - Ověří, že `kod` po odstranění bílých znaků (`.strip()`) není prázdný. Pokud je prázdný, vyvolá `ValueError("Kód zásilky nesmí být prázdný.")`.
  - Ověří, že `hmotnost_kg > 0`. Pokud ne, vyvolá `ValueError("Hmotnost musí být kladná.")`.
  - Uloží `self.kod = kod.strip()` a `self.hmotnost_kg = float(hmotnost_kg)`.

* **`@abstractmethod def spocitej_cenu(self) -> float`:** Abstraktní metoda, tělo pouze `pass`. Každá odvozená třída ji musí implementovat.

* **`__str__(self) -> str`:** Vrátí textový popis ve formátu:
  ```
  "Zásilka {kod} [{cena:.2f} Kč]"
  ```
  *(např. `"Zásilka CZ-123456-STD [97.50 Kč]"`)*.

* **`__repr__(self) -> str`:** Vrátí jednoznačnou reprezentaci ve formátu:
  ```
  f"{self.__class__.__name__}(kod='{self.kod}', hmotnost_kg={self.hmotnost_kg})"
  ```
  *(např. `"StandardniZasilka(kod='CZ-123456-STD', hmotnost_kg=2.5)"`)*.

* **`__eq__(self, other: object) -> bool`:** Dvě zásilky jsou si rovny, pokud:
  - `other` je instance třídy `Zasilka` **a zároveň**
  - obě mají **stejnou konkrétní třídu** (`self.__class__ == other.__class__`) **a zároveň**
  - mají **stejný kód** (`self.kod == other.kod`).
  
  V opačném případě vraťte `False`.

* **`__lt__(self, other: object) -> bool`:** Porovnání „menší než“ podle ceny.
  - Pokud `other` je instance `Zasilka`, vraťte `self.spocitej_cenu() < other.spocitej_cenu()`.
  - Jinak vraťte `NotImplemented` (Python pak vyvolá `TypeError`).

* **`__add__(self, other: object) -> float`:** Součet cen dvou zásilek.
  - Pokud `other` je instance `Zasilka`, vraťte `self.spocitej_cenu() + other.spocitej_cenu()`.
  - Jinak vraťte `NotImplemented`.

#### Třída `StandardniZasilka(Zasilka)`

* **Konstruktor `__init__(self, kod: str, hmotnost_kg: float) -> None`:**
  - Zavolá `super().__init__(kod, hmotnost_kg)`.

* **`spocitej_cenu(self) -> float`:**
  - Základní cena je 60 Kč, za každý kilogram se připočítá 15 Kč.
  - Vrácenou hodnotu zaokrouhlete na 2 desetinná místa:
    ```python
    round(60.0 + self.hmotnost_kg * 15.0, 2)
    ```

#### Třída `ExpresniZasilka(Zasilka)`

* **Konstruktor `__init__(self, kod: str, hmotnost_kg: float, priplatek: float = 100.0) -> None`:**
  - Zavolá `super().__init__(kod, hmotnost_kg)`.
  - Ověří, že `priplatek >= 0`. Pokud je záporný, vyvolá `ValueError("Příplatek nesmí být záporný.")`.
  - Uloží `self.priplatek = float(priplatek)`.

* **`spocitej_cenu(self) -> float`:**
  - Základní cena je 60 Kč, za každý kilogram se připočítá 25 Kč (expres je dražší) a k tomu se přičte příplatek.
  - Vrácenou hodnotu zaokrouhlete na 2 desetinná místa:
    ```python
    round((60.0 + self.hmotnost_kg * 25.0) + self.priplatek, 2)
    ```

---

### Část 4: Příkazová řádka s `argparse`

* **Funkce `vytvor_parser() -> argparse.ArgumentParser`:**
  - Vytvoří a vrátí parser s `description="Systém pro kalkulaci a správu zásilek"`.
  - Poziční argument `"kod"`: `type=str`, `help="Kód zásilky"`.
  - Poziční argument `"hmotnost"`: `type=float`, `help="Hmotnost zásilky v kg"`.
  - Volitelný argument `"--typ"`, zkratka `"-t"`: `type=str`, `choices=["standard", "expres"]`, `default="standard"`, `help="Typ zásilky"`.
  - Volitelný argument `"--priplatek"`, zkratka `"-p"`: `type=float`, `default=100.0`, `help="Expresní příplatek"`.
  - Pro přidání argumentů použijte `parser.add_argument(...)`.

* **Funkce `vytvor_zasilku_z_argumentu(args: argparse.Namespace) -> Zasilka`:**
  - Pokud `args.typ == "standard"`, vytvoří a vrátí `StandardniZasilka(args.kod, args.hmotnost)`.
  - Pokud `args.typ == "expres"`, vytvoří a vrátí `ExpresniZasilka(args.kod, args.hmotnost, priplatek=args.priplatek)`.
  - Vytvořený objekt vraťte (nevypisujte ho).

* **Blok `if __name__ == "__main__":`:** Ukázka použití – vytvořte parser, načtěte argumenty pomocí `parser.parse_args()`, vytvořte zásilku pomocí `vytvor_zasilku_z_argumentu(args)` a vypište ji funkcí `print(...)`. Ošetřete `NeplatnyKodZasilkyError` a `ValueError` pomocí `try/except` a vypište srozumitelnou chybovou zprávu (např. na `sys.stderr`).

Ukázkové spuštění z terminálu:

```shell
python ukol_4.py CZ-123456-STD 2.5
python ukol_4.py SK-987654-EXP 3.0 --typ expres --priplatek 150
python ukol_4.py DE-000001-STD 1.2 -t expres -p 50
```

---

## Lokální testování

Před odesláním řešení ověřte, že všechny testy procházejí:

```shell
cd Ukol_4
python -m unittest test.py
```
*(Na Linuxu/macOS případně: `python3 -m unittest test.py`)*

Testy musí projít se zprávou **`OK`**.
