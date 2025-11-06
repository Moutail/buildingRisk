# 🚀 Guide de Déploiement et Partage

## 📦 Options de Partage

### 1. Partage via GitHub (Recommandé)

#### A. Pousser vers GitHub

```bash
# Si pas encore fait, initialiser Git
cd "c:\Users\Lion Tech\Documents\GitHub\buildingRisk"
git init
git add .
git commit -m "Initial commit: Building Risk Prioritization"

# Créer un repo sur GitHub, puis:
git remote add origin https://github.com/VOTRE-USERNAME/buildingRisk.git
git branch -M main
git push -u origin main
```

#### B. Rendre le Repo Attractif

1. **Ajouter des badges** dans README.md:
```markdown
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-red.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Made with Love](https://img.shields.io/badge/Made%20with-❤-red.svg)](https://github.com/VOTRE-USERNAME/buildingRisk)
```

2. **Ajouter des topics/tags**:
   - machine-learning
   - climate-change
   - urban-planning
   - python
   - streamlit
   - montreal
   - sustainability

3. **Activer GitHub Pages** (optionnel):
   - Settings → Pages
   - Publier la documentation

#### C. Créer une Release

```bash
# Créer un tag
git tag -a v1.0.0 -m "Version 1.0.0 - Initial Release"
git push origin v1.0.0
```

**Notes de release** (sur GitHub):
```markdown
# Version 1.0.0 - Initial Release

## 🎉 Fonctionnalités

- ✅ Système de priorisation ML sans géomatique
- ✅ Dashboard web interactif (Streamlit)
- ✅ Documentation complète en français
- ✅ Pipeline reproductible

## 📊 Résultats

- 2,075 bâtiments analysés
- 46 bâtiments critiques identifiés
- 16,772 tonnes CO₂/an de potentiel

## 📥 Installation

\`\`\`bash
pip install -r requirements.txt
python run_full_pipeline.py
streamlit run 04_web_dashboard.py
\`\`\`

## 📚 Documentation

Voir [README.md](README.md) et [METHODOLOGY.md](METHODOLOGY.md)

## 🤝 Contribution

Issues et Pull Requests bienvenues!
```

---

### 2. Déploiement du Dashboard Web

#### Option A: Streamlit Cloud (GRATUIT et Facile)

1. **Créer un compte**: https://streamlit.io/cloud
2. **Connecter GitHub**: Autoriser l'accès à votre repo
3. **Déployer**:
   - Cliquer "New app"
   - Sélectionner votre repo
   - Main file: `04_web_dashboard.py`
   - Cliquer "Deploy"

**Résultat**: Votre dashboard sera accessible à une URL publique!
```
https://VOTRE-USERNAME-buildingrisk.streamlit.app
```

#### Option B: Heroku (Plus de Contrôle)

Créer un `Procfile`:
```bash
web: streamlit run 04_web_dashboard.py --server.port=$PORT
```

Créer `runtime.txt`:
```
python-3.11.0
```

Déployer:
```bash
heroku create votre-app-name
git push heroku main
```

#### Option C: Docker (Pour Production)

Créer un `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "04_web_dashboard.py", "--server.address", "0.0.0.0"]
```

Build et run:
```bash
docker build -t building-risk .
docker run -p 8501:8501 building-risk
```

---

### 3. Créer un Package Python (Avancé)

#### Structure du Package

```
buildingRisk/
├── setup.py
├── building_risk/
│   ├── __init__.py
│   ├── matching.py
│   ├── model.py
│   └── dashboard.py
└── tests/
```

#### `setup.py`

```python
from setuptools import setup, find_packages

setup(
    name="building-risk-prioritization",
    version="1.0.0",
    author="Projet VILLE_IA",
    author_email="contact@iriu.ca",
    description="ML system for building prioritization without GIS",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/VOTRE-USERNAME/buildingRisk",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.5.0",
        "numpy>=1.23.0",
        "scikit-learn>=1.1.0",
        "plotly>=5.11.0",
        "streamlit>=1.25.0",
    ],
    entry_points={
        "console_scripts": [
            "building-risk=building_risk.cli:main",
        ],
    },
)
```

Publier sur PyPI:
```bash
python setup.py sdist bdist_wheel
pip install twine
twine upload dist/*
```

---

### 4. Documentation sur ReadTheDocs

#### Créer `docs/` avec Sphinx

```bash
pip install sphinx sphinx-rtd-theme
cd docs
sphinx-quickstart
```

#### Configurer sur ReadTheDocs

1. Créer compte: https://readthedocs.org
2. Importer projet depuis GitHub
3. Build automatique à chaque push

**Résultat**: Documentation hébergée à:
```
https://building-risk-prioritization.readthedocs.io
```

---

### 5. Présentation et Démonstration

#### A. Créer une Vidéo Démo

**Script suggéré** (5 minutes):
1. **Introduction** (30s): Problème et solution
2. **Installation** (1m): Commandes rapides
3. **Exécution** (1m30): Pipeline complet
4. **Dashboard** (2m): Exploration interactive
5. **Conclusion** (30s): Résultats et impact

**Outils**:
- OBS Studio (gratuit) pour enregistrer
- DaVinci Resolve (gratuit) pour éditer

#### B. Créer des Slides

Template PowerPoint/Google Slides avec:
1. Titre et contexte
2. Le problème (avec/sans géomatique)
3. Notre innovation
4. Méthodologie (4 piliers)
5. Résultats chiffrés
6. Démonstration
7. Impact et applications
8. Appel à l'action

