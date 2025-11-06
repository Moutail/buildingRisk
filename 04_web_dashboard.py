"""
Dashboard interactif pour la priorisation des bâtiments à risque
Interface intuitive pour utilisateurs non-techniques
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Configuration de la page
st.set_page_config(
    page_title="Batiments a Risque - Montreal",
    page_icon=":office:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé pour un design moderne
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem;
        background: linear-gradient(90deg, #e8f4f8 0%, #ffffff 100%);
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 0.5rem 0;
    }
    .priority-critical {
        background-color: #ff4444;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 5px;
        font-weight: bold;
    }
    .priority-high {
        background-color: #ff8c00;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 5px;
        font-weight: bold;
    }
    .priority-medium {
        background-color: #ffd700;
        color: black;
        padding: 0.3rem 0.8rem;
        border-radius: 5px;
        font-weight: bold;
    }
    .priority-low {
        background-color: #90ee90;
        color: black;
        padding: 0.3rem 0.8rem;
        border-radius: 5px;
        font-weight: bold;
    }
    .info-box {
        background-color: #e8f4f8;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Charge les données de priorisation"""
    try:
        df = pd.read_csv('output_buildings_prioritized.csv', encoding='utf-8-sig')
        return df
    except FileNotFoundError:
        st.error("ATTENTION: Fichier de donnees non trouve. Veuillez executer le pipeline d'abord.")
        st.info("Executez: python run_full_pipeline.py")
        st.stop()

def get_priority_color(priority_level):
    """Retourne la couleur selon le niveau de priorité"""
    colors = {
        'Critical': '#ff4444',
        'High': '#ff8c00',
        'Medium': '#ffd700',
        'Low': '#90ee90'
    }
    return colors.get(priority_level, '#cccccc')

