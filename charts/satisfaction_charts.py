"""
Gráficos de satisfação
"""

import streamlit as st
import plotly.express as px


def create_satisfaction_charts(analyzer):
    """Cria gráficos de satisfação usando Plotly"""
    satisfaction_data = analyzer.calculate_satisfaction_metrics()
    
    if 'satisfacao_geral' in satisfaction_data:
        data = satisfaction_data['satisfacao_geral']['data']
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Histograma
            fig_hist = px.histogram(
                x=data, 
                nbins=5,
                title="Distribuição da Satisfação Geral",
                labels={'x': 'Nível de Satisfação', 'count': 'Frequência'},
                color_discrete_sequence=['#1f77b4']
            )
            fig_hist.update_layout(showlegend=False)
            st.plotly_chart(fig_hist, use_container_width=True)
        
        with col2:
            # Box plot
            fig_box = px.box(
                y=data,
                title="Box Plot - Satisfação Geral",
                labels={'y': 'Nível de Satisfação'}
            )
            fig_box.update_traces(marker_color='#ff7f0e')
            st.plotly_chart(fig_box, use_container_width=True)
