"""
Exemplo de cruzamento: Satisfação vs Carga de Trabalho
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from scipy import stats


def analyze_satisfaction_vs_workload(analyzer):
    """
    Analisa a correlação entre satisfação geral e carga de trabalho
    
    Args:
        analyzer: Instância do INJuniorSurveyAnalyzer
        
    Returns:
        dict: Resultados da análise de cruzamento
    """
    df = analyzer.df_processed
    
    # Colunas de interesse
    satisfaction_col = 'O quão satisfeito(a) você está com a IN Junior?'
    workload_dir_col = 'Quantas horas por semana você gasta com tarefas de diretoria?'
    workload_proj_col = 'Quantas horas semanalmente você gasta com tarefas de projeto?'
    
    results = {}
    
    # Verificar se as colunas existem
    if satisfaction_col in df.columns:
        # Análise Satisfação vs Horas Diretoria
        if workload_dir_col in df.columns:
            data_dir = df[[satisfaction_col, workload_dir_col]].dropna()
            if len(data_dir) > 5:  # Mínimo de dados para análise
                correlation_dir, p_value_dir = stats.pearsonr(
                    data_dir[satisfaction_col], 
                    data_dir[workload_dir_col]
                )
                
                results['satisfacao_vs_diretoria'] = {
                    'correlacao': round(correlation_dir, 3),
                    'p_value': round(p_value_dir, 3),
                    'significativo': p_value_dir < 0.05,
                    'data': data_dir,
                    'n_amostras': len(data_dir)
                }
        
        # Análise Satisfação vs Horas Projeto
        if workload_proj_col in df.columns:
            data_proj = df[[satisfaction_col, workload_proj_col]].dropna()
            if len(data_proj) > 5:
                correlation_proj, p_value_proj = stats.pearsonr(
                    data_proj[satisfaction_col], 
                    data_proj[workload_proj_col]
                )
                
                results['satisfacao_vs_projeto'] = {
                    'correlacao': round(correlation_proj, 3),
                    'p_value': round(p_value_proj, 3),
                    'significativo': p_value_proj < 0.05,
                    'data': data_proj,
                    'n_amostras': len(data_proj)
                }
        
        # Análise combinada (carga total)
        if workload_dir_col in df.columns and workload_proj_col in df.columns:
            data_combined = df[[satisfaction_col, workload_dir_col, workload_proj_col]].dropna()
            if len(data_combined) > 5:
                # Cria coluna de carga total
                data_combined = data_combined.copy()
                data_combined['carga_total'] = data_combined[workload_dir_col] + data_combined[workload_proj_col]
                
                correlation_total, p_value_total = stats.pearsonr(
                    data_combined[satisfaction_col], 
                    data_combined['carga_total']
                )
                
                results['satisfacao_vs_carga_total'] = {
                    'correlacao': round(correlation_total, 3),
                    'p_value': round(p_value_total, 3),
                    'significativo': p_value_total < 0.05,
                    'data': data_combined,
                    'n_amostras': len(data_combined)
                }
    
    return results


def create_satisfaction_workload_charts(analyzer):
    """Cria gráficos do cruzamento satisfação vs carga de trabalho"""
    
    st.subheader("🔄 Cruzamento: Satisfação vs Carga de Trabalho")
    
    # Realiza a análise
    results = analyze_satisfaction_vs_workload(analyzer)
    
    if not results:
        st.warning("Dados insuficientes para análise de correlação.")
        return
    
    # Layout com 2 colunas
    col1, col2 = st.columns(2)
    
    # Gráfico: Satisfação vs Horas Diretoria
    if 'satisfacao_vs_diretoria' in results:
        with col1:
            data = results['satisfacao_vs_diretoria']['data']
            corr = results['satisfacao_vs_diretoria']['correlacao']
            sig = results['satisfacao_vs_diretoria']['significativo']
            
            fig = px.scatter(
                data,
                x='Quantas horas por semana você gasta com tarefas de diretoria?',
                y='O quão satisfeito(a) você está com a IN Junior?',
                title=f"Satisfação vs Horas Diretoria<br>Correlação: {corr} {'*' if sig else ''}",
                labels={
                    'Quantas horas por semana você gasta com tarefas de diretoria?': 'Horas Diretoria/Semana',
                    'O quão satisfeito(a) você está com a IN Junior?': 'Satisfação Geral'
                },
                trendline="ols"
            )
            fig.update_traces(marker_size=8)
            st.plotly_chart(fig, use_container_width=True)
    
    # Gráfico: Satisfação vs Horas Projeto
    if 'satisfacao_vs_projeto' in results:
        with col2:
            data = results['satisfacao_vs_projeto']['data']
            corr = results['satisfacao_vs_projeto']['correlacao']
            sig = results['satisfacao_vs_projeto']['significativo']
            
            fig = px.scatter(
                data,
                x='Quantas horas semanalmente você gasta com tarefas de projeto?',
                y='O quão satisfeito(a) você está com a IN Junior?',
                title=f"Satisfação vs Horas Projeto<br>Correlação: {corr} {'*' if sig else ''}",
                labels={
                    'Quantas horas semanalmente você gasta com tarefas de projeto?': 'Horas Projeto/Semana',
                    'O quão satisfeito(a) você está com a IN Junior?': 'Satisfação Geral'
                },
                trendline="ols"
            )
            fig.update_traces(marker_size=8, marker_color='orange')
            st.plotly_chart(fig, use_container_width=True)
    
    # Gráfico: Satisfação vs Carga Total
    if 'satisfacao_vs_carga_total' in results:
        data = results['satisfacao_vs_carga_total']['data']
        corr = results['satisfacao_vs_carga_total']['correlacao']
        sig = results['satisfacao_vs_carga_total']['significativo']
        
        fig = px.scatter(
            data,
            x='carga_total',
            y='O quão satisfeito(a) você está com a IN Junior?',
            title=f"Satisfação vs Carga Total de Trabalho<br>Correlação: {corr} {'*' if sig else ''}",
            labels={
                'carga_total': 'Carga Total (Horas/Semana)',
                'O quão satisfeito(a) você está com a IN Junior?': 'Satisfação Geral'
            },
            trendline="ols"
        )
        fig.update_traces(marker_size=8, marker_color='red')
        st.plotly_chart(fig, use_container_width=True)
    
    # Resumo estatístico
    st.subheader("📈 Resumo Estatístico")
    
    summary_data = []
    for analysis_name, analysis_data in results.items():
        summary_data.append({
            'Análise': analysis_name.replace('_', ' ').title(),
            'Correlação': analysis_data['correlacao'],
            'P-valor': analysis_data['p_value'],
            'Significativo (p<0.05)': '✅' if analysis_data['significativo'] else '❌',
            'N° Amostras': analysis_data['n_amostras']
        })
    
    if summary_data:
        summary_df = pd.DataFrame(summary_data)
        st.dataframe(summary_df, use_container_width=True)
        
        # Interpretação
        st.subheader("🎯 Interpretação")
        
        with st.expander("Como interpretar os resultados"):
            st.markdown("""
            **Correlação:**
            - **-1 a -0.7**: Correlação negativa forte
            - **-0.7 a -0.3**: Correlação negativa moderada  
            - **-0.3 a 0.3**: Correlação fraca ou inexistente
            - **0.3 a 0.7**: Correlação positiva moderada
            - **0.7 a 1**: Correlação positiva forte
            
            **Significância estatística:**
            - ✅ p < 0.05: A correlação é estatisticamente significativa
            - ❌ p ≥ 0.05: A correlação pode ser devido ao acaso
            
            **(*) indica correlação estatisticamente significativa**
            """)


def get_correlation_insights(results):
    """
    Gera insights baseados nos resultados da correlação
    
    Args:
        results: Resultados da análise de correlação
        
    Returns:
        list: Lista de insights textuais
    """
    insights = []
    
    for analysis_name, data in results.items():
        corr = data['correlacao']
        sig = data['significativo']
        
        if sig:  # Apenas para correlações significativas
            if abs(corr) >= 0.7:
                strength = "forte"
            elif abs(corr) >= 0.3:
                strength = "moderada"
            else:
                strength = "fraca"
            
            direction = "positiva" if corr > 0 else "negativa"
            
            analysis_readable = analysis_name.replace('_', ' ').replace('satisfacao vs ', '')
            
            insight = f"📊 **{analysis_readable.title()}**: Correlação {direction} {strength} ({corr})"
            insights.append(insight)
    
    return insights
