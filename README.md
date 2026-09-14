# Toma Beauty Styling

One-page website for Toma's beauty services in Hadera, built with Pelican and Tailwind CSS.

## Stack

- Pelican 4.12
- Tailwind CSS 4
- Render Static Site

## Local development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
npm install
npm run build:css
pelican content -s pelicanconf.py
python -m http.server 8000 -d output
```

For Windows PowerShell, activate the virtual environment with:

```powershell
.\.venv\Scripts\Activate.ps1
```

## Production build

```bash
pip install -r requirements.txt && npm install --no-audit --no-fund && npm run build:css && pelican content -s publishconf.py
```

Render publish directory: `output`
