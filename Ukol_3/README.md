# Úkol 3: Objektově orientované programování – třídy, typové anotace a vlastnosti

Cílem tohoto úkolu je procvičit základní pilíře **Objektově orientovaného programování (OOP)** v Pythonu:
1. **Tvorba tříd a objektů:** Konstruktor `__init__`, instance třídy, parametr `self` a metody.
2. **Type Hinting (typové anotace):** Správné anotování parametrů, návratových hodnot a atributů.
3. **Zapouzdření a Vlastnosti (`@property`):** Chráněné atributy (`_nazev`), gettery, settery s validací vstupních dat (vyvolání `ValueError`) a vypočítané vlastnosti (pouze pro čtení).

* **Datum zadání:** 27. 10. 2026  
* **Termín odevzdání (deadline):** **3. 11. 2026 (23:59:59)**

---

## Zadání

V souboru `ukol_3.py` naimplementujte 3 samostatné třídy podle níže uvedených specifikací:
* `Kniha`
* `PolozkaSkladu`
* `Student`

### Soubor k úpravě:
* `Ukol_3/ukol_3.py`

*(Ostatní soubory jako `test.py` ani soubory v `.github/` neupravujte).*

---

### Třída 1: `Kniha`

Reprezentuje knihu s názvem, autorem, počtem stran a cenou.

* **Konstruktor `__init__(self, nazev: str, autor: str, pocet_stran: int, cena: float) -> None`:**
  - Inicializuje vnitřní chráněné atributy `_nazev`, `_autor`, `_pocet_stran`, `_cena`.
  - **Doporučení:** Hodnoty v `__init__` přiřazujte přímo přes property (např. `self.nazev = nazev`), aby proběhla veškerá validace i při vytvoření instance.

* **Vlastnost `nazev` (`@property` + setter):**
  - Getter vrátí název knihy (`str`).
  - Setter ověří, že zadaná hodnota je neprázdný řetězec i po odstranění bílých znaků (`.strip()`).
  - Uloží oříznutý řetězec. Pokud je prázdný, vyvolá výjimku `ValueError("Název nesmí být prázdný.")`.

* **Vlastnost `autor` (`@property` + setter):**
  - Getter vrátí jméno autora (`str`).
  - Setter ověří, že zadaná hodnota po `.strip()` není prázdná, a uloží oříznutý řetězec.
  - Pokud je prázdná, vyvolá `ValueError("Autor nesmí být prázdný.")`.

* **Vlastnost `pocet_stran` (`@property` + setter):**
  - Getter vrátí počet stran (`int`).
  - Setter ověří, že hodnota je kladné celé číslo $> 0$.
  - Pokud ne, vyvolá `ValueError("Počet stran musí být kladné číslo.")`.

* **Vlastnost `cena` (`@property` + setter):**
  - Getter vrátí cenu (`float`).
  - Setter ověří, že cena je nezáporná ($\ge 0$). Kniha může mít cenu 0 (např. zdarma).
  - Pokud je záporná, vyvolá `ValueError("Cena nesmí být záporná.")`.

* **Metoda `sleva(self, procento: float) -> None`:**
  - Zlevní knihu o zadané procento ($0 \le procento \le 100$).
  - Novou cenu spočítá a zaokrouhlí na 2 desetinná místa pomocí `round(..., 2)`.
  - Pokud je hodnota `procento` mimo interval 0 až 100, vyvolá `ValueError("Sleva musí být v rozmezí 0 až 100 %.")`.

* **Metoda `__str__(self) -> str`:**
  - Vrátí textový popis ve formátu:  
    `"{nazev} ({autor}) - {pocet_stran} str., {cena} Kč"`  
    *(např. `"1984 (George Orwell) - 328 str., 299.0 Kč"`)*.

---

### Třída 2: `PolozkaSkladu`

Reprezentuje položku zboží evidovanou na skladě.

* **Konstruktor `__init__(self, kod: str, nazev: str, cena_za_kus: float, pocet_kusu: int = 0) -> None`:**
  - Inicializuje chráněné atributy `_kod`, `_nazev`, `_cena_za_kus`, `_pocet_kusu`.
  - Výchozí hodnota `pocet_kusu` je `0`.
  - Pro atributy využijte příslušné settery pro zajištění validace.

* **Vlastnost `kod` (`@property` – pouze getter):**
  - Vrátí kód položky (`str`). Kód položky je neměnný (nemá setter).

