"""
Funções utilitárias para o dashboard
"""

import streamlit as st
import pandas as pd
import numpy as np


def display_metrics_cards(report):
    """Exibe cards com métricas principais"""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="📊 Total de Respostas",
            value=report['info_geral']['total_respostas']
        )
    
    with col2:
        if 'satisfacao_geral' in report['satisfacao']:
            satisfaction = report['satisfacao']['satisfacao_geral']
            st.metric(
                label="😊 Satisfação Média",
                value=f"{satisfaction['media']}/5",
                delta=f"±{satisfaction['desvio_padrao']}"
            )
    
    with col3:
        if 'horas_semanais_diretoria' in report['carga_trabalho']:
            hours = report['carga_trabalho']['horas_semanais_diretoria']
            st.metric(
                label="⏰ Horas Diretoria/Semana",
                value=f"{hours['media']}h",
                delta=f"Max: {hours['maximo']}h"
            )
    
    with col4:
        if 'horas_semanais_projeto' in report['carga_trabalho']:
            hours = report['carga_trabalho']['horas_semanais_projeto']
            st.metric(
                label="🚀 Horas Projeto/Semana",
                value=f"{hours['media']}h",
                delta=f"Max: {hours['maximo']}h"
            )
