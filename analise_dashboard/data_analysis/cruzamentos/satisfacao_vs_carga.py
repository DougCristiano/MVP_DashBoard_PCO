"""
Exemplo de cruzamento: Satisfação vs Carga de Trabalho
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from scipy import stats


def _convert_workload_to_numeric(workload_series, tipo='diretoria'):
    """Converte dados categóricos de workload para numéricos"""
    mapping = {}
    
    if tipo == 'diretoria':
        mapping = {
            '1 a 5 horas': 3,
            '6 a 10 horas': 8,
            '11 a 15 horas': 13,
            'Mais de 15 horas': 18
        }
    elif tipo == 'projeto':
        mapping = {
            '1 a 5 horas': 3,
            '6 a 10 horas': 8,
            '11 a 15 horas': 13,
            'Mais de 10 horas': 15,
            'Mais de 15 horas': 18
        }
    elif tipo == 'projetos':
        mapping = {
            'Nenhum': 0,
            'Um': 1,
            'Dois': 2,
            'Três': 3,
            'Mais de três': 4
        }
    
    return workload_series.map(mapping)


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
                
                # Converter dados categóricos para numéricos quando possível
                satisfaction_numeric = pd.to_numeric(data_dir[satisfaction_col], errors='coerce')
                workload_numeric = _convert_workload_to_numeric(data_dir[workload_dir_col], 'diretoria')
                
                # Remover valores que não puderam ser convertidos
                valid_data = pd.DataFrame({
                    'satisfaction': satisfaction_numeric,
                    'workload': workload_numeric
                }).dropna()
                
                if len(valid_data) > 5:
                    correlation_dir, p_value_dir = stats.pearsonr(
                        valid_data['satisfaction'], 
                        valid_data['workload']
                    )
                    
                    results['satisfacao_vs_diretoria'] = {
                        'correlacao': round(correlation_dir, 3),
                        'p_value': round(p_value_dir, 3),
                        'significativo': p_value_dir < 0.05,
                        'data': data_dir,  # Dados originais para visualização
                        'data_numerica': valid_data,  # Dados numéricos para correlação
                        'n_amostras': len(valid_data)
                    }
                else:
                    # Se não conseguir converter para numérico, fazer análise categórica
                    results['satisfacao_vs_diretoria'] = {
                        'tipo_analise': 'categorica',
                        'crosstab': pd.crosstab(data_dir[satisfaction_col], data_dir[workload_dir_col]),
                        'data': data_dir,
                        'n_amostras': len(data_dir)
                    }
        
        # Análise Satisfação vs Horas Projeto
        if workload_proj_col in df.columns:
            data_proj = df[[satisfaction_col, workload_proj_col]].dropna()
            if len(data_proj) > 5:
                
                # Converter dados categóricos para numéricos quando possível
                satisfaction_numeric = pd.to_numeric(data_proj[satisfaction_col], errors='coerce')
                workload_numeric = _convert_workload_to_numeric(data_proj[workload_proj_col], 'projeto')
                
                # Remover valores que não puderam ser convertidos
                valid_data = pd.DataFrame({
                    'satisfaction': satisfaction_numeric,
                    'workload': workload_numeric
                }).dropna()
                
                if len(valid_data) > 5:
                    correlation_proj, p_value_proj = stats.pearsonr(
                        valid_data['satisfaction'], 
                        valid_data['workload']
                    )
                    
                    results['satisfacao_vs_projeto'] = {
                        'correlacao': round(correlation_proj, 3),
                        'p_value': round(p_value_proj, 3),
                        'significativo': p_value_proj < 0.05,
                        'data': data_proj,  # Dados originais para visualização
                        'data_numerica': valid_data,  # Dados numéricos para correlação
                        'n_amostras': len(valid_data)
                    }
                else:
                    # Se não conseguir converter para numérico, fazer análise categórica
                    results['satisfacao_vs_projeto'] = {
                        'tipo_analise': 'categorica',
                        'crosstab': pd.crosstab(data_proj[satisfaction_col], data_proj[workload_proj_col]),
                        'data': data_proj,
                        'n_amostras': len(data_proj)
                    }
        
        # Análise combinada (carga total)
        if workload_dir_col in df.columns and workload_proj_col in df.columns:
            data_combined = df[[satisfaction_col, workload_dir_col, workload_proj_col]].dropna()
            if len(data_combined) > 5:
                
                # Converter dados categóricos para numéricos quando possível
                satisfaction_numeric = pd.to_numeric(data_combined[satisfaction_col], errors='coerce')
                workload_dir_numeric = _convert_workload_to_numeric(data_combined[workload_dir_col], 'diretoria')
                workload_proj_numeric = _convert_workload_to_numeric(data_combined[workload_proj_col], 'projeto')
                
                # Criar carga total apenas se ambos forem numéricos
                valid_data = pd.DataFrame({
                    'satisfaction': satisfaction_numeric,
                    'workload_dir': workload_dir_numeric,
                    'workload_proj': workload_proj_numeric
                }).dropna()
                
                if len(valid_data) > 5:
                    # Criar carga total
                    valid_data['carga_total'] = valid_data['workload_dir'] + valid_data['workload_proj']
                    
                    correlation_total, p_value_total = stats.pearsonr(
                        valid_data['satisfaction'], 
                        valid_data['carga_total']
                    )
                    
                    results['satisfacao_vs_carga_total'] = {
                        'correlacao': round(correlation_total, 3),
                        'p_value': round(p_value_total, 3),
                        'significativo': p_value_total < 0.05,
                        'data': data_combined,  # Dados originais
                        'data_numerica': valid_data,  # Dados numéricos
                        'n_amostras': len(valid_data)
                    }
                else:
                    # Se não conseguir converter, fazer análise categórica básica
                    results['satisfacao_vs_carga_total'] = {
                        'tipo_analise': 'categorica_combinada',
                        'data': data_combined,
                        'n_amostras': len(data_combined),
                        'nota': 'Análise categórica - sem conversão numérica possível'
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
            resultado = results['satisfacao_vs_diretoria']
            corr = resultado['correlacao']
            sig = resultado['significativo']
            
            # Usar dados numéricos se disponíveis, senão fazer gráfico categórico
            if 'data_numerica' in resultado:
                data_num = resultado['data_numerica']
                fig = px.scatter(
                    data_num,
                    x='workload',
                    y='satisfaction',
                    title=f"Satisfação vs Horas Diretoria<br>Correlação: {corr} {'*' if sig else ''}",
                    labels={
                        'workload': 'Horas Diretoria/Semana (mapeamento numérico)',
                        'satisfaction': 'Satisfação Geral'
                    }
                )
                fig.update_traces(marker_size=8)
            else:
                # Análise categórica - criar gráfico de barras agrupadas
                data = resultado['data']
                crosstab = pd.crosstab(data['O quão satisfeito(a) você está com a IN Junior?'], 
                                     data['Quantas horas por semana você gasta com tarefas de diretoria?'])
                fig = px.bar(
                    x=crosstab.columns,
                    y=crosstab.loc[crosstab.index[0]] if len(crosstab.index) > 0 else [],
                    title="Satisfação vs Horas Diretoria (Análise Categórica)",
                    labels={'x': 'Horas Diretoria/Semana', 'y': 'Quantidade de Respostas'}
                )
            st.plotly_chart(fig, width="stretch")
    
    # Gráfico: Satisfação vs Horas Projeto
    if 'satisfacao_vs_projeto' in results:
        with col2:
            resultado = results['satisfacao_vs_projeto']
            corr = resultado['correlacao']
            sig = resultado['significativo']
            
            # Usar dados numéricos se disponíveis, senão fazer gráfico categórico
            if 'data_numerica' in resultado:
                data_num = resultado['data_numerica']
                fig = px.scatter(
                    data_num,
                    x='workload',
                    y='satisfaction',
                    title=f"Satisfação vs Horas Projeto<br>Correlação: {corr} {'*' if sig else ''}",
                    labels={
                        'workload': 'Horas Projeto/Semana (mapeamento numérico)',
                        'satisfaction': 'Satisfação Geral'
                    }
                )
                fig.update_traces(marker_size=8, marker_color='orange')
            else:
                # Análise categórica - criar gráfico de barras agrupadas
                data = resultado['data']
                crosstab = pd.crosstab(data['O quão satisfeito(a) você está com a IN Junior?'], 
                                     data['Quantas horas semanalmente você gasta com tarefas de projeto?'])
                fig = px.bar(
                    x=crosstab.columns,
                    y=crosstab.loc[crosstab.index[0]] if len(crosstab.index) > 0 else [],
                    title="Satisfação vs Horas Projeto (Análise Categórica)",
                    labels={'x': 'Horas Projeto/Semana', 'y': 'Quantidade de Respostas'}
                )
            st.plotly_chart(fig, width="stretch")
    
    # Gráfico: Satisfação vs Carga Total
    if 'satisfacao_vs_carga_total' in results:
        resultado = results['satisfacao_vs_carga_total']
        corr = resultado['correlacao']
        sig = resultado['significativo']
        
        # Usar dados numéricos se disponíveis
        if 'data_numerica' in resultado:
            data_num = resultado['data_numerica']
            fig = px.scatter(
                data_num,
                x='carga_total',
                y='satisfaction',
                title=f"Satisfação vs Carga Total de Trabalho<br>Correlação: {corr} {'*' if sig else ''}",
                labels={
                    'carga_total': 'Carga Total (Horas/Semana)',
                    'satisfaction': 'Satisfação Geral'
                }
            )
            fig.update_traces(marker_size=8, marker_color='red')
        else:
            # Fallback para dados originais se necessário
            data = resultado['data']
            fig = px.histogram(
                data,
                x='carga_total',
                title="Distribuição da Carga Total de Trabalho",
                labels={'carga_total': 'Carga Total (Horas/Semana)'}
            )
        st.plotly_chart(fig, width="stretch")
    
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
        st.dataframe(summary_df, width="stretch")
        
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
