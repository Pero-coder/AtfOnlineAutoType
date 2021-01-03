# AtfOnlineAutoType
Program pro automatické psaní lekcí na atfonline.cz

Program je napsaný v Pythonu a využívá framework Selenium. Pro spuštění je potřeba mít nainsalovaný python 3, selenium a keyboard knihovnu.

Návod na instalaci požadavků:
1) stáhnout a nainstalovat Python: https://www.python.org/downloads/
2) do cmd napsat:
"pip install selenium",
"pip install keyboard"
3) Stáhnout chrome driver (pokud chcete použít driver jiného prohlížeče, je potřeba udělat změny v kódu programu): https://chromedriver.chromium.org/
4) vložit chromedriver.exe do "C:\Program Files (x86)" (pokud umístníte soubor jinam, je potřeba změnit cestu k němu v kódu programu)

Návod na použití:
1) v libovolném textovém editoru (například notepad.exe) otevřete AtfAutoType.py a na označeném místě přepíšete vaše přihlašovací údaje
2) po spuštění se vám načte stránka atfonline.cz a automaticky budete přihlášeni
3) nyní stačí vybrat lekci kterou chcete vyplnit a stisknout "ctrl" 
PS: během psaní nesmíte překlinkout do jiného okna
PS2: pokud lekce obsahuje více řádků, je potřeba na každém novém řádku znovu stisknout "ctrl"
