"""
Modèle de Machine Learning pour prioriser les bâtiments
Combine: énergie, risques climatiques, vulnérabilité sociale

Approche sans géomatique:
- Utilise les enrichissements de codes postaux
- Analyse des caractéristiques des bâtiments
- Scoring multi-critères avec ML
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingRegressor
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import warnings
warnings.filterwarnings('ignore')

class BuildingRiskPrioritizer:
    """
    Modèle ML pour prioriser les bâtiments basé sur:
    1. Consommation énergétique / Émissions GES
    2. Vulnérabilité climatique (chaleur + inondations)
    3. Vulnérabilité sociale
    4. État du bâtiment (âge, surface)
    """

    def __init__(self):
        self.scaler = StandardScaler()
        self.risk_scaler = MinMaxScaler()
        self.features = []

    def calculate_building_age_risk(self, construction_year):
        """
        Les vieux bâtiments sont moins efficaces énergétiquement
        et plus vulnérables
        """
        current_year = 2024
        if pd.isna(construction_year) or construction_year == 0:
            return 0.7  # Risk moyen si inconnu

        age = current_year - construction_year

        # Score de risque basé sur l'âge
        if age < 10:
            return 0.1  # Très récent, probablement efficace
        elif age < 30:
            return 0.3  # Relativement récent
        elif age < 50:
            return 0.6  # Nécessite probablement rénovation
        elif age < 75:
            return 0.8  # Vieux, haute priorité
        else:
            return 1.0  # Très vieux, priorité maximale

    def calculate_size_risk(self, area):
        """
        Les grands bâtiments ont plus d'impact potentiel
        """
        if pd.isna(area) or area == 0:
            return 0.5

        # Normalisation logarithmique
        # Plus grand = plus d'impact potentiel
        log_area = np.log10(area + 1)
        return min(1.0, log_area / 6)  # Normalise entre 0 et 1

    def estimate_energy_consumption_risk(self, row):
        """
        Estime le risque de consommation énergétique basé sur:
        - Âge du bâtiment
        - Surface
        - Type d'usage
        - Nombre d'étages
        """
        risk_score = 0.0
        factors = 0

        # Age factor
        if 'buildingConstrYear' in row:
            risk_score += self.calculate_building_age_risk(row['buildingConstrYear'])
            factors += 1

        # Size factor
        if 'buildingArea' in row and not pd.isna(row['buildingArea']):
            risk_score += self.calculate_size_risk(row['buildingArea'])
            factors += 1
        elif 'builtArea' in row and not pd.isna(row['builtArea']):
            risk_score += self.calculate_size_risk(row['builtArea'])
            factors += 1

        # Usage factor - certains usages sont plus énergivores
        high_consumption_usages = [
            'PISCINE', 'ARÉNA', 'ARENA', 'CENTRE SPORTIF', 'BIBLIOTHÈQUE',
            'CASERNE', 'HÔPITAL', 'CENTRE COMMUNAUTAIRE'
        ]

        if 'usageName' in row and not pd.isna(row['usageName']):
            usage = str(row['usageName']).upper()
            is_high_consumption = any(keyword in usage for keyword in high_consumption_usages)
            if is_high_consumption:
                risk_score += 0.8
            else:
                risk_score += 0.3
            factors += 1

        # Floor factor - plus d'étages = plus de consommation
        if 'floorAmount' in row and not pd.isna(row['floorAmount']):
            floors = row['floorAmount']
            if floors > 10:
                risk_score += 0.9
            elif floors > 5:
                risk_score += 0.7
            elif floors > 2:
                risk_score += 0.5
            else:
                risk_score += 0.3
            factors += 1

        return risk_score / factors if factors > 0 else 0.5

    def calculate_combined_climate_risk(self, row):
        """
        Combine les risques de chaleur et d'inondation
        """
        flood_risk = row.get('postal_flood_risk', 0.5)
        heat_risk = row.get('postal_heat_risk', 0.5)

        # Weighted combination - les deux sont importants
        combined = (flood_risk * 0.5) + (heat_risk * 0.5)

        return combined

    def normalize_borough_simple(self, borough):
        """Normalisation simple des noms d'arrondissements"""
        if pd.isna(borough):
            return 'UNKNOWN'

        borough = str(borough).upper().strip()

        # Remplacer les caractères spéciaux
        replacements = {
            'É': 'E', 'È': 'E', 'Ê': 'E',
            'À': 'A', 'Â': 'A',
            'Î': 'I', 'Ô': 'O', 'Ù': 'U',
            '-': '-', '/': '-', '  ': ' '
        }
        for old, new in replacements.items():
            borough = borough.replace(old, new)

        return borough

    def calculate_social_vulnerability_proxy(self, row):
        """
        Proxy de vulnérabilité sociale basé sur l'arrondissement
        Certains arrondissements ont plus de défavorisation
        """
        # Mapping basé sur données connues de Montréal
        vulnerability_by_borough = {
            'MONTREAL-NORD': 0.9,
            'MERCIER-HOCHELAGA-MAISONNEUVE': 0.8,
            'VILLERAY-SAINT-MICHEL-PARC-EXTENSION': 0.8,
            'RIVIERE-DES-PRAIRIES-POINTE-AUX-TREMBLES': 0.7,
            'R-D-P / P-A-T': 0.7,
            'ROSEMONT-PETITE-PATRIE': 0.6,
            'PLATEAU-MONT-ROYAL': 0.4,
            'AHUNTSIC-CARTIERVILLE': 0.6,
            'SUD-OUEST': 0.7,
            'SAINT-LEONARD': 0.6,
            'LASALLE': 0.6,
            'VERDUN': 0.6,
            'LACHINE': 0.6,
            'VILLE-MARIE': 0.5,  # Mixte
            'COTE-DES-NEIGES-NOTRE-DAME-DE-GRACE': 0.7,
            'COTE-DES-NEIGES / N-D-DE-GRACE': 0.7,
            'OUTREMONT': 0.2,
            'ANJOU': 0.5,
            'SAINT-LAURENT': 0.6,
            'ILE-BIZARD-SAINTE-GENEVIEVE': 0.3,
            'PIERREFONDS-ROXBORO': 0.4
        }

        borough = self.normalize_borough_simple(row.get('boroughName', ''))

        return vulnerability_by_borough.get(borough, 0.5)

    def create_feature_matrix(self, df):
        """
        Crée la matrice de features pour le modèle ML
        """
        print("\nCreating feature matrix...")

        features_df = pd.DataFrame()

        # Feature 1: Age Risk
        features_df['age_risk'] = df.apply(
            lambda row: self.calculate_building_age_risk(row.get('buildingConstrYear')),
            axis=1
        )

        # Feature 2: Size/Impact Potential
        features_df['size_impact'] = df.apply(
            lambda row: self.calculate_size_risk(row.get('buildingArea', row.get('builtArea', 0))),
            axis=1
        )

        # Feature 3: Energy Consumption Risk (estimated)
        features_df['energy_risk'] = df.apply(
            self.estimate_energy_consumption_risk,
            axis=1
        )

        # Feature 4: Climate Risk (flood + heat)
        features_df['climate_risk'] = df.apply(
            self.calculate_combined_climate_risk,
            axis=1
        )

        # Feature 5: Social Vulnerability
        features_df['social_vulnerability'] = df.apply(
            self.calculate_social_vulnerability_proxy,
            axis=1
        )

        # Feature 6: Floor count normalized
        features_df['floor_count_norm'] = df['floorAmount'].fillna(df['floorAmount'].median())
        features_df['floor_count_norm'] = MinMaxScaler().fit_transform(
            features_df[['floor_count_norm']]
        )

        # Feature 7: Has basement (risk d'inondation)
        features_df['has_basement'] = (df['basementAmount'].fillna(0) > 0).astype(int)

        print(f"Created {len(features_df.columns)} features")
        print(features_df.describe())

        self.features = features_df.columns.tolist()
        return features_df

    def calculate_priority_score(self, features_df):
        """
        Calcule un score de priorité composite
        Approche multi-critères:
        - 40% Potentiel de réduction GES (énergie)
        - 30% Vulnérabilité climatique
        - 20% Vulnérabilité sociale
        - 10% Impact (taille)
        """
        priority_score = (
            features_df['energy_risk'] * 0.40 +
            features_df['climate_risk'] * 0.30 +
            features_df['social_vulnerability'] * 0.20 +
            features_df['size_impact'] * 0.10
        )

        # Bonus pour bâtiments très vieux avec risque combiné
        age_climate_bonus = (
            (features_df['age_risk'] > 0.7) &
            (features_df['climate_risk'] > 0.6)
        ).astype(int) * 0.15

        priority_score = priority_score + age_climate_bonus

        # Normaliser entre 0 et 100
        priority_score = MinMaxScaler(feature_range=(0, 100)).fit_transform(
            priority_score.values.reshape(-1, 1)
        ).flatten()

        return priority_score

    def cluster_buildings(self, features_df, n_clusters=5):
        """
        Cluster les bâtiments en groupes similaires
        Pour identifier les typologies de risques
        """
        print(f"\nClustering buildings into {n_clusters} groups...")

        # Standardize features
        features_scaled = self.scaler.fit_transform(features_df)

        # K-Means clustering
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        clusters = kmeans.fit_predict(features_scaled)

        # Analyze clusters
        cluster_profiles = pd.DataFrame(features_scaled, columns=features_df.columns)
        cluster_profiles['cluster'] = clusters

        print("\nCluster profiles:")
        for i in range(n_clusters):
            cluster_data = cluster_profiles[cluster_profiles['cluster'] == i]
            print(f"\nCluster {i} (n={len(cluster_data)}):")
            print(cluster_data.drop('cluster', axis=1).mean().round(3))

        return clusters, cluster_profiles

    def create_intervention_recommendations(self, row, priority_score):
        """
        Génère des recommandations d'intervention basées sur le profil du bâtiment
        """
        recommendations = []

        # Energy efficiency
        if row.get('age_risk', 0) > 0.6:
            recommendations.append("Isolation thermique et remplacement des fenêtres")
            recommendations.append("Mise à niveau du système de chauffage")

        if row.get('energy_risk', 0) > 0.7:
            recommendations.append("Audit énergétique complet")
            recommendations.append("Installation de panneaux solaires si possible")

        # Climate adaptation
        if row.get('climate_risk', 0) > 0.6:
            if row.get('postal_flood_risk', 0) > 0.6:
                recommendations.append("Mesures de protection contre les inondations")
                if row.get('has_basement', 0) == 1:
                    recommendations.append("Imperméabilisation du sous-sol")

            if row.get('postal_heat_risk', 0) > 0.6:
                recommendations.append("Installation de toits verts ou toits blancs")
                recommendations.append("Augmentation de la végétation périmétrique")
                recommendations.append("Système de climatisation efficace")

        # Social priority
        if row.get('social_vulnerability', 0) > 0.7:
            recommendations.append("PRIORITÉ SOCIALE - Financement public recommandé")

        # Prioritization
        if priority_score > 80:
            recommendations.insert(0, "⚠️ HAUTE PRIORITÉ - Intervention urgente recommandée")
        elif priority_score > 60:
            recommendations.insert(0, "⚡ PRIORITÉ MOYENNE-HAUTE")
        elif priority_score > 40:
            recommendations.insert(0, "📋 PRIORITÉ MOYENNE")

        return " | ".join(recommendations) if recommendations else "Suivi régulier"


