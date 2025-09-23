"""
Gráficos da cultura de feedback
"""

import streamlit as st
import plotly.express as px


def create_feedback_charts(analyzer):
    """Cria gráficos da cultura de feedback"""
    feedback_data = analyzer.analyze_feedback_culture()
    
    if feedback_data:
        metrics_names = []
        metrics_values = []
        
        name_mapping = {
            'preparacao_feedback': 'Preparação p/ Feedback',
            'frequencia_feedback_dado': 'Frequência Feedback Dado',
            'frequencia_feedback_recebido': 'Frequência Feedback Recebido'
        }
        
        for key, data in feedback_data.items():
            metrics_names.append(name_mapping.get(key, key))
            metrics_values.append(data['media'])
        
        if metrics_names:
            fig = px.bar(
                x=metrics_names,
                y=metrics_values,
                title="Cultura de Feedback (Médias)",
                labels={'x': 'Aspecto', 'y': 'Média (1-5)'},
                color=metrics_values,
                color_continuous_scale='plasma'
            )
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig, width="stretch")
