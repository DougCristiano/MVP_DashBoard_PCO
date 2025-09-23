"""
Gráficos da estrutura organizacional
"""

import streamlit as st
import plotly.express as px


def create_organizational_charts(analyzer):
    """Cria gráficos da estrutura organizacional"""
    org_data = analyzer.analyze_organizational_structure()
    
    if org_data:
        # Gráfico de barras com as médias
        metrics_names = []
        metrics_values = []
        
        name_mapping = {
            'organizacao_de': 'Organização DE',
            'acessibilidade_diretor': 'Acessibilidade Diretor',
            'comunicacao_interna': 'Comunicação Interna'
        }
        
        for key, data in org_data.items():
            metrics_names.append(name_mapping.get(key, key))
            metrics_values.append(data['media'])
        
        if metrics_names:
            fig = px.bar(
                x=metrics_names,
                y=metrics_values,
                title="Avaliação da Estrutura Organizacional (Médias)",
                labels={'x': 'Aspecto', 'y': 'Média (1-5)'},
                color=metrics_values,
                color_continuous_scale='viridis'
            )
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig, width="stretch")
