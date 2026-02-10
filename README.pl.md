# 💌 Kreatora Walentynek

Aplikacja webowa do tworzenia spersonalizowanych walentynek z możliwością udostępniania poprzez link lub kod QR.

---

## ✨ Funkcje

- 🎨 **3 Piękne Motywy** - Ciemny romantyk, Różowy glass, Gwiaździsta noc
- 📝 **5 Szablonów Tekstu** - Różne style i emocje
- ✍️ **Własny Tekst** - Napisz swoją wiadomość (imię automatycznie dodane do tytułu)
- 📱 **Generator Kodu QR** - Wygeneruj i pobierz kod QR do udostępnienia
- 🔗 **Udostępnianie Linkiem** - Prześlij bezpośredni link do walentynki
- 📱 **Responsywny Projekt** - Działa na desktop, tablet i mobile
- 🐳 **Docker Ready** - Łatwy deploy
- 🗄️ **Baza SQLite** - Lekka i przenośna

---

## 🎬 Jak To Działa

### 1️⃣ Strona Główna
Użytkownicy widzą główną stronę z wezwaniem do stworzenia walentynki.

### 2️⃣ Kreator Walentynki
- Wpisz imię wybranki
- Wybierz z 3 pięknych motywów
- Wybierz z 5 szablonów tekstu lub napisz swoją wiadomość
- Imię automatycznie dodawane do tytułu

### 3️⃣ Podgląd i Udostępnianie
- Podgląd walentynki w iframe
- Skopiuj bezpośredni link lub pobierz kod QR
- Udostępnij przez aplikacje komunikacyjne lub media społecznościowe

### 4️⃣ Widok Odbiorcy
- Odbiorca otwiera link lub skanuje kod QR
- Piękna animowana walentynka się wyświetla
- Interaktywne przyciski "Tak/Nie" z konfetti celebracji
- W pełni responsywne na wszystkich urządzeniach

---

## 🚀 Szybki Start

