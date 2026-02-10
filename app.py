import os
import sqlite3
import string
import random
from flask import Flask, render_template, request, redirect, url_for, g

app = Flask(__name__)

# Config from environment
DB_PATH = os.environ.get('DB_PATH', '/data/valentines.db')
BASE_DOMAIN = os.environ.get('DOMAIN', 'http://localhost:8014').rstrip('/')

# ── Template data ──────────────────────────────────────────────

TEMPLATES = {
    1: {
        'label': 'Wzruszająca',
        'preview': 'Każdego ranka budzę się z myślą, że jestem najszczęśliwszym człowiekiem na świecie...',
        'title': 'Moja jedyna, {name}...',
        'body': [
            'Nie potrzebuję jednego dnia w roku, żeby Ci powiedzieć, co do Ciebie czuję. Ale dzisiaj chcę to zrobić wyjątkowo.',
            'Każdego ranka budzę się z myślą, że jestem najszczęśliwszym człowiekiem na świecie \u2014 bo mam Ciebie. Twój śmiech leczy moje gorsze dni, a Twoje serce jest moim domem.',
            'Po tych wszystkich wspólnych chwilach kocham Cię bardziej niż pierwszego dnia. I mam do Ciebie jedno pytanie...',
        ],
        'celeb_title': 'Wiedziałem!',
        'celeb_text': [
            'Bo tak naprawdę nigdy nie było innej opcji.',
            'Dziękuję, że jesteś ze mną \u2014 wczoraj, dziś i na zawsze.',
        ],
    },
    2: {
        'label': 'Krótka i mocna',
        'preview': 'Mógłbym napisać tysiąc słów... ale Ty znasz mnie lepiej niż ktokolwiek...',
        'title': 'Hej, {name}...',
        'body': [
            'Wiesz co? Mógłbym napisać tysiąc słów o tym, jak bardzo Cię kocham.',
            'Ale Ty znasz mnie lepiej niż ktokolwiek \u2014 wiesz, że wolę to pokazywać niż mówić.',
            'Dziś jednak zrobię wyjątek. Jesteś miłością mojego życia. Kropka.',
            'A teraz... mam jedno małe pytanie...',
        ],
        'celeb_title': 'A widzisz!',
        'celeb_text': [
            'Nie da się powiedzieć \u201eNie\u201d miłości życia.',
            'Dziękuję, że jesteś moja \u2014 dzisiaj, jutro i na zawsze.',
        ],
    },
    3: {
        'label': 'Nostalgiczna',
        'preview': 'Pamiętasz naszą pierwszą Walentynkę? Od tamtego dnia...',
        'title': 'Kochanie, {name}...',
        'body': [
            'Pamiętasz naszą pierwszą Walentynkę? Od tamtego dnia minęło tyle czasu, a ja nadal czuję to samo ciepło, kiedy splatasz swoje palce z moimi.',
            'Zmieniło się wszystko wokół nas \u2014 ale jedno zostało takie samo: to, jak mocno bije mi serce, gdy jesteś blisko.',
            'I jest coś, o co chcę Cię dziś zapytać, choć odpowiedź znam od lat...',
        ],
        'celeb_title': 'Jak zawsze...',
        'celeb_text': [
            '...tak samo jak za pierwszym razem.',
            'Każda kolejna Walentynka z Tobą jest najpiękniejszą z nich wszystkich.',
        ],
    },
    4: {
        'label': 'Wdzięczna i ciepła',
        'preview': 'Gdybym mógł cofnąć czas, wybrałbym Cię jeszcze raz...',
        'title': 'Moje serce, {name}...',
        'body': [
            'Gdybym mógł cofnąć czas \u2014 wybrałbym Cię jeszcze raz. I jeszcze raz. I za każdym razem.',
            'Dziękuję za każdy wspólny poranek, za każdy wieczór na kanapie, za każdą chwilę, w której po prostu byłaś obok.',
            'Ty sprawiasz, że zwykłe dni stają się niezwykłe. I mam do Ciebie pewne pytanie...',
        ],
        'celeb_title': 'Dziękuję!',
        'celeb_text': [
            'Za to, że wybrałaś mnie. Za to, że wybierasz mnie każdego dnia.',
            'Obiecuję Ci kolejne wspólne lata pełne miłości, śmiechu i przygód.',
        ],
    },
    5: {
        'label': 'Zmysłowa',
        'preview': 'Nie wiem, czym sobie zasłużyłem na kogoś takiego jak Ty...',
        'title': '{name}...',
        'body': [
            'Nie wiem, czym sobie zasłużyłem na kogoś takiego jak Ty.',
            'Potrafisz jednym spojrzeniem sprawić, że zapominam o całym świecie. Jednym uśmiechem \u2014 że wszystko będzie dobrze. I jednym dotykiem \u2014 że jestem w domu.',
            'Jesteś wszystkim, o czym nie wiedziałem, że marzę. A teraz mam jedno pytanie...',
        ],
        'celeb_title': 'Moja Walentynko!',
        'celeb_text': [
            'Wiedziałem, że powiesz \u201eTak\u201d \u2014 bo jesteśmy pisani sobie.',
            'Obiecuję, że każdy dzień z Tobą będę traktował jak prezent.',
        ],
    },
}

