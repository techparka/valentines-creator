# 💌 Valentine's Card Creator

A web application to create personalized Valentine's Day cards with the ability to share via link or QR code.

---

## ✨ Features

- 🎨 **3 Beautiful Themes** - Dark Romantic, Pink Glass, Starry Night
- 📝 **5 Text Templates** - Various styles and emotions
- ✍️ **Custom Text** - Write your own message (recipient's name added automatically)
- 📱 **QR Code Generator** - Generate and download QR code for sharing
- 🔗 **Link Sharing** - Share direct link to the card
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile
- 🐳 **Docker Ready** - Easy deployment
- 🗄️ **SQLite Database** - Lightweight and portable

---

## 🚀 Quick Start

### Requirements
- Docker & Docker Compose
- Python 3.12+ (if running without Docker)

### Docker (Recommended)

```bash
git clone https://github.com/techparka/valentines-creator.git
cd valentines-creator

# Copy environment template
cp .env.example .env

# Edit configuration (optional)
nano .env
# Set your DOMAIN if deploying to production

# Run
docker-compose up -d

# View logs
docker-compose logs -f
```

Access: `http://localhost:8014`

### Local Setup (Without Docker)

```bash
git clone https://github.com/techparka/valentines-creator.git
cd valentines-creator

# Install dependencies
pip install -r requirements.txt

# Run Flask
export DB_PATH=./valentines.db
export DOMAIN=http://localhost:8014
python app.py
```

---

## 📋 Project Structure

```
valentines-creator/
├── app.py                    # Flask backend
├── requirements.txt          # Python dependencies
├── Dockerfile               # Docker configuration
├── docker-compose.yml       # Docker Compose setup
├── .env.example             # Environment variables template
├── README.md                # This file
│
├── templates/
│   ├── landing.html         # Landing page
│   ├── builder.html         # Card builder form
│   ├── preview.html         # Preview & share page
│   ├── valentine1.html      # Theme 1: Dark Romantic
│   ├── valentine2.html      # Theme 2: Pink Glass
│   └── valentine3.html      # Theme 3: Starry Night
│
└── static/
    └── style.css            # Styling
```

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Database:** SQLite
- **Frontend:** HTML/CSS/JavaScript
- **Server:** Gunicorn
- **Containerization:** Docker

---

## 🔧 Configuration

### Environment Variables (.env)

```env
# Domain for generating card links
DOMAIN=http://localhost:8014

# Path to SQLite database
DB_PATH=/data/valentines.db
```

---

## 📖 How to Use

1. Visit the landing page
2. Click "Create Valentine"
3. Enter recipient's name
4. Choose a theme (3 options)
5. Select a text template (5 options) or write your own
6. Copy link or download QR code
7. Share with your special someone! 💘

---

## 🗄️ Database

SQLite database with `valentines` table:

```sql
CREATE TABLE valentines (
    id TEXT PRIMARY KEY,           -- 8-character unique ID
    name TEXT NOT NULL,            -- Recipient's name
    theme INTEGER NOT NULL,        -- Theme: 1, 2, or 3
    template INTEGER NOT NULL,     -- Template: 1-5
    custom_title TEXT,             -- Custom card title
    custom_body TEXT,              -- Custom card message
    custom_celeb TEXT,             -- Custom celebration message
    created_at TIMESTAMP           -- Creation timestamp
);
```

---

## 🎨 Text Templates

1. **Deep & Touching** - Romantic and heartfelt
2. **Short & Powerful** - Simple and direct
3. **Nostalgic & Poetic** - Memories and feelings
4. **Grateful & Warm** - Thanks and affection
5. **Confident & Sensual** - Passionate and bold

---

## 🚀 Deployment

### Using Docker Compose

```bash
docker-compose up --build -d
docker-compose logs -f
docker-compose down
```

### Manual Deployment Example (Linux/Proxmox)

```bash
# 1. Install dependencies
apt update && apt install -y docker.io docker-compose git

# 2. Clone repository
cd /root
git clone https://github.com/yourusername/valentines-creator.git
cd valentines-creator

# 3. Configure environment
cp .env.example .env
nano .env

# 4. Start application
docker-compose up -d

# 5. Expose to internet (example: using reverse proxy)
# Set up nginx, Apache, or Caddy to forward traffic to localhost:8014
```

### Making It Public

To expose your application to the internet, you can use:
- **Reverse Proxy** (nginx, Apache, Caddy)
- **Tunnel Services** (ngrok, Cloudflare Tunnel, etc.)
- **Cloud Hosting** (AWS, Digital Ocean, Heroku, etc.)

Choose the method that best fits your infrastructure.

---

## 🔐 Security Notes

- Change `DOMAIN` variable for production deployments
- Keep `.env` file private (it's in `.gitignore`)
- Use HTTPS when exposing to the internet
- Regularly backup your SQLite database

---

## 📝 License

MIT - Feel free to use and modify as needed!

---

## 🤝 Contributing

Found a bug? Have a feature idea?
- Open an issue on GitHub
- Submit a pull request

---

## 👨‍💻 Author

Created for Valentine's Day 2026 ❤️

---

**Enjoy creating beautiful Valentine's cards! 💌**
