# 🏢 Building Risk Prioritization - Montréal

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![VILLE_IA](https://img.shields.io/badge/Project-VILLE__IA-orange.svg)](https://iriu.ca)

## 📋 Description

Solution de machine learning pour identifier et prioriser les bâtiments municipaux de Montréal nécessitant des rénovations énergétiques et une adaptation climatique.

**Innovation clé:** Approche **SANS géomatique** - remplace l'analyse spatiale traditionnelle par de l'intelligence artificielle et l'analyse textuelle.

### Problème Résolu

Les villes doivent prioriser les rénovations pour:
- 🌱 Réduire les émissions de GES
- 🌡️ Renforcer la résilience climatique (chaleur, inondations)
- 👥 Protéger les populations vulnérables

Traditionnellement, cela requiert des outils SIG complexes. Notre solution utilise **seulement Python et du ML** pour obtenir des résultats comparables.

## 🚀 Installation Rapide

```bash
# Cloner le repository
git clone https://github.com/[your-repo]/buildingRisk.git
cd buildingRisk

# Créer un environnement virtuel (recommandé)
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt
```

## 📊 Utilisation

### Option 1: Pipeline Complet (Recommandé)

```bash
# Exécuter tout le pipeline d'analyse
python run_full_pipeline.py
```

Cela va:
1. Explorer les données
2. Enrichir avec intelligence des codes postaux
3. Calculer les scores de priorisation
4. Générer les fichiers de sortie

### Option 2: Étape par Étape

```bash
# 1. Exploration des données
python 01_data_exploration.py

# 2. Matching intelligent
python 02_intelligent_matching.py

# 3. Modèle ML de priorisation
python 03_ml_prioritization_model.py
```

### Option 3: Dashboard Web Interactif

```bash
# Lancer l'interface web
streamlit run 04_web_dashboard.py
```

Ouvrez votre navigateur à: `http://localhost:8501`

## 📁 Structure du Projet

```
buildingRisk/
│
├── data/                                    # Données sources
│   ├── batiments-municipaux.csv             # 2,075 bâtiments
│   ├── consommation-energetique-*.csv       # Données énergie
│   ├── ilots-de-chaleur-*.geojson           # Îlots de chaleur
│   ├── vdq-zonesinondablesreglementees.csv  # Zones inondables
│   └── IndiceCanadienDeVulnérabilitéSociale.csv
│
├── 01_data_exploration.py                   # Exploration des données
├── 02_intelligent_matching.py               # Matching sans géomatique
├── 03_ml_prioritization_model.py            # Modèle ML
├── 04_web_dashboard.py                      # Dashboard Streamlit
├── run_full_pipeline.py                     # Pipeline automatisé
│
├── output_buildings_enriched.csv            # Résultats intermédiaires
├── output_buildings_prioritized.csv         # Résultats complets
├── output_top_100_priorities.csv            # Top 100 priorités
│
├── METHODOLOGY.md                           # Documentation détaillée
├── README.md                                # Ce fichier
└── requirements.txt                         # Dépendances Python
```

## 🧠 Méthodologie

### L'Innovation: Remplacer la Géomatique

**Approche Traditionnelle (SIG):**
```
Adresses → Géocodage → Coordonnées → Jointures Spatiales → Analyse
```

**Notre Approche (ML + Analyse Textuelle):**
```
Adresses → Codes Postaux → Intelligence Géographique → ML → Priorisation
```

### Comment Ça Marche

1. **Extraction de Codes Postaux**
   - Les codes postaux canadiens encodent la géographie
   - H1 = Est Montréal, H3 = Centre-ville, etc.
   - Mapping manuel des risques par zone

2. **Proxys de Vulnérabilité**
   - Vulnérabilité sociale par arrondissement
   - Risques climatiques basés sur la géographie connue
   - Validation avec données existantes

3. **Modélisation ML**
   ```python
   Score_Priorité =
       40% × Risque_Énergétique +
       30% × Risque_Climatique +
       20% × Vulnérabilité_Sociale +
       10% × Impact_Potentiel
   ```

4. **Classification Automatique**
   - Critical (80-100): Action urgente
   - High (60-80): Court terme
   - Medium (40-60): Moyen terme
   - Low (0-40): Suivi

Voir [METHODOLOGY.md](METHODOLOGY.md) pour détails complets.

## 📈 Résultats

### Statistiques Clés

| Métrique | Valeur |
|----------|--------|
| Bâtiments Analysés | 2,075 |
| Priorité Critique | 46 (2.2%) |
| Priorité Haute | 399 (19.2%) |
| Potentiel GES Total | 16,772 tonnes CO₂/an |
| Top 100 Potentiel | 3,256 tonnes CO₂/an |

### Top 5 Bâtiments Prioritaires

1. **Piscines Montréal-Nord** (Score: 100/100) - Zone vulnérable
2. **Aréna Garon** (Score: 94/100) - 47 t CO₂/an potentiel
3. **Aréna Rolland** (Score: 93/100) - 34 t CO₂/an potentiel
4. **Auditorium Verdun** (Score: 87/100) - 202 t CO₂/an potentiel
5. **Édifice Bellechasse** (Score: 87/100) - 187 t CO₂/an potentiel

## 🎯 Cas d'Usage

### Pour Décideurs Municipaux

**Scénario 1: Budget Limité (500K$)**
- Cibler 5-10 bâtiments en zones vulnérables
- Maximiser l'impact social
- ROI: Équité + résilience communautaire

**Scénario 2: Programme Moyen (2M$)**
- Top 20 bâtiments par score
- Mix 60% équité + 40% impact GES
- ROI: ~800 tonnes CO₂/an

**Scénario 3: Transformation (10M$)**
- Top 100 bâtiments
- Programme sur 3 ans
- ROI: ~3,200 tonnes CO₂/an

### Pour Analystes

Le dashboard permet de:
- Filtrer par arrondissement, priorité, vulnérabilité
- Visualiser les corrélations entre facteurs
- Exporter des listes personnalisées
- Analyser les tendances par âge, type, localisation

## 🛠️ Technologies

- **Python 3.8+**
- **Pandas** - Manipulation de données
- **Scikit-learn** - Machine Learning
- **Streamlit** - Dashboard web
- **Plotly** - Visualisations interactives

**Aucun outil SIG requis!** 🎉

## 📚 Documentation

- [METHODOLOGY.md](METHODOLOGY.md) - Méthodologie complète (10 pages)
- Code commenté en détail dans chaque fichier
- Dashboard avec tooltips explicatifs

## 🤝 Contribution

Ce projet est développé pour le **Projet VILLE_IA** - Institut de la résilience et de l'innovation urbaine (IRIU).

Contributions bienvenues:
1. Fork le projet
2. Créez une branche feature (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour détails.

## 🔗 Liens

- [Projet VILLE_IA](https://iriu.ca)
- [IRIU](https://iriu.ca)
- [Données Ouvertes Montréal](https://donnees.montreal.ca/)

## 👥 Auteurs

- **Projet VILLE_IA** - Institut de la résilience et de l'innovation urbaine (IRIU)

## 🙏 Remerciements

- Ville de Montréal pour les données ouvertes
- Municipalités partenaires de VILLE_IA
- Communauté open source Python

## 📧 Contact

Pour questions ou support:
- Email: [contact]
- Website: [IRIU](https://iriu.ca)

---

**⭐ Si ce projet vous est utile, donnez-lui une étoile!**

---

*Généré avec ❤️ pour la résilience urbaine*
