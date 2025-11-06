# 🚀 Guide de Démarrage Rapide

## Installation en 3 Minutes

### 1. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 2. Exécuter le pipeline

```bash
python run_full_pipeline.py
```

### 3. Lancer le dashboard

```bash
streamlit run 04_web_dashboard.py
```

C'est tout! 🎉

---

## Utilisation du Dashboard

### Interface pour Utilisateurs Non-Techniques

Le dashboard est conçu pour être **extrêmement simple** à utiliser:

#### 1. Page d'Accueil
- **Vue d'ensemble** des bâtiments analysés
- **Indicateurs clés** en haut de page
- **Graphiques intuitifs** sans jargon technique

#### 2. Filtres (Barre Latérale)
- **Arrondissement**: Sélectionnez une zone spécifique
- **Niveau de priorité**: Filtrez par urgence
- **Score minimum**: Ajustez le seuil de priorité
- **Vulnérabilité sociale**: Ciblez les zones défavorisées

#### 3. Onglets Principaux

##### 📊 Vue d'Ensemble
- Graphique circulaire: Distribution des priorités
- Top 10 bâtiments
- Carte de risques multi-dimensionnelle

##### 🗺️ Par Arrondissement
- Statistiques détaillées par zone
- Comparaison des arrondissements
- Tableau récapitulatif

##### ⚡ Analyse Détaillée
- Distributions des facteurs de risque
- Analyse par âge de bâtiment
- Corrélations (pour experts)

##### 📋 Liste Complète
- Tableau interactif de tous les bâtiments
- Mode simplifié ou mode expert
- Export CSV disponible

#### 4. Télécharger les Résultats
- Bouton **"Télécharger (CSV)"** en bas de page
- Import direct dans Excel/Google Sheets

---

## Scénarios d'Utilisation

### Scénario 1: Identifier les Urgences

**Objectif**: Trouver les bâtiments nécessitant une action immédiate

**Étapes**:
1. Ouvrir le dashboard
2. Filtrer: Priorité = "Critical"
3. Noter les bâtiments dans votre arrondissement
4. Télécharger la liste
5. Planifier des inspections

**Temps**: 2 minutes

---

### Scénario 2: Budget Annuel

**Objectif**: Planifier les investissements de l'année

**Étapes**:
1. Filtrer: Score > 60 (Haute priorité)
2. Trier par "Potentiel GES"
3. Sélectionner les 10-20 premiers selon budget
4. Exporter vers Excel
5. Calculer les coûts estimés

**Temps**: 5 minutes

---

### Scénario 3: Équité Sociale

**Objectif**: Prioriser les zones vulnérables

**Étapes**:
1. Filtrer: Vulnérabilité sociale > 0.7
2. Filtrer: Priorité >= Medium
3. Observer les arrondissements affectés
4. Exporter la liste
5. Intégrer dans programme d'équité

**Temps**: 3 minutes

---

### Scénario 4: Analyse Approfondie

**Objectif**: Comprendre les patterns de risque

**Étapes**:
1. Onglet "Analyse Détaillée"
2. Observer les distributions
3. Vérifier les corrélations
4. Identifier les tendances par âge
5. Documenter les insights

**Temps**: 15 minutes

---

## Interprétation des Résultats

### Score de Priorité (0-100)

| Score | Niveau | Signification | Action |
|-------|--------|---------------|--------|
| **80-100** | 🔴 Critique | Risques multiples élevés | Action urgente (< 6 mois) |
| **60-80** | 🟠 Haute | Risques significatifs | Planifier court terme (< 1 an) |
| **40-60** | 🟡 Moyenne | Risques modérés | Planifier moyen terme (1-3 ans) |
| **0-40** | 🟢 Faible | Risques limités | Suivi régulier |

### Facteurs de Risque

#### Risque Énergétique (0-1)
- **> 0.7**: Très énergivore, GES élevé
- **0.5-0.7**: Consommation importante
- **< 0.5**: Relativement efficace

#### Risque Climatique (0-1)
- **> 0.7**: Forte exposition chaleur/inondation
- **0.5-0.7**: Exposition modérée
- **< 0.5**: Faible exposition