def main():
    print("="*80)
    print("BUILDING RISK PRIORITIZATION MODEL")
    print("="*80)

    # Load enriched data
    buildings = pd.read_csv('output_buildings_enriched.csv')
    print(f"\nLoaded {len(buildings)} buildings")

    # Initialize model
    model = BuildingRiskPrioritizer()

    # Create features
    features = model.create_feature_matrix(buildings)

    # Calculate priority scores
    print("\nCalculating priority scores...")
    buildings['priority_score'] = model.calculate_priority_score(features)

    # Classify priority levels
    buildings['priority_level'] = pd.cut(
        buildings['priority_score'],
        bins=[0, 40, 60, 80, 100],
        labels=['Low', 'Medium', 'High', 'Critical']
    )

    # Cluster analysis
    buildings['risk_cluster'], cluster_profiles = model.cluster_buildings(features, n_clusters=5)

    # Add individual feature scores for transparency
    for col in features.columns:
        buildings[f'score_{col}'] = features[col]

    # Generate recommendations
    print("\nGenerating intervention recommendations...")
    buildings['recommendations'] = buildings.apply(
        lambda row: model.create_intervention_recommendations(
            row, row['priority_score']
        ),
        axis=1
    )

    # Estimate impact
    print("\nEstimating potential impact...")

    # GES reduction potential (tonnes CO2/year)
    # Basé sur: surface * facteur énergie * facteur âge
    buildings['estimated_ges_reduction_potential'] = (
        buildings['buildingArea'].fillna(buildings['builtArea'].fillna(1000)) / 100 *
        buildings['score_energy_risk'] *
        buildings['score_age_risk'] *
        2.5  # Facteur de conversion moyen
    )

    # Sort by priority
    buildings_sorted = buildings.sort_values('priority_score', ascending=False)

    # Display top priorities
    print("\n" + "="*80)
    print("TOP 20 PRIORITY BUILDINGS")
    print("="*80)

    display_cols = [
        'buildingName', 'address', 'boroughName',
        'priority_score', 'priority_level',
        'score_energy_risk', 'score_climate_risk', 'score_social_vulnerability',
        'estimated_ges_reduction_potential'
    ]

    print(buildings_sorted[display_cols].head(20).to_string())

    # Summary statistics
    print("\n" + "="*80)
    print("SUMMARY STATISTICS")
    print("="*80)

    print(f"\nPriority Level Distribution:")
    print(buildings['priority_level'].value_counts().sort_index())

    print(f"\nTotal estimated GES reduction potential: {buildings['estimated_ges_reduction_potential'].sum():.1f} tonnes CO2/year")

    print(f"\nTop 100 buildings GES potential: {buildings_sorted.head(100)['estimated_ges_reduction_potential'].sum():.1f} tonnes CO2/year")

    print(f"\nHigh-risk buildings in vulnerable areas:")
    vulnerable = buildings[
        (buildings['priority_score'] > 60) &
        (buildings['score_social_vulnerability'] > 0.7)
    ]
    print(f"  Count: {len(vulnerable)}")
    print(f"  GES potential: {vulnerable['estimated_ges_reduction_potential'].sum():.1f} tonnes CO2/year")

    # Save results
    output_file = 'output_buildings_prioritized.csv'
    buildings_sorted.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"\n[OK] Results saved to {output_file}")

    # Save top 100 priority list
    top_100_file = 'output_top_100_priorities.csv'
    buildings_sorted.head(100).to_csv(top_100_file, index=False, encoding='utf-8-sig')
    print(f"[OK] Top 100 priorities saved to {top_100_file}")

    return buildings_sorted, features


if __name__ == "__main__":
    results, features = main()
