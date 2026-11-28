# SheCodes — Gestion des emplois du temps du département

Mini-projet DevOps — Université de Béjaïa — Thème 1

## 👥 Équipe
- Roubache Alyssa — Backend Core & Base de données
- Kerkadi Tiziri — DevOps / CI-CD
- Hammad Malak Nour El Houda — Frontend & Tests
- Ziani Yasmine — Sécurité, Docs & Observabilité

## 🎯 Objectif
Application web de gestion d'emplois du temps (cours, TD, TP) avec
détection automatique de conflits (enseignant occupé, salle occupée,
groupe déjà en cours, salle trop petite).

## 🏗️ Architecture
[Frontend Jinja2/JS] → [FastAPI] → [PostgreSQL]
                          ↓
              [GitHub Actions] → [Docker Hub] → [Docker Compose]

## 🚀 Installation locale
```bash
git clone https://github.com/tiziri-dev/SheCodes.git
cd SheCodes
cp .env.example .env
docker compose up -d