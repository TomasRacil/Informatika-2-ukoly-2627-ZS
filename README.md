# Informatika 2 – Úkoly 2026/2027 ZS (Python)

Tento repozitář slouží jako centrální místo pro zadávání, automatické testování a odevzdávání vašich úkolů.

V tomto semestru se zaměřujeme na programovací jazyk **Python**. Úkoly budou v průběhu semestru postupně přibývat.

---

## 📌 Pravidla a podmínky zápočtu

* **Povinnost úkolů:** Všechny zadané úkoly jsou **povinné pro udělení zápočtu**.
* **Termíny odevzdání:** Úkoly **musí být odevzdány v termínu** (standardně do data zadání následujícího úkolu).
* **Vztah ke zkoušce:** Za úkoly se nepřičítají body ke zkoušce. Úkoly slouží k průběžnému osvojení látky a k praktickému ověření dovedností pro zápočet. Výslednou známku určuje zkouška.
* **Integrita:** Úkoly vypracovávejte samostatně. **Nikdy neměňte testovací soubory (`test.py`) ani konfigurační soubory GitHub Actions!** Změny těchto souborů jsou automaticky detekovány a znamenají neuznání úkolu.

---

## 🚀 Postup pro odevzdávání úkolů (Krok za krokem)

Odevzdávání probíhá pomocí **Gitu, GitHubu a Pull Requestů**, se kterým se běžně setkáte v profesionální praxi.

```text
[Původní repozitář vyučujícího]  <--- Pull Request ---  [Váš Fork na GitHubu]
             |                                                  ^
             |  Fork (pouze na začátku)                         |  git push
             v                                                  |
     [Lokální klon / Codespaces] --------------------------------
         (úprava kódu + testy)
```

### 1. Forknutí repozitáře (pouze jednou na začátku semestru)
1. V pravém horním rohu této stránky klikněte na tlačítko **Fork**.
2. **Repository name:** Pojmenujte repozitář tak, aby bylo jasné, komu patří, např. `Informatika-2-ukoly-2627-ZS-VaseJmeno`.
3. Ponechte zaškrtnutou volbu **Copy the `master` branch only**.
4. Klikněte na **Create fork**.

---

### 2. Prvotní konfigurace Gitu (Nastavení identity)

Pokud pracujete na novém počítači nebo v prostředí GitHub Codespaces poprvé, je nutné Gitu nastavit vaše jméno a e-mail. Bez tohoto nastavení vám Git nedovolí vytvářet commity (`Author identity unknown`).

Otevřete terminál a zadejte:

```shell
# Nastavení vašeho celého jména (zobrazí se u vašich odevzdaných commitů):
git config --global user.name "Jméno Příjmení"

# Nastavení e-mailu (MUSÍ se shodovat s e-mailem na vašem GitHub účtu):
git config --global user.email "vas-email@domena.cz"
```

> **Důležité:** Použijte stejný e-mail, jaký máte zaregistrovaný na svém účtu na GitHubu (*Settings -> Emails*). Jinak GitHub nepropojí vaše commity s vaším profilem.

**Doporučená volitelná nastavení:**
```shell
# Výchozí název hlavní větve:
git config --global init.defaultBranch master

# Správné zakončování řádků (prevence chyb CRLF vs LF):
# Na Windows:
git config --global core.autocrlf true
# Na Linuxu a macOS:
git config --global core.autocrlf input
```

Správnost nastavení můžete zkontrolovat příkazem:
```shell
git config --list
```

---

### 3. Možnosti vývojového prostředí

Máte tři možnosti, jak s kódem pracovat:

* **A) GitHub Codespaces (Přímo v prohlížeči – bez instalace na PC):**  
  Nejjednodušší cesta, pokud nechcete na svůj počítač nic instalovat nebo nemáte dostatečná oprávnění.  
  1. Ve svém forknutém repozitáři na GitHubu klikněte na zelené tlačítko **Code**.  
  2. Přepněte se na záložku **Codespaces** a klikněte na **Create codespace on master**.  
  3. Během minut se přímo ve vašem webovém prohlížeči otevře plnohodnotné VS Code prostředí se všemi nástroji a terminálem.

* **B) Dev Container ve VS Code (Doporučeno pro práci s Dockerem):**  
  Pokud máte nainstalovaný **Docker Desktop** a **VS Code** s rozšířením *Dev Containers*:  
  1. Naklonujte si svůj fork do PC:  
     ```shell
     git clone https://github.com/<VaseGitHubJmeno>/Informatika-2-ukoly-2627-ZS-VaseJmeno.git
     cd Informatika-2-ukoly-2627-ZS-VaseJmeno
     code .
     ```
  2. VS Code automaticky rozpozná konfiguraci a v pravém dolním rohu vám nabídne **"Reopen in Container"**. Klikněte na něj. Vše běží v izolovaném kontejneru se správnou verzí Pythonu.

* **C) Běžná lokální instalace Pythonu:**  
  Ujistěte se, že máte nainstalovaný Python (verze 3.10 nebo novější) a naklonujte repozitář (viz výše).  
  Doporučujeme vytvořit lokální virtuální prostředí:  
  ```shell
  python -m venv .venv
  # Aktivace na Windows (PowerShell):
  .\.venv\Scripts\Activate.ps1
  # Aktivace na Linux/macOS:
  source .venv/bin/activate
  ```

---

### 4. Vypracování libovolného úkolu
1. Otevřete složku se zadaným úkolem (např. `Ukol_0`, `Ukol_1`, ...).
2. Pečlivě si přečtěte zadání v souboru `README.md` v dané složce.
3. Upravte zadané zdrojové soubory v Pythonu podle pokynů.
4. **Důležité:** Neupravujte soubory `test.py` ani soubory v `.github/`.

