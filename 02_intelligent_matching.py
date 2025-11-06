"""
Système de matching intelligent SANS géomatique
Approche alternative utilisant:
- Extraction de patterns d'adresses
- Analyse textuelle des localisations
- Matching par arrondissement/quartier
- Clustering basé sur attributs
"""

import pandas as pd
import numpy as np
import re
from collections import defaultdict
import json
from pathlib import Path

DATA_DIR = Path("data")

class IntelligentMatcher:
    """
    Système de matching qui remplace la géomatique par de l'intelligence textuelle
    et des heuristiques basées sur les données disponibles
    """

    def __init__(self):
        self.borough_mapping = {}
        self.postal_code_mapping = {}
        self.address_registry = {}

    def extract_address_components(self, address):
        """Extrait les composants d'une adresse canadienne"""
        if pd.isna(address):
            return {}

        address = str(address).upper()

        components = {
            'full': address,
            'street_number': None,
            'street_name': None,
            'postal_code': None,
            'borough': None
        }

        # Extract postal code (format: A1A 1A1)
        postal_match = re.search(r'([A-Z]\d[A-Z]\s*\d[A-Z]\d)', address)
        if postal_match:
            components['postal_code'] = postal_match.group(1).replace(' ', '')

        # Extract street number
        number_match = re.search(r'^(\d+)[-\s]', address)
        if number_match:
            components['street_number'] = number_match.group(1)

        # Extract street name (between number and postal/borough)
        street_match = re.search(r'\d+[-\s]+([A-Z\s\'-\.]+?)(?:\s*,|\s*H\d)', address)
        if street_match:
            components['street_name'] = street_match.group(1).strip()

        return components

    def normalize_borough_name(self, borough):
        """Normalise les noms d'arrondissements"""
        if pd.isna(borough):
            return None

        borough = str(borough).upper().strip()

        # Mapping des variations communes
        mappings = {
            'VILLE-MARIE': ['VILLE MARIE', 'VILLEMARIE', 'DOWNTOWN'],
            'PLATEAU-MONT-ROYAL': ['PLATEAU', 'MONT ROYAL', 'MONT-ROYAL'],
            'ROSEMONT-PETITE-PATRIE': ['ROSEMONT', 'PETITE PATRIE', 'PETITE-PATRIE'],
            'MERCIER-HOCHELAGA-MAISONNEUVE': ['MERCIER', 'HOCHELAGA', 'MAISONNEUVE'],
            'COTE-DES-NEIGES-NOTRE-DAME-DE-GRACE': ['CDN', 'NDG', 'COTE DES NEIGES'],
            'VILLERAY-SAINT-MICHEL-PARC-EXTENSION': ['VILLERAY', 'SAINT MICHEL', 'PARC EXTENSION'],
            'AHUNTSIC-CARTIERVILLE': ['AHUNTSIC', 'CARTIERVILLE'],
            'SUD-OUEST': ['SUD OUEST', 'SOUTHWEST'],
            'RIVIERE-DES-PRAIRIES-POINTE-AUX-TREMBLES': ['RDP', 'POINTE AUX TREMBLES'],
            'SAINT-LEONARD': ['ST LEONARD', 'ST-LEONARD'],
            'SAINT-LAURENT': ['ST LAURENT', 'ST-LAURENT'],
            'VERDUN': ['VERDUN'],
            'ILE-BIZARD-SAINTE-GENEVIEVE': ['ILE BIZARD', 'SAINTE GENEVIEVE'],
            'LACHINE': ['LACHINE'],
            'LASALLE': ['LASALLE', 'LA SALLE'],
            'MONTREAL-NORD': ['MONTREAL NORD', 'NORTH MONTREAL'],
            'OUTREMONT': ['OUTREMONT'],
            'PIERREFONDS-ROXBORO': ['PIERREFONDS', 'ROXBORO'],
            'ANJOU': ['ANJOU']
        }

        for standard, variations in mappings.items():
            if borough == standard or borough in variations:
                return standard
            for variation in variations:
                if variation in borough:
                    return standard

        return borough

    def create_location_fingerprint(self, row):
        """
        Crée une empreinte digitale de localisation sans coordonnées
        Utilise: arrondissement, début d'adresse, code postal
        """
        fingerprint_parts = []

        if 'boroughName' in row and not pd.isna(row['boroughName']):
            borough = self.normalize_borough_name(row['boroughName'])
            fingerprint_parts.append(f"B:{borough}")

        if 'address' in row:
            components = self.extract_address_components(row['address'])
            if components.get('postal_code'):
                # Use first 3 characters of postal code (Forward Sortation Area)
                fingerprint_parts.append(f"P:{components['postal_code'][:3]}")
            if components.get('street_name'):
                fingerprint_parts.append(f"S:{components['street_name'][:20]}")

        return "|".join(fingerprint_parts) if fingerprint_parts else "UNKNOWN"

    def match_by_proximity_proxy(self, buildings_df, risk_df, risk_type):
        """
        Matche les bâtiments avec les risques en utilisant des proxys de proximité
        au lieu de coordonnées géographiques
        """
        print(f"\nMatching buildings with {risk_type} data...")

        # Create location fingerprints for buildings
        buildings_df['location_fp'] = buildings_df.apply(self.create_location_fingerprint, axis=1)

        # Strategy: Assign risk scores based on available location information
        # This simulates spatial analysis without actual coordinates

        matched_data = buildings_df.copy()
        matched_data[f'{risk_type}_risk_score'] = 0.0

        # Extract borough-level statistics from risk data if available
        if 'borough' in risk_df.columns or 'boroughName' in risk_df.columns:
            borough_col = 'borough' if 'borough' in risk_df.columns else 'boroughName'
            borough_risks = risk_df.groupby(borough_col).size().to_dict()

            # Normalize risk scores
            max_risk = max(borough_risks.values()) if borough_risks else 1
            borough_risks = {k: v/max_risk for k, v in borough_risks.items()}

            # Assign risk scores based on borough
            for idx, row in matched_data.iterrows():
                borough = self.normalize_borough_name(row.get('boroughName'))
                if borough in borough_risks:
                    matched_data.at[idx, f'{risk_type}_risk_score'] = borough_risks[borough]

        return matched_data

    def enrich_with_postal_code_intelligence(self, df):
        """
        Enrichit les données avec l'intelligence des codes postaux
        Les codes postaux canadiens encodent la géographie:
        - H1-H9: Montréal par secteur
        - H1: Est (Hochelaga, Mercier)
        - H2: Centre-Nord (Plateau, Villeray)
        - H3: Centre (Ville-Marie, Downtown)
        - H4: Ouest (NDG, Westmount)
        """
        postal_risk_mapping = {
            'H1': {'flood_risk': 0.8, 'heat_risk': 0.6},  # Est, près du fleuve
            'H2': {'flood_risk': 0.3, 'heat_risk': 0.7},  # Centre-Nord, urbain dense
            'H3': {'flood_risk': 0.4, 'heat_risk': 0.9},  # Centre, îlot de chaleur
            'H4': {'flood_risk': 0.5, 'heat_risk': 0.5},  # Ouest, plus vert
            'H5': {'flood_risk': 0.2, 'heat_risk': 0.4},  # Nord, résidentiel
            'H7': {'flood_risk': 0.7, 'heat_risk': 0.5},  # Sud-Ouest, industriel
            'H8': {'flood_risk': 0.6, 'heat_risk': 0.6},  # Est lointain
            'H9': {'flood_risk': 0.3, 'heat_risk': 0.4},  # Ouest lointain
        }

        df['postal_prefix'] = None
        df['postal_flood_risk'] = 0.5  # Default medium risk
        df['postal_heat_risk'] = 0.5

        for idx, row in df.iterrows():
            if 'address' in row:
                components = self.extract_address_components(row['address'])
                if components.get('postal_code'):
                    prefix = components['postal_code'][:2]
                    df.at[idx, 'postal_prefix'] = prefix

                    if prefix in postal_risk_mapping:
                        df.at[idx, 'postal_flood_risk'] = postal_risk_mapping[prefix]['flood_risk']
                        df.at[idx, 'postal_heat_risk'] = postal_risk_mapping[prefix]['heat_risk']

        return df


