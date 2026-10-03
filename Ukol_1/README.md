# Úkol 1: Základy Pythonu – proměnné, operátory, větvení a cykly

Cílem tohoto úkolu je procvičit si základní stavební kameny programování v Pythonu: práci s proměnnými a čísly, aritmetické operátory, větvení programu pomocí podmínek `if-elif-else` a opakování kódu pomocí cyklů `for` a `while`.

---

## Zadání

V souboru `ukol_1.py` naimplementujte 4 samostatné funkce podle níže uvedených specifikací.

### Soubor k úpravě:
* `Ukol_1/ukol_1.py`

*(Ostatní soubory jako `test.py` ani soubory v `.github/` neupravujte).*

---

### Funkce 1: `vypocet_bmi(vaha_kg: float, vyska_m: float) -> float`
* **Cíl:** Spočítat Body Mass Index podle vzorce:
  $$\text{BMI} = \frac{\text{vaha\_kg}}{(\text{vyska\_m})^2}$$
* **Návratová hodnota:** Hodnota BMI zaokrouhlená na 2 desetinná místa pomocí funkce `round(bmi, 2)`.
* **Ošetření neplatných hodnot:** Pokud je váha $\le 0$ nebo výška $\le 0$, funkce vrátí `0.0`.
* **Příklad:**
  ```python
  vypocet_bmi(75.0, 1.80)  # vrací 23.15
  vypocet_bmi(0, 1.70)     # vrací 0.0
  ```

---

### Funkce 2: `kategorie_bmi(bmi: float) -> str`
* **Cíl:** Na základě vypočtené hodnoty BMI určit slovní kategorii:
  - $\text{BMI} < 18.5$: `"podvaha"`
  - $18.5 \le \text{BMI} < 25.0$: `"normalni"`
  - $25.0 \le \text{BMI} < 30.0$: `"nadvaha"`
  - $\text{BMI} \ge 30.0$: `"obezita"`
* **Ošetření neplatných hodnot:** Pokud je hodnota $\text{BMI} \le 0$, vrátí řetězec `"neplatna hodnota"`.
* **Příklad:**
  ```python
  kategorie_bmi(23.15)  # vrací "normalni"
  kategorie_bmi(28.4)   # vrací "nadvaha"
  kategorie_bmi(-5)     # vrací "neplatna hodnota"
  ```

---

### Funkce 3: `soucet_sudych(start: int, stop: int) -> int`
* **Cíl:** Pomocí cyklu `for` a funkce `range()` spočítat součet všech **sudých celých čísel** v uzavřeném intervalu od `start` do `stop` včetně.
* **Pravidla:**
  - Pokud je `start > stop`, funkce vrátí `0`.
  - Správně funguje i pro záporná čísla a nulu (nula je sudé číslo).
* **Příklady:**
  ```python
  soucet_sudych(1, 10)   # 2 + 4 + 6 + 8 + 10 = 30
  soucet_sudych(2, 6)    # 2 + 4 + 6 = 12
  soucet_sudych(5, 5)    # žádné sudé číslo -> 0
  soucet_sudych(4, 4)    # jediné sudé číslo -> 4
  soucet_sudych(10, 1)   # start > stop -> 0
  soucet_sudych(-4, 2)   # -4 + (-2) + 0 + 2 = -4
  ```

---

### Funkce 4: `pocet_kroku_collatz(n: int) -> int`
* **Cíl:** Pomocí cyklu `while` spočítat, kolik kroků trvá, než kladné celé číslo $n$ dosáhne hodnoty $1$ podle pravidel **Collatzovy posloupnosti**:
  - Je-li aktuální číslo sudé, vydělte ho 2: `n = n // 2`
  - Je-li aktuální číslo liché, vynásobte ho 3 a přičtěte 1: `n = 3 * n + 1`
  - V každém kroku zvyšte počítadlo o 1.
* **Pravidla:**
  - Pro počáteční $n \le 1$ vrátí `0` (pro $1$ není potřeba žádný krok, záporná čísla a nula jsou mimo definici).
* **Příklad pro $n = 6$:**
  Postup: $6 \rightarrow 3 \rightarrow 10 \rightarrow 5 \rightarrow 16 \rightarrow 8 \rightarrow 4 \rightarrow 2 \rightarrow 1$ (celkem 8 kroků).
  ```python
  pocet_kroku_collatz(1)  # vrací 0
  pocet_kroku_collatz(2)  # vrací 1 (2 -> 1)
  pocet_kroku_collatz(6)  # vrací 8
  pocet_kroku_collatz(7)  # vrací 16
  ```

---

## Lokální testování

Před vytvořením commitu si své řešení lokálně vyzkoušejte:

1. **Vlastní běh programu:**
   ```shell
   cd Ukol_1
   python ukol_1.py
   ```
2. **Spuštění automatických testů:**
   ```shell
   python -m unittest test.py
   ```
   *(Na Linuxu/macOS případně použijte `python3 -m unittest test.py`)*

Jakmile všechny testy projdou, zobrazí se zpráva:
```text
Ran 12 tests in 0.002s

OK
```

---

## Odevzdání úkolu

1. Vytvořte novou větev nebo pracujte ve své studentské větvi:
   ```shell
   git add ukol_1.py
   git commit -m "Reseni Ukol 1 - Jmeno Prijmeni"
   git push origin master
   ```
2. Na GitHubu otevřete **Pull Request** do repozitáře vyučujícího podle pokynů v [hlavním README.md](../README.md).
3. Sledujte výsledek automatických testů v Pull Requestu.
