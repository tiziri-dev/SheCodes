# SheCodes — Gestion des Emplois du Temps

Application web de planification des emplois du temps universitaires avec détection automatique des conflits (salle, enseignant, groupe, capacité, indisponibilité).

## Structure du projet
- `app/` : Code de l'application (modèles, logique métier, routes API, pages HTML)
- `tests/` : Tests automatisés (`pytest`)
- `docs/` : Documents de référence de l'équipe

## Installation et lancement
1. Créer et activer l'environnement virtuel :
   python3 -m venv .venv
   source .venv/bin/activate
2. Installer les dépendances :
   pip install -r requirements.txt
3. Configurer les variables d'environnement :
   cp .env.example .env
4. Lancer le serveur :
   uvicorn app.main:app --reload

## Règles Git
- Ne jamais coder directement sur `main`.
- Créer une branche par tâche (`feat/...`) avant de coder.
