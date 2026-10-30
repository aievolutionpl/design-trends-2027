# Wyniki QA — lokalnie

Test: Python Playwright + /usr/bin/google-chrome, serwer `python3 -m http.server 8765 --bind 127.0.0.1`. Surowe pomiary: `browser-results.json`; obrazy: `phone.png`, `tablet.png`, `desktop.png` i odpowiednie `*-hero.png`.

- 320×700, 390×844, 768×1024, 1440×900: szerokość dokumentu równa szerokości okna, 10 sekcji, 10 linków, 10 odrębnych klas ilustracji; hero wczytane.
- Kliknięcie pierwszej pozycji nawigacji prowadzi do #kierunki. Błędy konsoli i pageerror: 0 w testowanych widokach.
- Kontrast wyliczony z kolorów DOM dla ośmiu przykładowych selektorów: minimum 7,5:1. Nie jest to audyt każdej etykiety, grafik ani pełna certyfikacja WCAG.
- Zrzuty hero phone, tablet i desktop obejrzano; bez widocznego ucięcia tekstu. Obejrzano również całą stronę. Automatyczna analiza pełnego zrzutu błędnie sugerowała brak linku i powtórzone grafiki: DOM potwierdza 10 linków i 10 odrębnych rodzajów ilustracji.
- Impeccable: 39 ostrzeżeń (`impeccable.json`), w tym kontrast ilustracji. Hallmark render uruchomiony, 112 fail, 33 reflex, 7 warn (`sloplint.json`, pierwszy wiersz to log przed JSON). Wynik obejmuje m.in. reguły estetyczne, brak stampu Hallmark i tekst ilustracji. To nie jest zaliczona bramka stylu; potrzeba ręcznej analizy i poprawek.
- Po teście uzupełniono link do filmu wskazanego przez użytkownika: https://youtu.be/6m7Y5SKXhks. Nie sprawdzono ręcznie czytnika ekranu ani wszystkich linków zewnętrznych.
