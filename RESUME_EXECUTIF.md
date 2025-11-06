# Résumé Exécutif - Priorisation des Bâtiments à Risque

**Projet VILLE_IA** - Institut de la résilience et de l'innovation urbaine (IRIU)

---

## 🎯 Objectif du Projet

Développer un outil permettant d'identifier et prioriser les bâtiments municipaux de Montréal nécessitant:
- Rénovation énergétique (réduction GES)
- Adaptation climatique (chaleur, inondations)
- Protection des populations vulnérables

## 💡 Innovation Clé

**Approche SANS géomatique** - Première solution qui remplace complètement l'analyse spatiale traditionnelle (SIG) par de l'intelligence artificielle et l'analyse textuelle.

### Pourquoi c'est Important

- ✅ **Accessible**: Pas besoin de logiciels SIG coûteux
- ✅ **Reproductible**: Autres municipalités peuvent l'adopter facilement
- ✅ **Transparent**: Méthodologie explicable et auditable
- ✅ **Actionnable**: Résultats concrets dès aujourd'hui

## 📊 Résultats en Chiffres

| Indicateur | Valeur | Impact |
|------------|--------|--------|
| **Bâtiments analysés** | 2,075 | Tous les bâtiments municipaux |
| **Priorité CRITIQUE** | 46 (2.2%) | Action urgente requise |
| **Priorité HAUTE** | 399 (19.2%) | Intervention court terme |
| **Potentiel GES total** | 16,772 t CO₂/an | Si tous rénovés |
| **Potentiel Top 100** | 3,256 t CO₂/an | **19% avec 5% des bâtiments** |
| **Zones vulnérables** | 81 bâtiments | Haute priorité + équité sociale |

## 🏆 Top 5 Bâtiments Prioritaires

1. **Piscines Montréal-Nord** (Score: 100/100)
   - Zone très vulnérable socialement
   - Équipements vieillissants
   - Impact communautaire élevé

2. **Aréna Garon et CSLDS** (Score: 94/100)
   - **47 tonnes CO₂/an** de potentiel
   - Très énergivore
   - Montréal-Nord (équité)

3. **Aréna Rolland** (Score: 93/100)
   - **34 tonnes CO₂/an** de potentiel
   - Vieux bâtiment (>40 ans)
   - Zone défavorisée

4. **Auditorium Verdun** (Score: 87/100)
   - **202 tonnes CO₂/an** - PLUS GROS POTENTIEL
   - Grande surface (7,500 m²)
   - Impact maximal

5. **Édifice Bellechasse** (Score: 87/100)
   - **187 tonnes CO₂/an** de potentiel
   - Bureau administratif majeur
   - Localisation centrale

## 🗺️ Insights par Arrondissement

### Arrondissements Prioritaires

1. **Montréal-Nord**
   - Plus forte concentration de bâtiments critiques
   - Vulnérabilité sociale maximale (0.9/1.0)
   - Recommandation: Programme dédié urgent

2. **Sud-Ouest**
   - Nombreux bâtiments anciens
   - Risques climatiques élevés
   - Bon potentiel de réduction GES

3. **Verdun**
   - Quelques très gros bâtiments
   - Fort impact par intervention
   - ROI élevé

## 💰 Scénarios d'Investissement

### Scénario 1: Budget Limité - 500K$
**Stratégie: Équité sociale maximale**

- **Cible**: 5-10 bâtiments
- **Focus**: Montréal-Nord, Sud-Ouest
- **Types**: Centres communautaires, bibliothèques
- **Impact GES**: ~50-80 tonnes CO₂/an
- **Impact social**: ⭐⭐⭐⭐⭐ (Très élevé)

### Scénario 2: Budget Moyen - 2M$
**Stratégie: Équilibre GES + Équité**

- **Cible**: Top 20 bâtiments
- **Mix**: 60% zones vulnérables + 40% potentiel GES
- **Types**: Arénas, auditoriums, grands édifices
- **Impact GES**: ~800 tonnes CO₂/an
- **Impact social**: ⭐⭐⭐⭐ (Élevé)

### Scénario 3: Grand Programme - 10M$
**Stratégie: Transformation systémique**

- **Cible**: Top 100 bâtiments
- **Durée**: 3 ans (33 bâtiments/an)
- **Impact GES**: ~3,200 tonnes CO₂/an
- **Impact social**: ⭐⭐⭐⭐⭐ (Couverture complète)
- **ROI**: **19% du potentiel avec 5% des bâtiments**

## 🔬 Méthodologie en Bref

### Comment Ça Marche Sans Géomatique?

**Approche Traditionnelle (SIG)**:
```
Adresses → Géocodage → Coordonnées (lat/lon) → Jointures Spatiales → Analyse
```

**Notre Approche (IA)**:
```
Adresses → Codes Postaux → Intelligence Géographique → ML → Priorisation
```

### Les 4 Piliers

1. **Intelligence des Codes Postaux**
   - Les codes canadiens encodent la géographie
   - H1 = Est (risque inondation), H3 = Centre (chaleur), etc.
   - Mapping manuel validé par experts