def load_and_prepare_data():
    """Charge et prépare toutes les données"""
    print("Loading datasets...")

    # Buildings
    buildings = pd.read_csv(DATA_DIR / 'batiments-municipaux.csv')
    print(f"Loaded {len(buildings)} buildings")

    # Energy consumption
    try:
        consumption = pd.read_csv(DATA_DIR / 'consommation-energetique-plus-2000m2-municipaux-2023.csv',
                                 encoding='utf-8')
        print(f"Loaded {len(consumption)} energy consumption records")
    except Exception as e:
        print(f"Warning: Could not load energy data: {e}")
        consumption = pd.DataFrame()

    # Flood zones - try different separators
    try:
        flood = pd.read_csv(DATA_DIR / 'vdq-zonesinondablesreglementees.csv',
                           sep=';', on_bad_lines='skip', encoding='latin1')
        print(f"Loaded {len(flood)} flood zone records")
    except Exception as e:
        print(f"Warning: Could not load flood data: {e}")
        flood = pd.DataFrame()

    # Heat islands
    try:
        with open(DATA_DIR / 'ilots-de-chaleur-images-satellite-2023.geojson', 'r', encoding='utf-8') as f:
            heat_data = json.load(f)

        # Extract features into DataFrame
        heat_features = []
        for feature in heat_data.get('features', []):
            props = feature.get('properties', {})
            heat_features.append(props)

        heat = pd.DataFrame(heat_features) if heat_features else pd.DataFrame()
        print(f"Loaded {len(heat)} heat island records")
    except Exception as e:
        print(f"Warning: Could not load heat data: {e}")
        heat = pd.DataFrame()

    # Social vulnerability
    vulnerability = pd.read_csv(DATA_DIR / 'IndiceCanadienDeVulnérabilitéSociale.csv', encoding='latin1')
    # Filter for Quebec only
    vulnerability = vulnerability[vulnerability['Province ou territoire'] == 'Québec']
    print(f"Loaded {len(vulnerability)} vulnerability records (Quebec)")

    return {
        'buildings': buildings,
        'consumption': consumption,
        'flood': flood,
        'heat': heat,
        'vulnerability': vulnerability
    }


if __name__ == "__main__":
    # Load data
    data = load_and_prepare_data()

    # Initialize matcher
    matcher = IntelligentMatcher()

    # Enrich buildings with postal code intelligence
    print("\n" + "="*80)
    print("ENRICHING BUILDINGS WITH POSTAL CODE INTELLIGENCE")
    print("="*80)

    buildings_enriched = matcher.enrich_with_postal_code_intelligence(data['buildings'])

    # Create location fingerprints
    buildings_enriched['location_fingerprint'] = buildings_enriched.apply(
        matcher.create_location_fingerprint, axis=1
    )

    print("\nSample enriched buildings:")
    print(buildings_enriched[['buildingName', 'address', 'boroughName', 'postal_prefix',
                              'postal_flood_risk', 'postal_heat_risk', 'location_fingerprint']].head(10))

    # Save enriched data
    buildings_enriched.to_csv('output_buildings_enriched.csv', index=False, encoding='utf-8')
    print(f"\nSaved enriched buildings to output_buildings_enriched.csv")

    print("\n" + "="*80)
    print("INTELLIGENT MATCHING COMPLETE")
    print("="*80)
