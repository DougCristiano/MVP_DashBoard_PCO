"""
Gráficos de carga de trabalho
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


def create_workload_charts(analyzer):
    """Cria gráficos de carga de trabalho usando dados categóricos"""
    try:
        workload_data = analyzer.analyze_workload_distribution()
        
        # Debug: Verificar se há dados
        if not workload_data:
            st.warning("⚠️ Não foram encontrados dados de carga de trabalho.")
            st.info("📋 **Colunas que o sistema procura:**")
            st.write("• Horas de diretoria: 'Quantas horas por semana você gasta com tarefas de diretoria?'")
            st.write("• Horas de projeto: 'Quantas horas semanalmente você gasta com tarefas de projeto?'")
            st.write("• Número de projetos: 'Quantos projetos você está realizando na IN Junior atualmente?'")
            
            # Mostrar colunas disponíveis
            st.info("📊 **Colunas disponíveis no seu CSV:**")
            cols_with_hora = [col for col in analyzer.df_processed.columns if 'hora' in col.lower()]
            cols_with_projeto = [col for col in analyzer.df_processed.columns if 'projeto' in col.lower()]
            
            if cols_with_hora:
                st.write("🕐 Colunas relacionadas a horas:", cols_with_hora)
            if cols_with_projeto:
                st.write("📁 Colunas relacionadas a projetos:", cols_with_projeto)
            
            if not cols_with_hora and not cols_with_projeto:
                st.write("❌ Nenhuma coluna relacionada a horas ou projetos foi encontrada")
            
            return
        
        # Primeira linha: Gráficos de barras categóricos
        col1, col2 = st.columns(2)
        
        # Gráfico de horas de diretoria
        if 'horas_semanais_diretoria' in workload_data:
            with col1:
                try:
                    data = workload_data['horas_semanais_diretoria']
                    value_counts = data['value_counts']
                    
                    if len(value_counts) > 0:
                        fig_dir = px.bar(
                            x=value_counts.index,
                            y=value_counts.values,
                            title="Distribuição - Horas Diretoria/Semana",
                            labels={'x': 'Faixa de Horas', 'y': 'Quantidade de Respostas'},
                            color=value_counts.values,
                            color_continuous_scale='greens'
                        )
                        fig_dir.update_layout(showlegend=False)
                        st.plotly_chart(fig_dir, width="stretch")
                        
                        # Mostra estatísticas se disponíveis
                        if 'media' in data:
                            st.info(f"📊 **Estatísticas:** Média: {data['media']}h | Respostas: {data['n_respostas']}")
                    else:
                        st.warning("Não há dados válidos para horas de diretoria")
                except Exception as e:
                    st.error(f"Erro no gráfico de diretoria: {str(e)}")
        else:
            with col1:
                st.warning("Dados de 'horas_semanais_diretoria' não encontrados")
        
        # Gráfico de horas de projeto
        if 'horas_semanais_projeto' in workload_data:
            with col2:
                try:
                    data = workload_data['horas_semanais_projeto']
                    value_counts = data['value_counts']
                    
                    if len(value_counts) > 0:
                        fig_proj = px.bar(
                            x=value_counts.index,
                            y=value_counts.values,
                            title="Distribuição - Horas Projeto/Semana",
                            labels={'x': 'Faixa de Horas', 'y': 'Quantidade de Respostas'},
                            color=value_counts.values,
                            color_continuous_scale='oranges'
                        )
                        fig_proj.update_layout(showlegend=False)
                        st.plotly_chart(fig_proj, width="stretch")
                        
                        # Mostra estatísticas se disponíveis
                        if 'media' in data:
                            st.info(f"📊 **Estatísticas:** Média: {data['media']}h | Respostas: {data['n_respostas']}")
                    else:
                        st.warning("Não há dados válidos para horas de projeto")
                except Exception as e:
                    st.error(f"Erro no gráfico de projeto: {str(e)}")
        else:
            with col2:
                st.warning("Dados de 'horas_semanais_projeto' não encontrados")
        
        # Segunda linha: Gráfico de projetos simultâneos e comparativo
        col3, col4 = st.columns(2)
        
        # Gráfico de projetos simultâneos
        if 'projetos_simultaneos' in workload_data:
            with col3:
                try:
                    data = workload_data['projetos_simultaneos']
                    value_counts = data['value_counts']
                    
                    if len(value_counts) > 0:
                        fig_proj_num = px.pie(
                            values=value_counts.values,
                            names=value_counts.index,
                            title="Distribuição - Número de Projetos",
                            color_discrete_sequence=px.colors.qualitative.Set3
                        )
                        st.plotly_chart(fig_proj_num, width="stretch")
                        
                        if 'media' in data:
                            st.info(f"📊 **Estatísticas:** Média: {data['media']} projetos | Respostas: {data['n_respostas']}")
                    else:
                        st.warning("Não há dados válidos para número de projetos")
                except Exception as e:
                    st.error(f"Erro no gráfico de projetos: {str(e)}")
        else:
            with col3:
                st.warning("Dados de 'projetos_simultaneos' não encontrados")
        
        # Gráfico comparativo (se temos dados numéricos)
        if ('horas_semanais_diretoria' in workload_data and 'horas_semanais_projeto' in workload_data and
            'numeric_data' in workload_data['horas_semanais_diretoria'] and 
            'numeric_data' in workload_data['horas_semanais_projeto']):
            
            with col4:
                try:
                    dir_data = workload_data['horas_semanais_diretoria']['numeric_data']
                    proj_data = workload_data['horas_semanais_projeto']['numeric_data']
                    
                    if len(dir_data) > 0 and len(proj_data) > 0:
                        fig_compare = go.Figure()
                        fig_compare.add_trace(go.Box(y=dir_data, name='Diretoria', marker_color='green'))
                        fig_compare.add_trace(go.Box(y=proj_data, name='Projeto', marker_color='orange'))
                        fig_compare.update_layout(
                            title="Comparação de Carga de Trabalho",
                            yaxis_title="Horas/Semana (estimativa)"
                        )
                        st.plotly_chart(fig_compare, width="stretch")
                    else:
                        st.info("Dados insuficientes para gráfico comparativo")
                except Exception as e:
                    st.error(f"Erro no gráfico comparativo: {str(e)}")
        else:
            with col4:
                st.info("💡 **Gráfico comparativo não disponível**\n\nNecessário dados numéricos mapeáveis")
    
    except Exception as e:
        st.error(f"Erro geral nos gráficos de carga de trabalho: {str(e)}")
        st.write("**Debug - Dados do analyzer:**")
        try:
            st.write("Colunas disponíveis:", list(analyzer.df_processed.columns))
        except:
            st.write("Erro ao acessar dados do analyzer")