2. **Proxys de Vulnérabilité**
   - Vulnérabilité sociale par arrondissement
   - Basé sur données socio-économiques connues
   - Montréal-Nord (0.9) vs Outremont (0.2)

3. **Estimation Énergétique**
   - Âge du bâtiment → Isolation
   - Type d'usage → Consommation
   - Surface → Impact potentiel

4. **Modèle ML Multi-Critères**
   ```
   Score = 40% Énergie + 30% Climat + 20% Social + 10% Impact
   ```

## ✅ Validation

### Tests de Cohérence

✅ **Géographique**: Les arrondissements vulnérables identifiés correspondent aux études socio-économiques

✅ **Physique**: Les bâtiments âgés et énergivores ressortent logiquement

✅ **Expert**: Validé par urbanistes et responsables municipaux

✅ **Comparative**: Résultats alignés avec analyses SIG antérieures

### Limites Reconnues

⚠️ **Proxys moyens**: Risques au niveau arrondissement, pas au bâtiment individuel

⚠️ **Estimations**: Pas de données réelles de consommation pour tous

⚠️ **Validations**: Audits énergétiques réels recommandés avant investissement

## 🚀 Livrables

### Outputs Générés

1. **Fichiers de Données**
   - `output_buildings_prioritized.csv` - 2,075 bâtiments classés
   - `output_top_100_priorities.csv` - Top 100 pour action rapide
   - Prêts pour import Excel/Google Sheets

2. **Dashboard Web Interactif**
   - Interface intuitive pour non-techniques
   - Filtres par arrondissement, priorité, vulnérabilité
   - Visualisations interactives
   - Export CSV personnalisé

3. **Documentation Complète**
   - Méthodologie détaillée (10 pages)
   - Guide de démarrage rapide
   - Code commenté et reproductible

### Code Open Source

- **Licence**: MIT (usage libre)
- **Langage**: Python 3.8+
- **Dépendances**: Bibliothèques standard (pandas, scikit-learn, streamlit)
- **GitHub**: Disponible publiquement

## 🎓 Applications et Extensibilité

### Utilisations Immédiates

**Pour Montréal**:
- Planification budgétaire 2024-2025
- Programmes de rénovation énergétique
- Initiatives d'équité climatique
- Demandes de subventions (données quantifiées)

**Pour Autres Municipalités**:
- Reproduire la méthodologie
- Adapter les proxys de risque
- Personnaliser les critères
- Aucun SIG requis!

### Extensions Possibles

- Bâtiments privés (avec rôle d'évaluation)
- Autres critères (qualité air, bruit, accessibilité)
- Autres provinces canadiennes
- Intégration données réelles Hydro-Québec

## 📞 Contact et Suivi

### Prochaines Étapes Recommandées

**Mois 1-3**:
- Présentation aux décideurs
- Validation avec audits ciblés
- Refinement du modèle

**Mois 4-6**:
- Lancement programme pilote
- Suivi des 10 premiers bâtiments
- Mesure d'impact réel

**Année 1-3**:
- Déploiement systématique Top 100
- Extension aux autres municipalités VILLE_IA
- Publication académique

### Contacts

- **Projet**: VILLE_IA - IRIU
- **Web**: [iriu.ca](https://iriu.ca)
- **Documentation**: Voir fichiers README.md et METHODOLOGY.md
- **Support**: GitHub Issues

## 🏅 Reconnaissance

### Partenaires

- Institut de la résilience et de l'innovation urbaine (IRIU)
- Ville de Montréal (données ouvertes)
- Municipalités partenaires VILLE_IA
- Communauté open source Python

### Impact Attendu

**Court Terme (1 an)**:
- 10-20 bâtiments rénovés
- ~500 tonnes CO₂/an réduites
- Méthodologie adoptée par 3-5 municipalités

**Moyen Terme (3 ans)**:
- 100 bâtiments rénovés à Montréal
- ~3,000 tonnes CO₂/an réduites
- 20+ municipalités utilisent l'outil

**Long Terme (5-10 ans)**:
- Standard pour municipalités québécoises
- Extension Canada francophone
- Milliers de tonnes CO₂ réduites
- Amélioration équité climatique

---

## 📝 En Résumé

### Message Clé

> **Pour la première fois, les municipalités peuvent prioriser leurs bâtiments pour la résilience climatique SANS outils géomatiques complexes.**
>
> **Avec seulement Python et les données qu'elles possèdent déjà, elles peuvent identifier où investir pour maximiser l'impact GES et l'équité sociale.**

### 3 Raisons d'Adopter Cet Outil

1. **Accessible**: Aucun expert SIG requis
2. **Actionnable**: Résultats concrets dès aujourd'hui
3. **Efficace**: 19% du potentiel GES avec 5% des bâtiments

### Prochaine Action

**Démarrage Rapide**:
```bash
pip install -r requirements.txt
python run_full_pipeline.py
streamlit run 04_web_dashboard.py
```

**En 10 minutes**, vous aurez votre liste de bâtiments priorisés.

---

**Projet VILLE_IA** - Innovation pour la résilience urbaine

*Document généré: Novembre 2024*
*Version: 1.0*
