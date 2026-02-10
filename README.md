# 💌 Valentines Creator

Aplikacja webowa do stworzenia spersonalizowanej walentynki z możliwością wysłania via link lub QR code.

**Live:** https://walentynki.techparka.pl/

---

## ✨ Features

- 🎨 **3 motywy graficzne** - Ciemny romantyczny, Różowy glass, Gwiaździsta noc
- 📝 **5 szablonów tekstów** - Różne style i emocje
- ✍️ **Custom text** - Napisz swoją wiadomość (imię dodawane automatycznie)
- 📱 **QR Code** - Wygeneruj i pobierz kod do wysłania
- 🔗 **Link sharing** - Prześlij bezpośredni link do walentynki
- 📱 **Responsive design** - Działa na desktop, tablet i mobile
- 🐳 **Docker ready** - Łatwy deploy
- 🌐 **Cloudflare Tunnel** - Bezpieczny dostęp z internetu

---

## 🚀 Quick Start

### Wymagania
- Docker & Docker Compose
- Python 3.12+ (jeśli chcesz uruchomić bez Docker'a)

### Docker (rekomendowane)

```bash
git clone https://github.com/techparka/valentines-creator.git
cd valentines-creator

# Skopiuj .env
cp .env.example .env

# Edytuj domenę (opcjonalnie)
nano .env
# DOMAIN=https://twoja-domena.com

# Uruchom
docker-compose up -d

# Sprawdź logi
docker-compose logs -f
```

Dostęp: `http://localhost:8014`

### Lokalnie (bez Docker'a)

```bash
git clone https://github.com/techparka/valentines-creator.git
cd valentines-creator

# Zainstaluj dependencje
pip install -r requirements.txt

# Uruchom Flask
export DB_PATH=./valentines.db
export DOMAIN=http://localhost:8014
python app.py
```

---

## 📋 Struktura

```
valentines-creator/
├── app.py                    # Flask backend
├── requirements.txt          # Dependencje
├── Dockerfile               # Docker config
├── docker-compose.yml       # Compose config
├── .env.example             # Template zmiennych
│
├── templates/
│   ├── landing.html         # Strona główna
│   ├── builder.html         # Kreator walentynki
│   ├── preview.html         # Podgląd + share
│   ├── valentine1.html      # Motyw 1: Ciemny
│   ├── valentine2.html      # Motyw 2: Różowy glass
│   └── valentine3.html      # Motyw 3: Gwiaździsta noc
│
└── static/
    └── style.css            # Styles
```

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Database:** SQLite
- **Frontend:** HTML/CSS/JavaScript
- **Server:** Gunicorn
- **Deployment:** Docker + Cloudflare Tunnel

---

## 🔧 Konfiguracja

### Zmienne środowiskowe (.env)

```env
# Domena do generowania linków
DOMAIN=https://walentynki.example.com

# Ścieżka do bazy danych
DB_PATH=/data/valentines.db
```

### Cloudflare Tunnel

1. Zainstaluj cloudflared
2. Login: `cloudflared tunnel login`
3. Create tunnel: `cloudflared tunnel create valentines`
4. Config w `~/.cloudflared/config.yml`:

```yaml
tunnel: valentines
credentials-file: /root/.cloudflared/TUNNEL_ID.json

ingress:
  - hostname: walentynki.example.com
    service: http://localhost:8014
  - service: http_status:404
```

5. Run: `cloudflared tunnel run valentines`
6. Dodaj CNAME w Cloudflare DNS

---

## 📖 Jak używać

1. Wejdź na stronę główną
2. Kliknij "Stwórz Walentynkę"
3. Wpisz imię wybranki
4. Wybierz motyw (3 opcje)
5. Wybierz szablon tekstu (5 opcji) lub napisz swój
6. Skopiuj link lub pobierz QR code
7. Wyślij dziewczynie! 💘

---

## 📱 Baza danych

SQLite z tabelą `valentines`:

```sql
CREATE TABLE valentines (
    id TEXT PRIMARY KEY,           -- 8-znakowy ID
    name TEXT NOT NULL,            -- Imię wybranki
    theme INTEGER NOT NULL,        -- 1, 2 lub 3
    template INTEGER NOT NULL,     -- 1-5
    custom_title TEXT,             -- Custom nagłówek
    custom_body TEXT,              -- Custom treść
    custom_celeb TEXT,             -- Custom celebracja
    created_at TIMESTAMP           -- Data utworzenia
);
```

---

## 🎨 Szablony tekstów

1. **Głęboka, wzruszająca** - Romantyczna i poważna
2. **Krótka i mocna** - Prosta i bezpośrednia
3. **Nostalgiczna, poetycka** - Wspomnienia i uczucia
4. **Wdzięczna, ciepła** - Dziękowanie i miłość
5. **Pewna siebie, zmysłowa** - Stanowcza i pełna pasji

---

## 🚢 Deploy

### Docker Compose

```bash
docker-compose up --build -d
docker-compose logs -f
docker-compose down
```

### Proxmox LXC

1. Stwórz LXC kontener (Debian 12)
2. Zainstaluj Docker: `curl -fsSL https://get.docker.com | sh`
3. Clone repo i `docker-compose up -d`

---

## 📝 Licencja

MIT - Użyj i modyfikuj jak chcesz!

---

## 👨‍💻 Author

**techparka** - Valentine's Day 2026 🎁

---

## 🤝 Wsparcie

Znalazłeś bug? Masz pomysł na feature?
- Open issue na GitHub
- Lub skontaktuj się bezpośrednio

---

**Made with ❤️ for Valentine's Day**