#### Vulnérabilité Sociale (0-1)
- **> 0.7**: Zone très défavorisée
- **0.5-0.7**: Défavorisation modérée
- **< 0.5**: Zone favorisée

### Potentiel GES
**Tonnes CO₂/an réductibles** si le bâtiment est rénové

- **> 100 tonnes**: Impact très important
- **50-100 tonnes**: Impact important
- **10-50 tonnes**: Impact modéré
- **< 10 tonnes**: Impact limité

---

## Questions Fréquentes (FAQ)

### Q1: D'où viennent ces données?
**R**: Données ouvertes de la Ville de Montréal et sources publiques (Hydro-Québec, RNCan, INSPQ).

### Q2: Comment les scores sont-ils calculés?
**R**: Modèle ML combinant 4 facteurs:
- 40% Risque énergétique
- 30% Risque climatique
- 20% Vulnérabilité sociale
- 10% Potentiel d'impact (taille)

### Q3: Pourquoi certains bâtiments ont-ils des données manquantes?
**R**: Données non disponibles dans les sources publiques. Le modèle utilise des moyennes dans ce cas.

### Q4: Le potentiel GES est-il garanti?
**R**: Non, c'est une **estimation** basée sur des modèles. Un audit énergétique réel est nécessaire pour confirmer.

### Q5: Puis-je utiliser ceci pour d'autres villes?
**R**: Oui! La méthodologie est **reproductible**. Voir [METHODOLOGY.md](METHODOLOGY.md) pour adapter.

### Q6: Comment sont gérés les codes postaux manquants?
**R**: Le système utilise des valeurs par défaut (risque moyen = 0.5) pour assurer une couverture complète.

### Q7: Puis-je ajouter mes propres critères?
**R**: Oui! Le code est modulaire. Voir section "Extensibilité" dans [METHODOLOGY.md](METHODOLOGY.md).

### Q8: Les résultats sont-ils validés?
**R**: Les patterns observés sont cohérents avec la littérature et validés par des experts. Mais ce n'est pas un audit énergétique officiel.

---

## Commandes Utiles

### Exécution

```bash
# Pipeline complet
python run_full_pipeline.py

# Étape par étape
python 01_data_exploration.py
python 02_intelligent_matching.py
python 03_ml_prioritization_model.py

# Dashboard web
streamlit run 04_web_dashboard.py

# Notebook Jupyter
jupyter notebook buildings_risk.ipynb
```

### Fichiers Générés

```
output_buildings_enriched.csv       # Bâtiments avec enrichissements
output_buildings_prioritized.csv    # Tous les résultats complets
output_top_100_priorities.csv       # Top 100 prioritaires
```

### Nettoyage

```bash
# Supprimer les fichiers de sortie
rm output_*.csv

# Re-générer proprement
python run_full_pipeline.py
```

---

## Support et Contact

### Documentation
- **Guide rapide**: Ce fichier
- **Méthodologie complète**: [METHODOLOGY.md](METHODOLOGY.md)
- **README technique**: [README.md](README.md)
- **Code commenté**: Dans chaque fichier .py

### Aide
1. Consultez d'abord la [METHODOLOGY.md](METHODOLOGY.md)
2. Vérifiez les FAQ ci-dessus
3. Examinez le code (bien commenté)
4. Contactez le projet VILLE_IA

### Contribution
Issues et Pull Requests bienvenues sur GitHub!

---

## Checklist de Démarrage

- [ ] Python 3.8+ installé
- [ ] Dépendances installées (`pip install -r requirements.txt`)
- [ ] Données dans le dossier `data/`
- [ ] Pipeline exécuté (`python run_full_pipeline.py`)
- [ ] Fichiers de sortie générés (output_*.csv)
- [ ] Dashboard testé (`streamlit run 04_web_dashboard.py`)
- [ ] Méthodologie lue (au moins le résumé)

---

**🎉 Vous êtes prêt! Bonne analyse!**

---

*Guide de démarrage rapide - Projet VILLE_IA*
*Dernière mise à jour: Novembre 2024*
