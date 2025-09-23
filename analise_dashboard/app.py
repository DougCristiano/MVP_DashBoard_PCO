import streamlit as st
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Importações dos módulos locais
from data_analysis.survey_analyzer import INJuniorSurveyAnalyzer
from charts.satisfaction_charts import create_satisfaction_charts
from charts.workload_charts import create_workload_charts
from charts.organizational_charts import create_organizational_charts
from charts.feedback_charts import create_feedback_charts
from utils.helpers import display_metrics_cards
from data_analysis.cruzamentos.satisfacao_vs_carga import create_satisfaction_workload_charts

# Configuração da página
st.set_page_config(
    page_title="Dashboard - Análise IN Junior",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Interface principal do Streamlit
def main():
    st.title("📊 Dashboard de Análise - IN Junior")
    st.markdown("---")
    
    # Sidebar para upload do arquivo
    st.sidebar.header("📁 Upload de Dados")
    uploaded_file = st.sidebar.file_uploader(
        "Escolha o arquivo CSV da pesquisa:",
        type=['csv'],
        help="Faça upload do arquivo CSV com os dados da pesquisa de satisfação"
    )
    
    if uploaded_file is not None:
        try:
            # Carrega os dados
            df = pd.read_csv(uploaded_file)
            
            # Inicializa o analisador
            analyzer = INJuniorSurveyAnalyzer(df)
            
            # Gera o relatório
            report = analyzer.generate_summary_report()
            
            # Exibe cards com métricas principais
            st.subheader("📈 Visão Geral")
            display_metrics_cards(report)
            
            # Tabs para diferentes análises
            tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
                "😊 Satisfação",
                "⏰ Carga de Trabalho",
                "🏢 Estrutura Organizacional",
                "💬 Cultura de Feedback",
                "🔄 Cruzamentos",
                "📊 Dados Detalhados"
            ])
            
            with tab1:
                st.subheader("Análise de Satisfação")
                create_satisfaction_charts(analyzer)
                
                if 'satisfacao_geral' in report['satisfacao']:
                    sat = report['satisfacao']['satisfacao_geral']
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.info(f"**Média:** {sat['media']}/5")
                    with col2:
                        st.info(f"**Mediana:** {sat['mediana']}/5")
                    with col3:
                        st.info(f"**Desvio Padrão:** {sat['desvio_padrao']}")
            
            with tab2:
                st.subheader("Análise de Carga de Trabalho")
                create_workload_charts(analyzer)
                
                # Tabela resumo
                if report['carga_trabalho']:
                    st.subheader("Resumo da Carga de Trabalho")
                    workload_summary = []
                    for key, data in report['carga_trabalho'].items():
                        workload_summary.append({
                            'Métrica': key.replace('_', ' ').title(),
                            'Média': data['media'],
                            'Mediana': data['mediana'],
                            'Máximo': data['maximo'],
                            'N° Respostas': data['n_respostas']
                        })
                    
                    if workload_summary:
                        st.dataframe(pd.DataFrame(workload_summary), width="stretch")
            
            with tab3:
                st.subheader("Estrutura Organizacional")
                create_organizational_charts(analyzer)
            
            with tab4:
                st.subheader("Cultura de Feedback")
                create_feedback_charts(analyzer)
            
            with tab5:
                st.subheader("Análises de Cruzamento")
                create_satisfaction_workload_charts(analyzer)
            
            with tab6:
                st.subheader("Dados Detalhados")
                
                # Opções de visualização
                view_option = st.radio(
                    "Escolha o que visualizar:",
                    ["Dados Processados", "Estatísticas Resumidas", "Dados Originais"]
                )
                
                if view_option == "Dados Processados":
                    st.dataframe(analyzer.df_processed, width="stretch")
                
                elif view_option == "Estatísticas Resumidas":
                    try:
                        numeric_cols = analyzer.df_processed.select_dtypes(include=['number']).columns
                        if len(numeric_cols) > 0:
                            st.dataframe(analyzer.df_processed[numeric_cols].describe(), width="stretch")
                        else:
                            st.warning("Nenhuma coluna numérica encontrada para estatísticas.")
                    except Exception as e:
                        st.error(f"Erro ao gerar estatísticas: {str(e)}")
                        st.info("Tentando método alternativo...")
                        try:
                            # Método alternativo
                            numeric_data = analyzer.df_processed._get_numeric_data()
                            if not numeric_data.empty:
                                st.dataframe(numeric_data.describe(), width="stretch")
                            else:
                                st.warning("Nenhuma coluna numérica encontrada.")
                        except:
                            st.warning("Não foi possível gerar estatísticas para este dataset.")
                
                else:  # Dados Originais
                    st.dataframe(df, width="stretch")
                
                # Download dos dados processados
                csv = analyzer.df_processed.to_csv(index=False)
                st.download_button(
                    label="📥 Download dos Dados Processados",
                    data=csv,
                    file_name="dados_processados_in_junior.csv",
                    mime="text/csv"
                )
        
        except Exception as e:
            st.error(f"Erro ao processar o arquivo: {str(e)}")
            st.error(f"Tipo do erro: {type(e).__name__}")
            
            # Debug mais detalhado
            with st.expander("🔍 Informações de Debug"):
                import traceback
                st.code(traceback.format_exc())
            
            st.info("Verifique se o arquivo CSV está no formato correto.")
    
    else:
        st.info("👆 Por favor, faça upload do arquivo CSV na barra lateral para começar a análise.")
        
        # Instruções
        with st.expander("ℹ️ Instruções de Uso"):
            st.markdown("""
            ### Como usar este dashboard:
            
            1. **Upload do Arquivo**: Use a barra lateral para fazer upload do arquivo CSV da pesquisa
            2. **Visualização Automática**: O dashboard processará os dados automaticamente
            3. **Navegação por Abas**: Use as abas para explorar diferentes aspectos da análise
            4. **Métricas Interativas**: Todos os gráficos são interativos - você pode fazer zoom, filtrar, etc.
            5. **Cruzamentos**: Nova aba para análises de correlação entre variáveis
            
            ### Funcionalidades:
            - ✅ Análise automática de dados ausentes
            - ✅ Cálculo de métricas estatísticas profissionais
            - ✅ Visualizações interativas
            - ✅ Análises de cruzamento entre variáveis
            - ✅ Download dos dados processados
            - ✅ Interface responsiva
            """)


if __name__ == "__main__":
    main()