def create_gauge_chart(value, title, max_value=100):
    """Crée un graphique de type jauge"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': title, 'font': {'size': 20}},
        delta={'reference': max_value * 0.5},
        gauge={
            'axis': {'range': [None, max_value], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, max_value * 0.4], 'color': '#90ee90'},
                {'range': [max_value * 0.4, max_value * 0.6], 'color': '#ffd700'},
                {'range': [max_value * 0.6, max_value * 0.8], 'color': '#ff8c00'},
                {'range': [max_value * 0.8, max_value], 'color': '#ff4444'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': max_value * 0.8
            }
        }
    ))

    fig.update_layout(
        height=250,
        margin=dict(l=20, r=20, t=50, b=20),
        paper_bgcolor="white",
        font={'color': "darkblue", 'family': "Arial"}
    )

    return fig

def main():
    # Header
    st.markdown('<div class="main-header">Priorisation des Batiments a Risque - Montreal</div>', unsafe_allow_html=True)

    # Introduction pour utilisateurs non-techniques
    with st.expander("INFO: Comment utiliser ce tableau de bord ?", expanded=False):
        st.markdown("""
        ### Bienvenue sur l'outil de priorisation des batiments

        Cet outil vous aide a identifier les batiments municipaux de Montreal qui devraient etre priorises pour:
        - **Renovation energetique** (reduction des emissions de GES)
        - **Adaptation climatique** (protection contre chaleur et inondations)
        - **Equite sociale** (priorite aux zones defavorisees)

        **Comment naviguer:**
        1. Utilisez la barre laterale pour filtrer les batiments
        2. Consultez les indicateurs cles en haut de page
        3. Explorez les graphiques pour comprendre les tendances
        4. Telechargez la liste priorisee pour planifier vos interventions

        **Niveaux de priorite:**
        - **Critique** (80-100): Action urgente requise
        - **Haute** (60-80): Intervention recommandee a court terme
        - **Moyenne** (40-60): Planification a moyen terme
        - **Faible** (0-40): Suivi regulier
        """)

    # Charger les données
    df = load_data()

    # Sidebar - Filtres
    st.sidebar.header("Filtres")

    # Filtre par arrondissement
    boroughs = ['Tous'] + sorted(df['boroughName'].dropna().unique().tolist())
    selected_borough = st.sidebar.selectbox("Arrondissement", boroughs)

    # Filtre par niveau de priorité
    priority_levels = ['Tous'] + sorted(df['priority_level'].dropna().unique().tolist())
    selected_priority = st.sidebar.selectbox("Niveau de priorité", priority_levels)

    # Filtre par score minimum
    min_score = st.sidebar.slider("Score de priorité minimum", 0, 100, 0)

    # Filtre par vulnérabilité sociale
    social_vuln_threshold = st.sidebar.slider("Vulnérabilité sociale minimum", 0.0, 1.0, 0.0)

    # Appliquer les filtres
    filtered_df = df.copy()

    if selected_borough != 'Tous':
        filtered_df = filtered_df[filtered_df['boroughName'] == selected_borough]

    if selected_priority != 'Tous':
        filtered_df = filtered_df[filtered_df['priority_level'] == selected_priority]

    filtered_df = filtered_df[filtered_df['priority_score'] >= min_score]
    filtered_df = filtered_df[filtered_df['score_social_vulnerability'] >= social_vuln_threshold]

    # Sidebar - Information
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    ### À propos
    **Projet VILLE_IA**

    Développé pour l'Institut de la résilience et de l'innovation urbaine (IRIU)

    **Méthodologie:**
    Approche sans géomatique utilisant l'intelligence des codes postaux et le machine learning.
    """)

    # Metriques principales
    st.markdown("### Indicateurs Cles")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Bâtiments Analysés",
            value=f"{len(filtered_df):,}",
            delta=f"{len(filtered_df) / len(df) * 100:.1f}% du total"
        )

    with col2:
        critical_count = len(filtered_df[filtered_df['priority_level'] == 'Critical'])
        st.metric(
            label="Priorité Critique",
            value=f"{critical_count}",
            delta="Action urgente",
            delta_color="inverse"
        )

    with col3:
        total_ges = filtered_df['estimated_ges_reduction_potential'].sum()
        st.metric(
            label="Potentiel GES",
            value=f"{total_ges:.0f} t",
            delta="CO₂/an réductible"
        )

    with col4:
        avg_score = filtered_df['priority_score'].mean()
        st.metric(
            label="Score Moyen",
            value=f"{avg_score:.1f}/100",
            delta=f"±{filtered_df['priority_score'].std():.1f}"
        )

    # Graphiques principaux
    st.markdown("### Visualisations")

    tab1, tab2, tab3, tab4 = st.tabs(["Vue d'ensemble", "Par Arrondissement", "Analyse Detaillee", "Liste Complete"])

    with tab1:
        col1, col2 = st.columns(2)

        with col1:
            # Distribution des priorités
            priority_counts = filtered_df['priority_level'].value_counts()
            fig_priority = px.pie(
                values=priority_counts.values,
                names=priority_counts.index,
                title="Distribution des Niveaux de Priorité",
                color=priority_counts.index,
                color_discrete_map={
                    'Critical': '#ff4444',
                    'High': '#ff8c00',
                    'Medium': '#ffd700',
                    'Low': '#90ee90'
                }
            )
            fig_priority.update_traces(textposition='inside', textinfo='percent+label')
            fig_priority.update_layout(height=400)
            st.plotly_chart(fig_priority, use_container_width=True)

        with col2:
            # Top 10 bâtiments par score
            top_10 = filtered_df.nlargest(10, 'priority_score')[['buildingName', 'priority_score']].copy()
            top_10['buildingName'] = top_10['buildingName'].str[:30]  # Truncate names

            fig_top10 = px.bar(
                top_10,
                x='priority_score',
                y='buildingName',
                orientation='h',
                title="Top 10 Bâtiments Prioritaires",
                labels={'priority_score': 'Score de Priorité', 'buildingName': 'Bâtiment'},
                color='priority_score',
                color_continuous_scale='Reds'
            )
            fig_top10.update_layout(height=400, showlegend=False)
            st.plotly_chart(fig_top10, use_container_width=True)

        # Scatter plot multi-dimensionnel
        st.markdown("####  Analyse Multi-Critères")

        fig_scatter = px.scatter(
            filtered_df,
            x='score_energy_risk',
            y='score_climate_risk',
            size='estimated_ges_reduction_potential',
            color='priority_level',
            hover_data=['buildingName', 'boroughName', 'priority_score'],
            title="Risque Énergétique vs Risque Climatique (taille = potentiel GES)",
            labels={
                'score_energy_risk': 'Risque Énergétique',
                'score_climate_risk': 'Risque Climatique',
                'priority_level': 'Priorité'
            },
            color_discrete_map={
                'Critical': '#ff4444',
                'High': '#ff8c00',
                'Medium': '#ffd700',
                'Low': '#90ee90'
            }
        )
        fig_scatter.update_layout(height=500)
        st.plotly_chart(fig_scatter, use_container_width=True)

    with tab2:
        # Analyse par arrondissement
        st.markdown("#### ️ Statistiques par Arrondissement")

        borough_stats = filtered_df.groupby('boroughName').agg({
            'priority_score': 'mean',
            'buildingid': 'count',
            'estimated_ges_reduction_potential': 'sum',
            'score_social_vulnerability': 'mean'
        }).round(2)

        borough_stats.columns = ['Score Moyen', 'Nombre de Bâtiments', 'Potentiel GES Total', 'Vulnérabilité Sociale']
        borough_stats = borough_stats.sort_values('Score Moyen', ascending=False)

        # Graphique des arrondissements
        fig_borough = go.Figure()

        fig_borough.add_trace(go.Bar(
            x=borough_stats.index,
            y=borough_stats['Score Moyen'],
            name='Score de Priorité Moyen',
            marker_color='lightblue',
            yaxis='y'
        ))

        fig_borough.add_trace(go.Scatter(
            x=borough_stats.index,
            y=borough_stats['Vulnérabilité Sociale'] * 100,  # Scale to match
            name='Vulnérabilité Sociale (x100)',
            marker_color='red',
            yaxis='y2',
            mode='lines+markers'
        ))

        fig_borough.update_layout(
            title='Priorité et Vulnérabilité par Arrondissement',
            xaxis_title='Arrondissement',
            yaxis_title='Score de Priorité',
            yaxis2=dict(
                title='Vulnérabilité Sociale',
                overlaying='y',
                side='right'
            ),
            height=500,
            hovermode='x unified'
        )

        st.plotly_chart(fig_borough, use_container_width=True)

        # Tableau des stats
        st.dataframe(borough_stats, use_container_width=True)

    with tab3:
        # Analyses detaillees
        st.markdown("#### Analyses Approfondies")

        col1, col2, col3 = st.columns(3)

        with col1:
            # Distribution des scores d'énergie
            fig_energy = px.histogram(
                filtered_df,
                x='score_energy_risk',
                nbins=20,
                title="Distribution: Risque Énergétique",
                labels={'score_energy_risk': 'Score Risque Énergétique'},
                color_discrete_sequence=['#1f77b4']
            )
            fig_energy.update_layout(height=300)
            st.plotly_chart(fig_energy, use_container_width=True)

        with col2:
            # Distribution des scores climatiques
            fig_climate = px.histogram(
                filtered_df,
                x='score_climate_risk',
                nbins=20,
                title="Distribution: Risque Climatique",
                labels={'score_climate_risk': 'Score Risque Climatique'},
                color_discrete_sequence=['#ff7f0e']
            )
            fig_climate.update_layout(height=300)
            st.plotly_chart(fig_climate, use_container_width=True)

        with col3:
            # Distribution vulnérabilité sociale
            fig_social = px.histogram(
                filtered_df,
                x='score_social_vulnerability',
                nbins=20,
                title="Distribution: Vulnérabilité Sociale",
                labels={'score_social_vulnerability': 'Score Vulnérabilité'},
                color_discrete_sequence=['#d62728']
            )
            fig_social.update_layout(height=300)
            st.plotly_chart(fig_social, use_container_width=True)

        # Analyse par âge de bâtiment
        st.markdown("#### ️ Analyse par Âge des Bâtiments")

        # Create age bins
        filtered_df_copy = filtered_df.copy()
        current_year = 2024
        filtered_df_copy['building_age'] = current_year - filtered_df_copy['buildingConstrYear']
        filtered_df_copy['age_category'] = pd.cut(
            filtered_df_copy['building_age'],
            bins=[0, 20, 40, 60, 100, 200],
            labels=['< 20 ans', '20-40 ans', '40-60 ans', '60-100 ans', '> 100 ans']
        )

        age_analysis = filtered_df_copy.groupby('age_category').agg({
            'priority_score': 'mean',
            'buildingid': 'count',
            'estimated_ges_reduction_potential': 'mean'
        }).round(2)

        fig_age = px.bar(
            age_analysis,
            x=age_analysis.index,
            y='priority_score',
            title="Score de Priorité Moyen par Âge de Bâtiment",
            labels={'priority_score': 'Score Moyen', 'age_category': 'Catégorie d\'Âge'},
            color='priority_score',
            color_continuous_scale='Reds'
        )
        fig_age.update_layout(height=400)
        st.plotly_chart(fig_age, use_container_width=True)

        # Matrice de corrélation
        st.markdown("####  Corrélations entre Facteurs (Pour Experts)")

        corr_cols = ['score_energy_risk', 'score_climate_risk', 'score_social_vulnerability',
                     'score_age_risk', 'score_size_impact', 'priority_score']

        corr_matrix = filtered_df[corr_cols].corr()

        fig_corr = px.imshow(
            corr_matrix,
            labels=dict(color="Corrélation"),
            x=corr_matrix.columns,
            y=corr_matrix.columns,
            color_continuous_scale='RdBu',
            aspect='auto',
            title="Matrice de Corrélation des Facteurs de Risque"
        )
        fig_corr.update_layout(height=500)
        st.plotly_chart(fig_corr, use_container_width=True)

    with tab4:
        # Liste complète
        st.markdown("####  Liste Complète des Bâtiments Priorisés")

        # Options d'affichage
        show_all_cols = st.checkbox("Afficher toutes les colonnes (mode expert)", value=False)

        if show_all_cols:
            display_df = filtered_df
        else:
            # Colonnes simplifiées pour utilisateurs non-techniques
            simple_cols = [
                'buildingName', 'address', 'boroughName',
                'priority_score', 'priority_level',
                'score_energy_risk', 'score_climate_risk', 'score_social_vulnerability',
                'estimated_ges_reduction_potential',
                'recommendations'
            ]
            display_df = filtered_df[simple_cols]

        # Renommer les colonnes pour plus de clarté
        display_df = display_df.copy()
        display_df.columns = [
            col.replace('score_', '').replace('_', ' ').title()
            for col in display_df.columns
        ]

        # Colorier les lignes selon la priorité
        def highlight_priority(row):
            if 'Priority Level' in row.index:
                priority = row['Priority Level']
                if priority == 'Critical':
                    return ['background-color: #ffe6e6'] * len(row)
                elif priority == 'High':
                    return ['background-color: #fff4e6'] * len(row)
                elif priority == 'Medium':
                    return ['background-color: #fffee6'] * len(row)
            return [''] * len(row)

        # Afficher avec styling
        st.dataframe(
            display_df.style.apply(highlight_priority, axis=1),
            use_container_width=True,
            height=600
        )

        # Bouton de téléchargement
        csv = filtered_df.to_csv(index=False, encoding='utf-8-sig')
        st.download_button(
            label=" Télécharger les résultats (CSV)",
            data=csv,
            file_name='batiments_priorises.csv',
            mime='text/csv'
        )

    # Section recommandations
    st.markdown("---")
    st.markdown("###  Recommandations d'Action")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="info-box">
        <h4> Actions Prioritaires</h4>
        <ul>
            <li>Commencer par les bâtiments en priorité <strong>Critique</strong></li>
            <li>Prioriser les arrondissements à haute vulnérabilité sociale</li>
            <li>Cibler les bâtiments avec le plus grand potentiel de réduction GES</li>
            <li>Planifier des audits énergétiques pour les bâtiments > 60 ans</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-box">
        <h4> Prochaines Étapes</h4>
        <ul>
            <li>Effectuer des audits énergétiques détaillés</li>
            <li>Consulter les résidents des zones à haute vulnérabilité</li>
            <li>Budgétiser les interventions selon les priorités</li>
            <li>Suivre l'impact des rénovations sur les émissions</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
    <p><strong>Projet VILLE_IA</strong> - Institut de la résilience et de l'innovation urbaine (IRIU)</p>
    <p>Méthodologie sans géomatique - Approche par intelligence textuelle et machine learning</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
