"""
Pipeline complet reproductible
Exécute toutes les étapes du traitement
"""

import subprocess
import sys
from pathlib import Path

def run_script(script_name, description):
    """Execute un script Python et affiche les résultats"""
    print("\n" + "="*80)
    print(f"EXECUTING: {description}")
    print("="*80)

    try:
        result = subprocess.run(
            [sys.executable, script_name],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore'
        )

        if result.returncode == 0:
            print(f"[SUCCESS] {script_name}")
            # Print last 30 lines of output
            lines = result.stdout.split('\n')
            print('\n'.join(lines[-30:]))
        else:
            print(f"[ERROR] {script_name} failed with code {result.returncode}")
            print(result.stderr)
            return False

    except Exception as e:
        print(f"[EXCEPTION] Error running {script_name}: {e}")
        return False

    return True

def main():
    print("""
    ============================================================================
                     BUILDING RISK PRIORITIZATION PIPELINE

      Projet VILLE_IA - Identification des batiments a risque a Montreal
      Approche SANS geomatique - Intelligence textuelle et ML
    ============================================================================
    """)

    # Pipeline steps
    steps = [
        ("01_data_exploration.py", "Exploration des données"),
        ("02_intelligent_matching.py", "Matching intelligent sans géomatique"),
        ("03_ml_prioritization_model.py", "Modèle ML de priorisation"),
    ]

    success = True
    for script, description in steps:
        if not run_script(script, description):
            success = False
            print(f"\n[ABORT] Pipeline stopped due to error in {script}")
            break

    if success:
        print("\n" + "="*80)
        print("[COMPLETE] Pipeline executed successfully!")
        print("="*80)
        print("\nOutputs generated:")
        print("  - output_buildings_enriched.csv")
        print("  - output_buildings_prioritized.csv")
        print("  - output_top_100_priorities.csv")
        print("\nNext steps:")
        print("  - Review the prioritized buildings list")
        print("  - Launch the web dashboard: streamlit run 04_web_dashboard.py")
        print("  - Read the methodology document: METHODOLOGY.md")

    return success

if __name__ == "__main__":
    main()