---

### 5. Lokální otestování
Před odesláním řešení si vždy ověřte, že vaše implementace splňuje všechny připravené testy.

V terminálu přejděte do složky aktuálního úkolu a spusťte:

```shell
cd Ukol_X
python -m unittest test.py
```
*(Na Linuxu/macOS případně: `python3 -m unittest test.py`)*

Testy musí projít se souhrnným stavem **`OK`**. Pokud některý test selže, prostudujte výpis chyby (AssertionError), kód opravte a test spusťte znovu.

---

### 6. Commit a Push do vašeho forku
Jakmile máte řešení hotové a testy lokálně procházejí:

```shell
# Přidejte změněné soubory daného úkolu:
git add Ukol_X/

# Vytvořte commit s popisem:
git commit -m "Odevzdani Ukol X"

# Nahrajte změny do svého forku na GitHubu:
git push origin master
```

> **Poznámka k termínům:** Čas vašeho commitu na forknutém repozitáři slouží jako průkazný čas odevzdání v termínu.

---

### 7. Vytvoření Pull Requestu (PR)
1. Přejděte ve webovém prohlížeči na svůj forknutý repozitář na GitHubu.
2. Přejděte do záložky **Pull requests** a klikněte na **New pull request**.
3. **Nastavení větví (pozor na správný směr!):**
   * **base repository:** `TomasRacil/Informatika-2-ukoly-2627-ZS` (původní repozitář vyučujícího)
   * **base branch:** Větev s **vaším jménem** (např. `NovakJan`). *Větve pro jednotlivé studenty budou v původním repozitáři připraveny.*
   * **head repository:** Váš forknutý repozitář
   * **compare branch:** `master`
4. **Název Pull Requestu:** Zadejte ve formátu:  
   `Odevzdani Ukol X - Jmeno Prijmeni` (např. `Odevzdani Ukol 1 - Jan Novak`).
5. Ponechte zaškrtnutou volbu **Allow edits by maintainers** a klikněte na **Create pull request**.

---

### 8. Automatické testy a schválení
* Po vytvoření PR proběhne automatická kontrola pomocí **GitHub Actions**.
* **Zelená fajfka:** Všechny testy proběhly úspěšně. Úkol je v pořádku odevzdán a vyučující váš PR následně sloučí (mergne) do vaší větve.
* **Červený křížek:** Testy na GitHubu selhaly. Klikněte na *Details*, zjistěte příčinu chyby, kód opravte lokálně a odešlete nový commit (`git push origin master`). Otevřený Pull Request se **automaticky aktualizuje** a testy se spustí znovu.

---

## Jak získat nový úkol (Synchronizace vašeho forku)

Až vyučující během semestru zveřejní nový úkol, váš fork v něm ještě nebude mít příslušnou složku. Nové zadání si do svého forku stáhnete velmi snadno:

### Varianta 1: Přes webové rozhraní GitHubu (nejjednodušší)
1. Otevřete hlavní stránku **vašeho forknutého repozitáře** na GitHubu.
2. Pod modrým pruhem / zeleným tlačítkem *Code* najdete tlačítko **Sync fork**.
3. Klikněte na **Sync fork** a poté na **Update branch**. Váš fork na GitHubu je nyní aktuální.
4. Pokud pracujete na svém počítači lokálně, stáhněte si změny do terminálu:
   ```shell
   git pull origin master
   ```

### Varianta 2: Přes Git v terminálu
1. Pokud ještě nemáte nastavený odkaz na původní repozitář, přidejte si jej (stačí provést pouze jednou):
   ```shell
   git remote add upstream https://github.com/TomasRacil/Informatika-2-ukoly-2627-ZS.git
   ```
2. Kdykoliv vyjde nový úkol, stáhněte si novinky:
   ```shell
   git fetch upstream
   git checkout master
   git merge upstream/master
   git push origin master
   ```

---

## Seznam úkolů

| Složka | Název úkolu | Popis | Termín odevzdání | Stav |
| :--- | :--- | :--- | :---: | :---: |
| [**Ukol_0**](./Ukol_0/README.md) | **Hello World** | Ukázkový úkol pro seznámení s odevzdávacím systémem a testy | 2. 10. 2026 | Zadáno |
| [**Ukol_1**](./Ukol_1/README.md) | **Základy: proměnné, podmínky a cykly** | Výpočet BMI, klasifikace hodnot, cyklus for a Collatzova posloupnost (while) | 9. 10. 2026 | Zadáno |
| *Ukol_2* | *Bude doplněno* | *Zadání bude zveřejněno v průběhu semestru* | – | Připravuje se |

---

## Časté dotazy a řešení problémů

<details>
<summary><b>Chyba při commitu: "Author identity unknown" nebo "Please tell me who you are"</b></summary>
Nemáte nakonfigurované své jméno a e-mail v Gitu. Nastavte je v terminálu:
<pre><code>git config --global user.name "Vaše Jméno a Příjmení"
git config --global user.email "vas-github-email@domena.cz"</code></pre>
</details>

<details>
<summary><b>Co dělat, když se automatické testy v PR nespustí?</b></summary>
U prvního odevzdání (či prvního PR nového uživatele) GitHub z bezpečnostních důvodů vyžaduje jednorázové schválení spuštění workflow vlastníkem repozitáře. Vyčkejte na schválení vyučujícím.
</details>

<details>
<summary><b>Příkaz <code>python</code> v terminálu nefunguje.</b></summary>
Na některých systémech (např. macOS a Linux) je interpret dostupný pod názvem <code>python3</code>. Zkontrolujte instalaci zadáním:
<pre><code>python3 --version</code></pre>
</details>