THEMES = {
    1: {'name': 'Ciemny romantyczny', 'desc': 'Ciepłe czerwienie, unoszące się serca', 'colors': ['#1a0a0a', '#e74c3c', '#c0392b']},
    2: {'name': 'Różowy glass', 'desc': 'Jasny róż, efekt szkła, rysowane serce', 'colors': ['#fce4ec', '#e91e63', '#f06292']},
    3: {'name': 'Gwiaździsta noc', 'desc': 'Nocne niebo, księżyc, spadające gwiazdy', 'colors': ['#0a0a2e', '#9b59b6', '#d4a0ff']},
}


# ── Database ───────────────────────────────────────────────────

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exc):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    db = sqlite3.connect(DB_PATH)
    db.execute('''
        CREATE TABLE IF NOT EXISTS valentines (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            theme INTEGER NOT NULL,
            template INTEGER NOT NULL,
            custom_title TEXT,
            custom_body TEXT,
            custom_celeb TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    db.commit()
    db.close()


def generate_id():
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choices(chars, k=8))


# ── Routes ─────────────────────────────────────────────────────

@app.route('/')
def landing():
    return render_template('landing.html')


@app.route('/create')
def create_form():
    return render_template('builder.html', templates=TEMPLATES, themes=THEMES)


@app.route('/create', methods=['POST'])
def create_submit():
    name = request.form.get('name', '').strip()
    theme = request.form.get('theme', type=int)
    template = request.form.get('template', type=int)
    custom_title = request.form.get('custom_title', '').strip()
    custom_body = request.form.get('custom_body', '').strip() or None
    custom_celeb = request.form.get('custom_celeb', '').strip() or None

    if not name or theme not in THEMES or template not in TEMPLATES:
        return redirect(url_for('create_form'))

    # Jeśli custom_title, dodaj imię
    if custom_title:
        custom_title = f"{custom_title} {name}"
    else:
        custom_title = None

    vid = generate_id()
    db = get_db()
    db.execute(
        'INSERT INTO valentines (id, name, theme, template, custom_title, custom_body, custom_celeb) VALUES (?, ?, ?, ?, ?, ?, ?)',
        (vid, name, theme, template, custom_title, custom_body, custom_celeb),
    )
    db.commit()
    return redirect(url_for('preview', vid=vid))


@app.route('/preview/<vid>')
def preview(vid):
    db = get_db()
    val = db.execute('SELECT * FROM valentines WHERE id = ?', (vid,)).fetchone()
    if not val:
        return redirect(url_for('landing'))
    return render_template('preview.html', vid=vid, base_domain=BASE_DOMAIN)


@app.route('/v/<vid>')
def valentine(vid):
    db = get_db()
    val = db.execute('SELECT * FROM valentines WHERE id = ?', (vid,)).fetchone()
    if not val:
        return redirect(url_for('landing'))

    # Use custom text if provided, otherwise use template
    if val['custom_title']:
        title = val['custom_title']
        body = [p.strip() for p in val['custom_body'].split('\n') if p.strip()] if val['custom_body'] else []
        celeb_title = "Tak!"
        celeb_text = [val['custom_celeb']] if val['custom_celeb'] else ["Dziękuję!"]
    else:
        tmpl = TEMPLATES[val['template']]
        name = val['name']
        title = tmpl['title'].replace('{name}', name)
        body = tmpl['body']
        celeb_title = tmpl['celeb_title']
        celeb_text = tmpl['celeb_text']

    template_file = f"valentine{val['theme']}.html"
    return render_template(
        template_file,
        title=title,
        body=body,
        celeb_title=celeb_title,
        celeb_text=celeb_text,
        name=val['name'],
    )


# ── Init & run ─────────────────────────────────────────────────

init_db()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
