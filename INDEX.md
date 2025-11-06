# 📚 Index de la Documentation - Building Risk Prioritization

## 🚀 Pour Commencer

Vous êtes nouveau? Commencez ici:

1. **[README.md](README.md)** - Vue d'ensemble du projet (5 min)
2. **[GUIDE_RAPIDE.md](GUIDE_RAPIDE.md)** - Installation et premiers pas (3 min)
3. **[RESUME_EXECUTIF.md](RESUME_EXECUTIF.md)** - Résultats et impact (10 min)

## 📖 Documentation Complète

### Documents Principaux

| Document | Contenu | Audience | Durée Lecture |
|----------|---------|----------|---------------|
| **[README.md](README.md)** | Vue d'ensemble, installation, structure | Tous | 5-10 min |
| **[METHODOLOGY.md](METHODOLOGY.md)** | Méthodologie détaillée, formules, validation | Technique | 20-30 min |
| **[GUIDE_RAPIDE.md](GUIDE_RAPIDE.md)** | Installation rapide, FAQ, commandes | Utilisateurs | 5 min |
| **[RESUME_EXECUTIF.md](RESUME_EXECUTIF.md)** | Résultats, impacts, scénarios | Décideurs | 10 min |
| **[INDEX.md](INDEX.md)** | Ce fichier - Navigation | Tous | 2 min |

### Fichiers Techniques

| Fichier | Description | Type |
|---------|-------------|------|
| **[requirements.txt](requirements.txt)** | Dépendances Python | Config |
| **[LICENSE](LICENSE)** | Licence MIT | Légal |
| **[.gitignore](.gitignore)** | Fichiers ignorés par Git | Config |

## 💻 Code Source

### Scripts Python

#### Pipeline Principal

| Script | Description | Input | Output |
|--------|-------------|-------|--------|
| **[run_full_pipeline.py](run_full_pipeline.py)** | Exécute tout le pipeline | Données brutes | Tous les outputs |

#### Étapes Individuelles

| Script | Étape | Description |
|--------|-------|-------------|
| **[01_data_exploration.py](01_data_exploration.py)** | 1️⃣ | Exploration et analyse des données |
| **[02_intelligent_matching.py](02_intelligent_matching.py)** | 2️⃣ | Matching sans géomatique |
| **[03_ml_prioritization_model.py](03_ml_prioritization_model.py)** | 3️⃣ | Modèle ML de priorisation |
| **[04_web_dashboard.py](04_web_dashboard.py)** | 🌐 | Dashboard web Streamlit |

#### Notebook Interactif

| Fichier | Description | Utilisation |
|---------|-------------|-------------|
| **[buildings_risk.ipynb](buildings_risk.ipynb)** | Jupyter Notebook | Exploration interactive |

## 📊 Données

### Données Sources (dossier `data/`)

| Fichier | Description | Taille | Source |
|---------|-------------|--------|--------|
| `batiments-municipaux.csv` | 2,075 bâtiments municipaux | 387 KB | Ville de Montréal |
| `consommation-energetique-*.csv` | Consommation énergétique | 15 KB | Ville de Montréal |
| `ilots-de-chaleur-*.geojson` | Îlots de chaleur | 18 MB | INSPQ |
| `vdq-zonesinondablesreglementees.csv` | Zones inondables | 14 MB | Québec |
| `IndiceCanadienDeVulnérabilitéSociale.csv` | Vulnérabilité sociale | 4.3 MB | StatCan |

### Fichiers de Sortie (générés)

| Fichier | Description | Lignes | Colonnes |
|---------|-------------|--------|----------|
| `output_buildings_enriched.csv` | Bâtiments enrichis | 2,075 | ~20 |
| `output_buildings_prioritized.csv` | Résultats complets | 2,075 | ~30 |
| `output_top_100_priorities.csv` | Top 100 priorités | 100 | ~30 |

## 🎯 Par Cas d'Usage

### Je suis... Décideur Municipal

**Parcours recommandé:**
1. Lire: [RESUME_EXECUTIF.md](RESUME_EXECUTIF.md)
2. Voir: Dashboard web (après installation)
3. Consulter: [METHODOLOGY.md](METHODOLOGY.md) (section "Applications Pratiques")

**Temps total**: 20 minutes

---

### Je suis... Analyste / Data Scientist

**Parcours recommandé:**
1. Lire: [README.md](README.md)
2. Explorer: [METHODOLOGY.md](METHODOLOGY.md) (sections techniques)
3. Exécuter: [run_full_pipeline.py](run_full_pipeline.py)
4. Analyser: [buildings_risk.ipynb](buildings_risk.ipynb)

**Temps total**: 1-2 heures

---

### Je suis... Développeur

**Parcours recommandé:**
1. Lire: [README.md](README.md) et [GUIDE_RAPIDE.md](GUIDE_RAPIDE.md)
2. Installer: `pip install -r requirements.txt`
3. Étudier le code: Scripts Python annotés
4. Contribuer: Pull requests bienvenues!

**Temps total**: 2-3 heures

---

### Je suis... Chercheur

**Parcours recommandé:**
1. Lire: [METHODOLOGY.md](METHODOLOGY.md) (complet)
2. Reproduire: Exécuter le pipeline
3. Valider: Comparer avec vos propres analyses
4. Citer: Voir section "Citation" ci-dessous

**Temps total**: 4-6 heures

---

### Je veux... Reproduire pour Ma Ville

