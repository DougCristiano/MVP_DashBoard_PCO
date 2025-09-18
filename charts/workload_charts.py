"""
Gráficos de carga de trabalho
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


def create_workload_charts(analyzer):
    """Cria gráficos de carga de trabalho usando Plotly"""
    workload_data = analyzer.analyze_workload_distribution()
    
    if workload_data:
        col1, col2 = st.columns(2)
        
        # Histogramas de horas
        if 'horas_semanais_diretoria' in workload_data:
            with col1:
                data = workload_data['horas_semanais_diretoria']['data']
                fig_dir = px.histogram(
                    x=data,
                    title="Distribuição - Horas Diretoria/Semana",
                    labels={'x': 'Horas', 'count': 'Frequência'},
                    color_discrete_sequence=['#2ca02c']
                )
                st.plotly_chart(fig_dir, use_container_width=True)
        
        if 'horas_semanais_projeto' in workload_data:
            with col2:
                data = workload_data['horas_semanais_projeto']['data']
                fig_proj = px.histogram(
                    x=data,
                    title="Distribuição - Horas Projeto/Semana",
                    labels={'x': 'Horas', 'count': 'Frequência'},
                    color_discrete_sequence=['#d62728']
                )
                st.plotly_chart(fig_proj, use_container_width=True)
        
        # Box plot comparativo
        if 'horas_semanais_diretoria' in workload_data and 'horas_semanais_projeto' in workload_data:
            dir_data = workload_data['horas_semanais_diretoria']['data']
            proj_data = workload_data['horas_semanais_projeto']['data']
            
            fig_compare = go.Figure()
            fig_compare.add_trace(go.Box(y=dir_data, name='Diretoria', marker_color='#2ca02c'))
            fig_compare.add_trace(go.Box(y=proj_data, name='Projeto', marker_color='#d62728'))
            fig_compare.update_layout(
                title="Comparação de Carga de Trabalho",
                yaxis_title="Horas/Semana"
            )
            st.plotly_chart(fig_compare, use_container_width=True)