### Wymagania
- Docker & Docker Compose
- Python 3.12+ (jeśli uruchamiasz bez Docker'a)

### Docker (Rekomendowane)

```bash
git clone https://github.com/techparka/valentines-creator.git
cd valentines-creator

# Skopiuj szablon zmiennych środowiskowych
cp .env.example .env

# Edytuj konfigurację (opcjonalnie)
nano .env
# Ustaw domenę jeśli deployujesz na produkcję

# Uruchom
docker-compose up -d

# Wyświetl logi
docker-compose logs -f
```

Dostęp: `http://localhost:8014`

### Lokalna Instalacja (Bez Docker'a)

```bash
git clone https://github.com/techparka/valentines-creator.git
cd valentines-creator

# Zainstaluj zależności
pip install -r requirements.txt

# Uruchom Flask
export DB_PATH=./valentines.db
export DOMAIN=http://localhost:8014
python app.py
```

---

## 📋 Struktura Projektu

```
valentines-creator/
├── app.py                    # Backend Flask
├── requirements.txt          # Zależności Pythona
├── Dockerfile               # Konfiguracja Docker'a
├── docker-compose.yml       # Konfiguracja Docker Compose
├── .env.example             # Szablon zmiennych środowiskowych
├── README.md                # English readme
├── README.pl.md             # Polski readme (ten plik)
│
├── templates/
│   ├── landing.html         # Strona główna
│   ├── builder.html         # Formularz kreatora
│   ├── preview.html         # Strona podglądu i udostępniania
│   ├── valentine1.html      # Motyw 1: Ciemny Romantyk
│   ├── valentine2.html      # Motyw 2: Różowy Glass
│   └── valentine3.html      # Motyw 3: Gwiaździsta Noc
│
└── static/
    └── style.css            # Style
```

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Baza Danych:** SQLite
- **Frontend:** HTML/CSS/JavaScript
- **Serwer:** Gunicorn
- **Konteneryzacja:** Docker

---

## 🔧 Konfiguracja

### Zmienne Środowiskowe (.env)

```env
# Domena do generowania linków do walentynek
DOMAIN=http://localhost:8014

# Ścieżka do bazy danych SQLite
DB_PATH=/data/valentines.db
```

---

## 📖 Jak Używać

1. Odwiedź stronę główną
2. Kliknij "Stwórz Walentynkę"
3. Wpisz imię swojej wybranki
4. Wybierz motyw (3 opcje)
5. Wybierz szablon tekstu (5 opcji) lub napisz swoją wiadomość
6. Skopiuj link lub pobierz kod QR
7. Udostępnij ukochanej osobie! 💘

---

## 🎨 Motywy Walentynek

### Motyw 1: Ciemny Romantyk
- Głębokie ciemne tło ze świecącymi efektami
- Czerwone akcenty i animacja unoszących się serc
- Intymny i namiętny klimat

### Motyw 2: Różowy Glass
- Gradient różowego tła
- Efekt glass morphism
- Animacja rysowania serca
- Nowoczesny i elegancki

### Motyw 3: Gwiaździsta Noc
- Głębokie kosmiczne tło z migoczącymi gwiazdami
- Fioletowe gradienty i efekty mgławicy
- Celebracja spadających gwiazd
- Marzycielski i mistyczny klimat

---

## 🗄️ Baza Danych

Baza SQLite z tabelą `valentines`:

```sql
CREATE TABLE valentines (
    id TEXT PRIMARY KEY,           -- 8-znakowy unikalny identyfikator
    name TEXT NOT NULL,            -- Imię wybranki
    theme INTEGER NOT NULL,        -- Motyw: 1, 2 lub 3
    template INTEGER NOT NULL,     -- Szablon: 1-5
    custom_title TEXT,             -- Własny tytuł walentynki
    custom_body TEXT,              -- Własna wiadomość
    custom_celeb TEXT,             -- Własna wiadomość celebracji
    created_at TIMESTAMP           -- Timestamp utworzenia
);
```

---

## 🎨 Szablony Tekstu

1. **Głęboka i Wzruszająca** - Romantyczna i poważna
2. **Krótka i Mocna** - Prosta i bezpośrednia
3. **Nostalgiczna i Poetycka** - Wspomnienia i uczucia
4. **Wdzięczna i Ciepła** - Dziękowanie i miłość
5. **Pewna Siebie i Zmysłowa** - Stanowcza i pełna pasji

---

## 🚀 Deploy

### Używając Docker Compose

```bash
docker-compose up --build -d
docker-compose logs -f
docker-compose down
```

### Przykład Manual Deploy'u (Linux/Proxmox)

```bash
# 1. Zainstaluj zależności
apt update && apt install -y docker.io docker-compose git

# 2. Sklonuj repozytorium
cd /root
git clone https://github.com/twoja-nazwa/valentines-creator.git
cd valentines-creator

# 3. Skonfiguruj zmienne środowiskowe
cp .env.example .env
nano .env

# 4. Uruchom aplikację
docker-compose up -d

# 5. Wystawienie na internet (przykład: używając reverse proxy)
# Skonfiguruj nginx, Apache lub Caddy aby przekierować ruch do localhost:8014
```

### Wystawienie na Internet

Aby wystawić aplikację na internet, możesz użyć:
- **Reverse Proxy** (nginx, Apache, Caddy)
- **Tunnel Services** (ngrok, Cloudflare Tunnel, itp.)
- **Cloud Hosting** (AWS, Digital Ocean, Heroku, itp.)

Wybierz metodę która najlepiej pasuje do Twojej infrastruktury.

---

## 🔐 Notatki Bezpieczeństwa

- Zmień zmienną `DOMAIN` dla deployów na produkcję
- Trzymaj plik `.env` w prywatności (jest w `.gitignore`)
- Używaj HTTPS gdy wystawiasz aplikację na internet
- Regularnie rób kopie zapasowe bazy danych SQLite

---

## 📝 Licencja

MIT - Używaj i modyfikuj jak chcesz!

---

## 🤝 Współpraca

Znalazłeś bug? Masz pomysł na funkcjonalność?
- Otwórz issue na GitHub
- Wyślij pull request

---

## 👨‍💻 Autor

Stworzono na Walentynki 2026 ❤️

---

**Miłych tworzenia pięknych walentynek! 💌**