**Parcours recommandé:**
1. Lire: [GUIDE_RAPIDE.md](GUIDE_RAPIDE.md)
2. Adapter: [METHODOLOGY.md](METHODOLOGY.md) section "Extensibilité"
3. Modifier: Les proxys de risque dans `02_intelligent_matching.py`
4. Exécuter: Votre pipeline personnalisé

**Temps total**: 1-2 jours (selon vos données)

## 🔍 Index Thématique

### Méthodologie

- **Approche sans géomatique**: [METHODOLOGY.md](METHODOLOGY.md) sections 2-3
- **Intelligence des codes postaux**: [METHODOLOGY.md](METHODOLOGY.md) section 3.1
- **Modèle ML**: [METHODOLOGY.md](METHODOLOGY.md) section 3.4
- **Validation**: [METHODOLOGY.md](METHODOLOGY.md) section 5

### Résultats

- **Statistiques globales**: [RESUME_EXECUTIF.md](RESUME_EXECUTIF.md) section "Résultats"
- **Top bâtiments**: [RESUME_EXECUTIF.md](RESUME_EXECUTIF.md) section "Top 5"
- **Par arrondissement**: [RESUME_EXECUTIF.md](RESUME_EXECUTIF.md) section "Insights"
- **Impact GES**: [RESUME_EXECUTIF.md](RESUME_EXECUTIF.md) section "Scénarios"

### Technique

- **Architecture**: [METHODOLOGY.md](METHODOLOGY.md) section 4
- **Formules**: [METHODOLOGY.md](METHODOLOGY.md) section 4.2
- **Technologies**: [METHODOLOGY.md](METHODOLOGY.md) section 4.3
- **Code**: Tous les fichiers `.py`

### Utilisation

- **Installation**: [GUIDE_RAPIDE.md](GUIDE_RAPIDE.md) section "Installation"
- **Dashboard**: [GUIDE_RAPIDE.md](GUIDE_RAPIDE.md) section "Utilisation"
- **FAQ**: [GUIDE_RAPIDE.md](GUIDE_RAPIDE.md) section "Questions"
- **Commandes**: [GUIDE_RAPIDE.md](GUIDE_RAPIDE.md) section "Commandes"

## 📚 Références et Citations

### Citer ce Projet

**Format APA:**
```
Projet VILLE_IA (2024). Priorisation des Bâtiments à Risque sans Géomatique:
Une Approche par Intelligence Artificielle. Institut de la résilience et de
l'innovation urbaine (IRIU), Montréal, Québec.
```

**Format BibTeX:**
```bibtex
@misc{villeia2024building,
  title={Priorisation des Bâtiments à Risque sans Géomatique},
  author={Projet VILLE\_IA},
  year={2024},
  institution={Institut de la résilience et de l'innovation urbaine (IRIU)},
  address={Montréal, Québec},
  note={Disponible sur GitHub}
}
```

### Sources de Données

- **Ville de Montréal**: [donnees.montreal.ca](https://donnees.montreal.ca/)
- **INSPQ**: Îlots de chaleur urbains
- **Gouvernement du Québec**: Zones inondables
- **StatCan**: Indice de vulnérabilité sociale

## 🆘 Aide et Support

### Problèmes Courants

| Problème | Solution | Document |
|----------|----------|----------|
| Installation échoue | Vérifier Python 3.8+ | [GUIDE_RAPIDE.md](GUIDE_RAPIDE.md) |
| Données manquantes | Télécharger depuis sources | [README.md](README.md) |
| Dashboard ne démarre pas | `pip install streamlit` | [GUIDE_RAPIDE.md](GUIDE_RAPIDE.md) |
| Résultats incohérents | Vérifier format données | [METHODOLOGY.md](METHODOLOGY.md) |

### Ressources

- **FAQ**: [GUIDE_RAPIDE.md](GUIDE_RAPIDE.md) section "Questions Fréquentes"
- **GitHub Issues**: Pour rapporter bugs
- **Email**: contact@iriu.ca (projet VILLE_IA)
- **Documentation**: Tous les fichiers sont commentés

## 🗺️ Roadmap

### Version 1.0 (Actuelle)
- ✅ Pipeline complet sans géomatique
- ✅ Dashboard web interactif
- ✅ Documentation complète
- ✅ Code open source

### Version 1.1 (Planifiée)
- 🔄 Intégration données réelles Hydro-Québec
- 🔄 Module de coût estimé des rénovations
- 🔄 API REST pour intégrations
- 🔄 Support multi-villes

### Version 2.0 (Future)
- 📅 Modèles deep learning
- 📅 Prédictions temporelles
- 📅 Optimisation de portefeuille
- 📅 Module de suivi post-rénovation

## 📞 Contacts

- **Projet**: VILLE_IA
- **Institution**: IRIU (Institut de la résilience et de l'innovation urbaine)
- **Web**: [iriu.ca](https://iriu.ca)
- **GitHub**: [Ce repository]
- **Email**: contact@iriu.ca

---

## 🚀 Démarrage Rapide (Récapitulatif)

**En 3 commandes:**

```bash
# 1. Installer
pip install -r requirements.txt

# 2. Exécuter
python run_full_pipeline.py

# 3. Visualiser
streamlit run 04_web_dashboard.py
```

**En 10 minutes**, vous avez vos résultats!

---

*Index généré pour le projet Building Risk Prioritization*
*Dernière mise à jour: Novembre 2024*
*Version: 1.0*
