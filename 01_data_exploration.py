"""
Exploration des données pour le projet Building Risk Montreal
Sans utilisation de géomatique - approche alternative intelligente
"""

import pandas as pd
import numpy as np
import json
from pathlib import Path

# Configuration
DATA_DIR = Path("data")

def explore_dataset(filepath, name):
    """Explore un dataset et affiche ses caractéristiques"""
    print(f"\n{'='*80}")
    print(f"Dataset: {name}")
    print(f"{'='*80}")

    try:
        if filepath.suffix == '.csv':
            df = pd.read_csv(filepath, nrows=5)
            print(f"\nShape (first 5 rows): {df.shape}")
            print(f"\nColumns: {df.columns.tolist()}")
            print(f"\nFirst rows:")
            print(df.head())
            print(f"\nData types:")
            print(df.dtypes)

            # Load full for stats
            df_full = pd.read_csv(filepath)
            print(f"\nFull dataset shape: {df_full.shape}")
            print(f"\nMissing values:")
            print(df_full.isnull().sum())

            return df_full

        elif filepath.suffix == '.geojson':
            # Read geojson as text to understand structure
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            print(f"\nType: {data.get('type')}")
            print(f"\nNumber of features: {len(data.get('features', []))}")
            if data.get('features'):
                print(f"\nFirst feature properties:")
                print(data['features'][0].get('properties'))
            return data

        elif filepath.suffix == '.gpkg':
            print(f"\nGeoPackage file - will need geopandas to read")
            return None

    except Exception as e:
        print(f"Error reading {name}: {e}")
        return None

# Explore all datasets
datasets = {
    'batiments': DATA_DIR / 'batiments-municipaux.csv',
    'consommation': DATA_DIR / 'consommation-energetique-plus-2000m2-municipaux-2023.csv',
    'chaleur': DATA_DIR / 'ilots-de-chaleur-images-satellite-2023.geojson',
    'inondation': DATA_DIR / 'vdq-zonesinondablesreglementees.csv',
    'vulnerabilite': DATA_DIR / 'IndiceCanadienDeVulnérabilitéSociale.csv',
    'aire': DATA_DIR / 'AireAmenagee.csv'
}

data = {}
for name, filepath in datasets.items():
    result = explore_dataset(filepath, name)
    data[name] = result

print("\n" + "="*80)
print("EXPLORATION COMPLETE")
print("="*80)