* **Vlastnost `nazev` (`@property` + setter):**
  - Getter i setter pro název zboží (`str`).
  - Setter ověří, že název po `.strip()` není prázdný, jinak vyvolá `ValueError("Název nesmí být prázdný.")`.

* **Vlastnost `cena_za_kus` (`@property` + setter):**
  - Getter i setter pro jednotkovou cenu (`float`).
  - Musí být $\ge 0$, jinak vyvolá `ValueError("Cena za kus nesmí být záporná.")`.

* **Vlastnost `pocet_kusu` (`@property` + setter):**
  - Getter i setter pro počet kusů (`int`).
  - Musí být nezáporné celé číslo $\ge 0$, jinak vyvolá `ValueError("Počet kusů nesmí být záporný.")`.

* **Vlastnost `hodnota_zasob` (`@property` – pouze getter):**
  - Vypočítaná vlastnost bez setteru.
  - Vrátí celkovou finanční hodnotu dané položky na skladě: `cena_za_kus * pocet_kusu`, zaokrouhlenou na 2 desetinná místa (`float`).

* **Metoda `prijem(self, pocet: int) -> None`:**
  - Přijme na sklad zadaný počet kusů (`_pocet_kusu += pocet`).
  - Pokud je `pocet <= 0`, vyvolá `ValueError("Počet kusů pro příjem musí být kladný.")`.

* **Metoda `vydej(self, pocet: int) -> bool`:**
  - Pokusí se vydat (odečíst) zadaný počet kusů ze skladu.
  - Pokud je `pocet <= 0`, vyvolá `ValueError("Počet kusů pro výdej musí být kladný.")`.
  - Pokud je na skladě dostatečné množství (`self.pocet_kusu >= pocet`), sníží počet kusů o `pocet` a vrátí `True`.
  - Pokud na skladě dostatek kusů není, počet kusů se nezmění a metoda vrátí `False`.

---

### Třída 3: `Student`

Reprezentuje studenta, jeho ročník a evidenci známek.

* **Konstruktor `__init__(self, jmeno: str, rocnik: int) -> None`:**
  - Inicializuje chráněné atributy `_jmeno`, `_rocnik` a seznam známek `_znamky: list[int]`.
  - Seznam `_znamky` je při vytvoření studenta vždy prázdný (`[]`).
  - Inicializace `jmeno` a `rocnik` probíhá přes settery.

* **Vlastnost `jmeno` (`@property` + setter):**
  - Getter i setter pro jméno (`str`). Po oříznutí mezer nesmí být prázdné, jinak `ValueError("Jméno studenta nesmí být prázdné.")`.

* **Vlastnost `rocnik` (`@property` + setter):**
  - Getter i setter pro ročník studia (`int`).
  - Povolené hodnoty jsou celé číslo 1 až 5 ($1 \le rocnik \le 5$). V opačném případě vyvolá `ValueError("Neplatný ročník (povolené hodnoty 1-5).")`.

* **Vlastnost `znamky` (`@property` – pouze getter):**
  - Vrátí **kopii** seznamu známek (`list(self._znamky)`), aby vnější kód nemohl nekontrolovaně modifikovat vnitřní stav přes referenci.

* **Metoda `pridej_znamku(self, znamka: int) -> None`:**
  - Přidá známku do seznamu `_znamky`.
  - Známka musí být celé číslo v rozsahu 1 až 5 ($1 \le znamka \le 5$).
  - Pokud hodnota není v rozsahu 1 až 5, vyvolá `ValueError("Známka musí být v rozsahu 1 až 5.")`.

* **Vlastnost `prumer` (`@property` – pouze getter):**
  - Vrátí aritmetický průměr všech známek zaokrouhlený na 2 desetinná místa pomocí `round(..., 2)`.
  - Pokud student dosud nemá žádné známky, vrátí `0.0`.

* **Vlastnost `prospel` (`@property` – pouze getter):**
  - Vrátí logickou hodnotu `bool`:
    * Pokud student nemá žádné známky, vrátí `True`.
    * Pokud má alespoň jednu známku 5, vrátí `False`.
    * Pokud je jeho studijní průměr $\le 3.0$ (a nemá žádnou 5), vrátí `True`.
    * Pokud je průměr $> 3.0$, vrátí `False`.

---

## Lokální testování

Před odesláním řešení ověřte, že všechny testy procházejí:

```shell
cd Ukol_3
python -m unittest test.py
```
*(Na Linuxu/macOS případně: `python3 -m unittest test.py`)*

Testy musí projít se zprávou **`OK`**.