#### C. Article de Blog

Publier sur:
- Medium
- Dev.to
- LinkedIn
- Blog municipal

---

### 6. Partage Académique

#### A. Préparer un Article

**Structure suggérée**:
```markdown
# Priorisation des Bâtiments Urbains Sans Géomatique:
# Une Approche par Intelligence Artificielle

## Abstract
## Introduction
## Related Work
## Methodology
## Results
## Discussion
## Conclusion
## References
```

#### B. Soumettre à des Conférences

Conférences pertinentes:
- **ACM e-Energy** (énergie + computing)
- **BuildSys** (bâtiments intelligents)
- **ICML Workshop** (ML for climate)
- **Smart City Expo** (innovation urbaine)

#### C. Déposer sur arXiv

```bash
# Créer un PDF du papier
# Soumettre sur: https://arxiv.org
# Catégories: cs.LG (ML), cs.CY (Computers and Society)
```

---

### 7. Communication et Promotion

#### A. Réseaux Sociaux

**Twitter/X**:
```
🏢 Nouveau: Système ML pour prioriser les bâtiments à rénover
🚀 Innovation: AUCUN outil géomatique requis!
📊 Résultats: 16,772 tonnes CO₂/an réductibles
🔗 Code open source: [lien]

#MachineLearning #ClimateAction #UrbanPlanning #Python
```

**LinkedIn**:
```
[Post plus détaillé avec résultats, méthodologie, impact]
+ Inclure des graphiques du dashboard
```

#### B. Communautés Techniques

Partager sur:
- **r/datascience** (Reddit)
- **r/MachineLearning** (Reddit)
- **r/Python** (Reddit)
- **Hacker News**
- **Kaggle** (créer un notebook)

#### C. Contacter des Médias

**Médias techniques**:
- Towards Data Science
- Analytics Vidhya
- KDnuggets

**Médias urbains/climat**:
- CityLab
- Smart Cities Dive
- CleanTechnica

---

### 8. Collaboration et Contributions

#### A. Créer CONTRIBUTING.md

```markdown
# Guide de Contribution

## Comment Contribuer

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## Standards de Code

- PEP 8 pour Python
- Docstrings pour toutes les fonctions
- Tests unitaires pour nouvelles fonctionnalités

## Idées de Contributions

- [ ] Support d'autres villes canadiennes
- [ ] Intégration API Hydro-Québec
- [ ] Module de coût estimé
- [ ] Traduction anglaise
- [ ] Tests unitaires
- [ ] Optimisation performances
```

#### B. Configurer GitHub Actions (CI/CD)

Créer `.github/workflows/tests.yml`:
```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.11
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest
      - name: Run tests
        run: pytest tests/
```

---

### 9. Partenariats et Adoption

#### A. Contacter des Organisations

**Municipalités**:
- Ville de Montréal
- Autres villes VILLE_IA
- Fédération canadienne des municipalités

**Institutions**:
- IRIU (déjà partenaire)
- INSPQ
- Universités (Polytechnique, McGill, UdeM)

**Email type**:
```
Objet: Outil Open Source pour Priorisation Énergétique des Bâtiments

Bonjour [Nom],

Je vous contacte concernant un outil open source que nous avons développé
pour le Projet VILLE_IA...

[Décrire brièvement]

Résultats concrets:
- 2,075 bâtiments analysés
- 16,772 tonnes CO₂/an de potentiel identifié
- Dashboard web interactif
- 100% reproductible sans outils SIG

Seriez-vous intéressé par:
□ Une démonstration
□ Tester l'outil sur vos données
□ Collaborer pour l'améliorer

Code disponible: [GitHub URL]
Documentation: [ReadTheDocs URL]

Cordialement,
[Votre nom]
```

#### B. Webinaires et Présentations

Proposer à:
- Meetups Python locaux
- Conférences municipales
- Événements climat/énergie
- Universités (cours invité)

---

### 10. Checklist de Partage

#### Avant de Partager

- [ ] Code nettoyé et commenté
- [ ] Documentation complète
- [ ] README attractif avec screenshots
- [ ] LICENSE clairement définie
- [ ] .gitignore configuré
- [ ] Données sensibles retirées
- [ ] Tests de base fonctionnels
- [ ] Requirements.txt à jour

#### Partage Minimal

- [ ] Code sur GitHub (public)
- [ ] README avec badges
- [ ] License MIT
- [ ] 1-2 screenshots du dashboard

#### Partage Complet

- [ ] Tout ci-dessus +
- [ ] Dashboard déployé (Streamlit Cloud)
- [ ] Vidéo démo (YouTube)
- [ ] Article de blog
- [ ] Posts réseaux sociaux
- [ ] Soumission conférences

---

### 🎯 Recommandation Immédiate

**Pour commencer MAINTENANT (30 minutes)**:

```bash
# 1. Pousser vers GitHub (si pas déjà fait)
git add .
git commit -m "Complete ML system for building risk prioritization"
git push origin main

# 2. Créer un README attractif (déjà fait ✅)

# 3. Ajouter un screenshot du dashboard
# Lancer le dashboard, faire une capture d'écran, ajouter au README

# 4. Créer une Release sur GitHub
git tag -a v1.0.0 -m "Initial Release"
git push origin v1.0.0

# 5. Partager sur LinkedIn avec:
# - Screenshot
# - Lien GitHub
# - Résultats clés
```

**Résultat**: Projet professionnel partageable immédiatement! 🚀

---

**Besoin d'aide pour une étape spécifique?** Demandez-moi!
